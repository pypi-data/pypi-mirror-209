# -*- coding: utf-8 -*-

import typing as T
from s3pathlib import S3Path

from sftp_to_s3 import api
from sftp_to_s3.tests import test_config, sftp_client, sftp_dir_home
from sftp_to_s3.tests.boto_ses import bsm

from .worker import process_request

logger = api.logger


def compare_delta() -> T.List[str]:
    """
    Compare the difference of partitions between SFTP and DynamoDB.
    """
    sftp_partition_list = [
        p.filename for p in sftp_client.listdir_attr(str(sftp_dir_home))
    ]

    # get all partition from DynamoDB, regardless of the status
    dynamodb_partition_list = [
        tracker.task_id
        for tracker in api.PartitionTracker.query_by_status(
            status=[
                api.StatusEnum.s00_todo,
                api.StatusEnum.s03_in_progress,
                api.StatusEnum.s06_failed,
                api.StatusEnum.s09_success,
                api.StatusEnum.s10_ignore,
            ]
        )
    ]

    dynamodb_partition_set = set(dynamodb_partition_list)
    todo_partition_list = [
        partition
        for partition in sftp_partition_list
        if partition not in dynamodb_partition_set
    ]
    return todo_partition_list


def send_request(request: api.Request):
    process_request(request=request)


@logger.start_and_end(msg="run coordinator")
def run_coordinator():
    todo_partition_list = compare_delta()
    todo_partition_list.sort()
    for partition_key in todo_partition_list:
        with logger.nested():
            request_list = api.plan_download_requests_for_partition(
                partition_key=partition_key,
                dir_root=sftp_dir_home.joinpath(partition_key),
                s3uri_root=S3Path(test_config.s3uri_download)
                .joinpath(partition_key)
                .uri,
                s3uri_requests=test_config.s3uri_requests,
                sftp_client=sftp_client,
                bsm=bsm,
                max_files=3,
                max_size=10 * 1000 * 1000,
            )
            for request in request_list:
                send_request(request=request)


@logger.start_and_end(
    msg="redo downloads for partition {partition_key}",
)
def redo_partition(
    partition_key: str,
):
    with logger.nested():
        request_list = api.redo_partition(
            partition_key=partition_key,
            s3uri_backup=test_config.s3uri_backup,
            s3uri_requests=test_config.s3uri_requests,
            sftp_client=sftp_client,
            bsm=bsm,
            max_files=3,
            max_size=10 * 1000 * 1000,
        )
        for request in request_list:
            send_request(request=request)


@logger.start_and_end(
    msg="retry unfinished batches for partition {partition_key}",
)
def retry_partition(
    partition_key: str,
):
    request_list = api.retry_partition(partition_key=partition_key)
    logger.info(f"got {len(request_list)} unfinished batches.")
    with logger.nested():
        for request in request_list:
            send_request(request=request)


def lambda_handler(event: dict, context):
    run_coordinator()
