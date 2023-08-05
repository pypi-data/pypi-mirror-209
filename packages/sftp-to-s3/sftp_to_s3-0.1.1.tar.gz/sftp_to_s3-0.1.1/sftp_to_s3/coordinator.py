# -*- coding: utf-8 -*-

"""
This module implements the coordinator logics with status tracking in DynamoDB.
It can fit into any computational resource, e.g. AWS Lambda, AWS Batch, etc.
"""

import typing as T
import uuid
from pathlib import Path
from datetime import datetime, timezone

from paramiko import SFTPClient
from boto_session_manager import BotoSesManager
from pathlib_mate.mate_tool_box import repr_data_size
from s3pathlib import S3Path

from .logger import logger
from .tracker import (
    StatusEnum,
    PartitionTracker,
    PartitionData,
    RequestTracker,
    RequestData,
)
from .download import (
    Request,
    plan_requests,
)

if T.TYPE_CHECKING:
    from pathlib_mate import Path as Path1

    PathType = T.Union[str, Path, Path1]


@logger.start_and_end(
    msg="plan download requests for partition {partition_key}",
)
def plan_download_requests_for_partition(
    partition_key: str,
    dir_root: "PathType",
    s3uri_root: str,
    s3uri_requests: str,
    sftp_client: SFTPClient,
    bsm: BotoSesManager,
    max_files: int,
    max_size: int,
) -> T.List[Request]:
    """
    A wrapper of :func:`sftp_to_s3.download.plan_requests`, added DynamoDB tracking
    logics and lots of logging. It scans the SFTP directory, split files into
    micro batch, and save the micro batch information into DynamoDB.

    :param partition_key: the partition name, e.g. ``part0001``.
    :param dir_root: the source folder of this partition on SFTP server.
        example ``/home/username/data/part0001``
    :param s3uri_root: the destination folder of this partition on S3.
        example ``s3://mybucket/home/username/data/part0001/``
    :param s3uri_requests: where you store the request metadata,
        it has to be an S3 folder. And the final S3 file would be
        ``${s3uri_requests}/${partition_key}/${request_id}.json``
    :param sftp_client: SFTP client object.
    :param bsm: boto session manager object.
    :param max_files: maximum number of files in a batch
    :param max_size: maximum total size (in bytes) of files in a batch

    :return: list of :class:`~sftp_to_s3.download.Request` object about to
        sent to the worker.
    """
    logger.info(f"split files into batches ...")
    dir_root = Path(dir_root)
    batches = plan_requests(
        sftp_client=sftp_client,
        dir_root=dir_root,
        s3uri_root=s3uri_root,
        max_files=max_files,
        max_size=max_size,
    )
    request_list = list()
    request_tracker_list = list()
    n_files = 0
    total_size = 0
    for batch in batches:
        n_files += batch.n_files
        total_size += batch.total_size
        request_id = uuid.uuid4().hex
        request = Request.from_batch(
            bsm=bsm,
            partition_key=partition_key,
            request_id=request_id,
            batch=batch,
            s3uri_requests_dir=s3uri_requests,
        )
        request_list.append(request)
        request_tracker = RequestTracker.new(
            job_id=partition_key,
            task_id=request_id,
            data=RequestData(
                sftp_dir=str(dir_root),
                s3_dir=s3uri_root,
                partition_key=request.partition_key,
                request_id=request.request_id,
                s3uri_batch=request.s3uri_batch,
                n_files=batch.n_files,
                total_size=batch.total_size,
            ),
            save=True,
        )
        request_tracker_list.append(request_tracker)

    n_batches = len(request_list)
    logger.info(f"- total number of batches: {n_batches}")
    logger.info(f"- total number of files: {n_files}")
    logger.info(f"- total file size: {repr_data_size(total_size)}")

    logger.info(f"initialize Dynamodb tracker items ...")
    with RequestTracker.batch_write() as batch:
        for request_tracker in request_tracker_list:
            batch.save(request_tracker)

    PartitionTracker.new(
        task_id=partition_key,
        data=PartitionData(
            sftp_dir=str(dir_root),
            s3_dir=s3uri_root,
            n_files=n_files,
            total_size=total_size,
            n_batches=n_batches,
            n_succeeded_batches=0,
        ),
        save=True,
    )

    return request_list


def redo_partition(
    partition_key: str,
    s3uri_backup: str,
    s3uri_requests: str,
    sftp_client: SFTPClient,
    bsm: BotoSesManager,
    max_files: int,
    max_size: int,
) -> T.List[Request]:
    """
    :param partition_key: the partition name, e.g. ``part0001``.
    :param s3uri_backup: where you store the backup of the requests data and
        downloaded files. it has to be an S3 folder. Final backup destination
        would be:
        - ``${s3uri_backup}/${partition_key}/backup-${datetime}/download/files...``
        - ``${s3uri_backup}/${partition_key}/backup-${datetime}/requests/${request_id}.json``
    :param s3uri_requests: where you store the request metadata,
        it has to be an S3 folder. And the final S3 file would be
        ``${s3uri_requests}/${partition_key}/${request_id}.json``
    :param sftp_client: SFTP client object.
    :param bsm: boto session manager object.
    :param max_files: maximum number of files in a batch
    :param max_size: maximum total size (in bytes) of files in a batch

    :return: list of :class:`~sftp_to_s3.download.Request` object about to
        sent to the worker.

    Todo: add logic to handle existing file or duplicate file name. Keep? Remove? Backup? Skip? Overwrite?
    """
    partition_tracker = PartitionTracker.get_one_or_none(task_id=partition_key)

    # backup existing requests data and downloaded files
    utcnow = datetime.utcnow().replace(tzinfo=timezone.utc)
    utcnow_str = utcnow.strftime("%Y-%m-%d-%H-%M-%S")

    s3dir_partition = S3Path(partition_tracker.data.s3_dir).to_dir()
    s3dir_request = S3Path(s3uri_requests).joinpath(partition_key).to_dir()
    s3dir_backup = (
        S3Path(s3uri_backup).joinpath(partition_key, f"backup-{utcnow_str}").to_dir()
    )
    s3dir_partition_backup = s3dir_backup.joinpath("download").to_dir()
    s3dir_request_backup = s3dir_backup.joinpath("requests").to_dir()

    s3dir_partition.move_to(dst=s3dir_partition_backup, bsm=bsm)
    s3dir_request.move_to(dst=s3dir_request_backup, bsm=bsm)

    # delete related DynamoDB items
    with RequestTracker.batch_write():
        for request_tracker in RequestTracker.query_by_status(
            job_id=partition_tracker.task_id,
            status=[
                StatusEnum.s00_todo.value,
                StatusEnum.s03_in_progress.value,
                StatusEnum.s06_failed.value,
                StatusEnum.s09_success.value,
                StatusEnum.s10_ignore.value,
            ],
            auto_refresh=False,
            limit=1000,
        ):
            request_tracker.delete()

    partition_tracker.delete()

    # Re-plan the download request for this partition
    request_list = plan_download_requests_for_partition(
        partition_key=partition_tracker.task_id,
        dir_root=partition_tracker.data.sftp_dir,
        s3uri_root=partition_tracker.data.s3_dir,
        s3uri_requests=s3uri_requests,
        sftp_client=sftp_client,
        bsm=bsm,
        max_files=max_files,
        max_size=max_size,
    )

    return request_list


def retry_partition(
    partition_key: str,
) -> T.List[Request]:
    """
    Retry those failed requests in a partition.

    :param partition_key: the partition name, e.g. ``part0001``.

    :return: list of :class:`~sftp_to_s3.download.Request` object about to
        sent to the worker.
    """
    # get unfinished requests DynamoDB item
    result = RequestTracker.query_by_status(
        job_id=partition_key,
        status=[
            StatusEnum.s00_todo.value,
            StatusEnum.s06_failed.value,
        ],
        auto_refresh=True,
        limit=1000,
    ).filter(lambda request_tracker: request_tracker.is_locked() is False)

    # convert DynamoDB item to request object
    request_list = [
        Request(
            partition_key=partition_key,
            request_id=request_tracker.task_id,
            s3uri_batch=request_tracker.data.s3uri_batch,
        )
        for request_tracker in result
    ]

    return request_list
