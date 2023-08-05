# -*- coding: utf-8 -*-

from sftp_to_s3.tracker import PartitionTracker, RequestTracker

from .boto_ses import bsm

_ = bsm

table_name = "example-sftp-to-s3-status-tracker"
region = "us-east-1"

# define the table name and region
PartitionTracker.Meta.table_name = table_name
PartitionTracker.Meta.region = region

RequestTracker.Meta.table_name = table_name
RequestTracker.Meta.region = region

# you can uncomment this to create the table manually
# PartitionTracker.create_table(wait=True)
