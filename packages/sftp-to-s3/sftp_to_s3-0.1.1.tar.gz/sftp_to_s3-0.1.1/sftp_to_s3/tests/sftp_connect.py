# -*- coding: utf-8 -*-

import json
import dataclasses
from io import StringIO


from paramiko import AutoAddPolicy, SFTPClient, SSHClient
from paramiko import RSAKey

from .paths import path_test_config, path_pkey


def sftp_connect(
    sftp_hostname: str,
    sftp_port: int,
    sftp_username: str,
    ssh_private_key: str,
    ssh_password: str,
) -> SFTPClient:
    private_key = RSAKey.from_private_key(
        StringIO(ssh_private_key),
        password=ssh_password,
    )
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(
        hostname=sftp_hostname,
        username=sftp_username,
        port=sftp_port,
        pkey=private_key,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp_client = ssh_client.open_sftp()
    return sftp_client


@dataclasses.dataclass
class TestConfig:
    sftp_hostname: str = dataclasses.field()
    sftp_username: str = dataclasses.field()
    ssh_password: str = dataclasses.field()
    s3uri_requests: str = dataclasses.field()
    s3uri_download: str = dataclasses.field()
    s3uri_backup: str = dataclasses.field()

    @classmethod
    def get(cls) -> "TestConfig":
        return cls(**json.loads(path_test_config.read_text()))


test_config = TestConfig.get()
sftp_client = sftp_connect(
    sftp_hostname=test_config.sftp_hostname,
    sftp_port=22,
    sftp_username=test_config.sftp_username,
    ssh_private_key=path_pkey.read_text(),
    ssh_password=test_config.ssh_password,
)
