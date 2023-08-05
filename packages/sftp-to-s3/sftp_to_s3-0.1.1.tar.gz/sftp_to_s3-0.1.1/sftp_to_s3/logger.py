# -*- coding: utf-8 -*-

"""
sftp_to_s3 project logging. The downloader worker and coordinator use this
logger to print debug information. To disable the logging, you can put your
application code inside the ``logger.disabled()`` context manager.

Example::

    with logger.disabled():
        # your application code here
"""

from fixa.nest_logger import NestedLogger

logger = NestedLogger(
    name="sftp_to_s3",
    log_format="%(message)s",
)

