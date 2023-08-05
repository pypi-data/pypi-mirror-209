# -*- coding: utf-8 -*-

"""
This module brings status tracking into the SFTP to S3 ingestion process,
allow you to track the status of each partition and each batch.
"""

import typing as T
import pynamodb_mate as pm


class StatusEnum(pm.patterns.status_tracker.BaseStatusEnum):
    """
    The status enum for the SFTP to S3 ingestion process.
    """

    s00_todo = 0
    s03_in_progress = 3
    s06_failed = 6
    s09_success = 9
    s10_ignore = 10


class Tracker(pm.patterns.status_tracker.BaseStatusTracker):
    STATUS_ZERO_PAD = 3
    MAX_RETRY = 3
    LOCK_EXPIRE_SECONDS = 900
    DEFAULT_STATUS = StatusEnum.s00_todo.value
    STATUS_ENUM = StatusEnum

    def start_job(
        self,
        debug=True,
    ) -> "Tracker":
        return self.start(
            in_process_status=StatusEnum.s03_in_progress,
            failed_status=StatusEnum.s06_failed,
            success_status=StatusEnum.s09_success,
            ignore_status=StatusEnum.s10_ignore,
            debug=debug,
        )


class PartitionData(pm.MapAttribute):
    """
    User data structure for partition tracker.

    :param sftp_dir: the SFTP directory name of this partition
    :param s3_dir: the S3 folder uri of this partition
    :param n_files: number of files in this partition
    :param total_size: total size of all files in this partition
    :param n_batches: number of batches in this partition
    :param n_succeeded_batches: number of succeeded batches in this partition

    If ``n_succeeded_batches`` is equal to ``n_batches``, then this partition
    is considered as "succeeded".
    """

    sftp_dir: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    s3_dir: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    n_files: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()
    total_size: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()
    n_batches: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()
    n_succeeded_batches: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()


class RequestData(pm.MapAttribute):
    """
    User data structure for partition tracker.

    :param sftp_dir: the SFTP directory name of this partition
    :param s3_dir: the S3 folder uri of this partition
    :param partition_key: the partition key of the request belongs to
    :param request_id: the unique request id
    :param s3uri_batch: the S3 URI where the batch data is stored. It has to be
        a JSON file on S3.
    :param n_files: number of files in this batch
    :param total_size: total size of all files in this batch
    """

    sftp_dir: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    s3_dir: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    partition_key: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    request_id: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    s3uri_batch: T.Union[str, pm.UnicodeAttribute] = pm.UnicodeAttribute()
    n_files: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()
    total_size: T.Union[int, pm.NumberAttribute] = pm.NumberAttribute()


PARTITION_TRACKER_JOB_ID = "partitions"


# Developer note, since there are two models (PartitionTracker and RequestTracker)
# sharing the same index class, the index class uses it's Meta class attribute
# to track who is the owner table of the index, we have to explicitly create
# two Index class and Meta attribute for each model. Otherwise, the index class
# won't be able to figure out who is the owner table.
class PartitionTrackerIndex(pm.patterns.status_tracker.StatusAndUpdateTimeIndex):
    class Meta:
        index_name = "status_and_update_time-index"
        projection = pm.IncludeProjection(["create_time"])


class RequestTrackerIndex(pm.patterns.status_tracker.StatusAndUpdateTimeIndex):
    class Meta:
        index_name = "status_and_update_time-index"
        projection = pm.IncludeProjection(["create_time"])


class PartitionTracker(Tracker):
    """
    The Partition download status tracker DynamoDB model.
    """

    class Meta:
        table_name = None
        region = None
        billing_mode = pm.PAY_PER_REQUEST_BILLING_MODE

    JOB_ID = PARTITION_TRACKER_JOB_ID

    data: T.Union[dict, PartitionData] = PartitionData()

    status_and_update_time_index = PartitionTrackerIndex()


class RequestTracker(Tracker):
    """
    The Request download status tracker DynamoDB model.
    """

    class Meta:
        table_name = None
        region = None
        billing_mode = pm.PAY_PER_REQUEST_BILLING_MODE

    data: T.Union[dict, RequestData] = RequestData()

    status_and_update_time_index = RequestTrackerIndex()
