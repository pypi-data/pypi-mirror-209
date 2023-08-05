# -*- coding: utf-8 -*-

import pynamodb_mate as pm
from sftp_to_s3.tests.boto_ses import bsm

# prepare Pynamodb connection
with bsm.awscli():
    connection = pm.Connection()
