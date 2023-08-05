# -*- coding: utf-8 -*-

"""
This module implements the worker logics with status tracking in DynamoDB.
It can fit into any computational resource, e.g. AWS Lambda, AWS Batch, etc.
"""

from paramiko import SFTPClient
from boto_session_manager import BotoSesManager
from pathlib_mate.mate_tool_box import repr_data_size


from .logger import logger
from .tracker import (
    PartitionTracker,
    RequestTracker,
)
from .download import (
    Request,
    download_file,
)


@logger.start_and_end(
    msg="download batch for request {request.request_id}",
)
def download_batch(
    request: Request,
    sftp_client: SFTPClient,
    bsm: BotoSesManager,
):
    """
    A wrapper of :func:`~sftp_to_s3.download.process_request`, added
    DynamoDB tracking logics and lots of logging.

    :param request: the :class`~sftp_to_s3.download.Request` object.
    :param sftp_client: the SFTP client object.
    :param bsm: boto session manager object.
    """
    logger.info(f"processing request:")
    logger.info(f"- partition key: {request.partition_key}")
    logger.info(f"- request id: {request.request_id}")

    request_tracker = RequestTracker.get_one_or_none(
        job_id=request.partition_key,
        task_id=request.request_id,
    )
    with request_tracker.start_job(debug=False):
        batch = request.get_batch(bsm=bsm)
        logger.info(f"copy files from {batch.dir_root!r} to {batch.s3uri_root!r}")
        logger.info(f"- n_files: {batch.n_files}")
        logger.info(f"- total_size: {repr_data_size(batch.total_size)}")
        for ith, path in enumerate(batch.files, start=1):
            logger.info(f"copy {ith}th file {path!r} ...")
            s3path = download_file(
                sftp_client=sftp_client,
                path=path,
                dir_root=batch.dir_root,
                bsm=bsm,
                s3uri_root=batch.s3uri_root,
            )
            logger.info(f"copied to: {s3path.uri}", 1)

    partition_tracker = PartitionTracker.new(task_id=request.partition_key, save=False)
    partition_tracker.update(
        actions=[
            PartitionTracker.data.n_succeeded_batches.set(
                PartitionTracker.data.n_succeeded_batches + 1
            ),
        ],
    )
