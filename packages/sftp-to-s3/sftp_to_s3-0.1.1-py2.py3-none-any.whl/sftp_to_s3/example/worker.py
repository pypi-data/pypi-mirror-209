# -*- coding: utf-8 -*-

from sftp_to_s3 import api
from sftp_to_s3.tests import sftp_client
from sftp_to_s3.tests.boto_ses import bsm


def process_request(request: api.Request):
    api.download_batch(
        request=request,
        sftp_client=sftp_client,
        bsm=bsm,
    )


def lambda_handler(event: dict, context):
    request = api.Request(
        partition_key=event["partition_key"],
        request_id=event["request_id"],
        s3uri_batch=event["s3uri_batch"],
    )
    process_request(request=request)
