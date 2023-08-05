# -*- coding: utf-8 -*-

from pathlib import PosixPath
from .boto_ses import bsm
from .sftp_connect import test_config

sftp_dir_home = PosixPath(
    f"/{bsm.aws_account_id}-{bsm.aws_region}-sftp/{test_config.sftp_username}/"
)
