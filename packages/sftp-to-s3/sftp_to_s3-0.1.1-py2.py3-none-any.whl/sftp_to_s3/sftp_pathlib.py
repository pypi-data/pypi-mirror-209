# -*- coding: utf-8 -*-

"""
Enhance the paramiko SFTP client, provide pathlib-like interface.
"""

import typing as T
import stat
from pathlib import Path

from paramiko import SFTPClient, SFTPAttributes as SFTPAttributes_


if T.TYPE_CHECKING:
    from pathlib_mate import Path as Path1

    PathType = T.Union[str, Path, Path1]


def write_bytes(sftp_client: SFTPClient, path: "PathType", data: bytes):
    """
    Write binary data to sftp file.

    :param sftp_client:
    :param path:
    :param data:
    :return:

    Todo: allow stream write
    """
    sftp_client.open(str(Path(path)), "wb").write(data)


def write_text(sftp_client: SFTPClient, path: "PathType", data: str):
    """
    White text data to sftp file.

    :param sftp_client:
    :param path:
    :param data:
    :return:
    """
    sftp_client.open(str(Path(path)), "w").write(data)


def read_bytes(sftp_client: SFTPClient, path: "PathType") -> bytes:
    """
    Read binary data from sftp file.

    :param sftp_client:
    :param path:
    :return:

    Todo: allow stream read
    """
    return sftp_client.open(str(Path(path)), "rb").read()


def read_text(sftp_client: SFTPClient, path: "PathType") -> str:
    """
    Read text data from sftp file.

    :param sftp_client:
    :param path:
    :return:
    """
    return sftp_client.open(str(Path(path)), "rb").read().decode("utf-8")


class SFTPAttributes(SFTPAttributes_):
    """
    Enhance the paramiko SFTPAttributes class. Provide additional attribute
    ``SFTPAttributes.path`` to access the pathlib.Path object.
    """

    @property
    def path(self) -> Path:
        """
        Access the pathlib.Path object of this file.
        """
        return self.attr["pathlib.Path"]


def _path(self) -> Path:
    return self.attr["pathlib.Path"]


SFTPAttributes_.path = property(_path)


def walk(
    sftp_client: SFTPClient,
    dir_root: "PathType",
) -> T.Iterable[
    T.Tuple[
        "PathType",
        T.List["SFTPAttributes"],
        T.List["SFTPAttributes"],
    ],
]:
    """
    Recursively, depth-first-search walk through the sftp directory tree.

    :param sftp_client:
    :param dir_root:
    :return: similar to ``os.walk`` it yields a tuple includes 3 elements:
        1. current directory path
        2. list of sub-directory attributes
        3. list of file attributes
    """
    dirs, files = [], []
    for attr in sftp_client.listdir_attr(str(Path(dir_root))):
        path = Path(dir_root, attr.filename)
        attr.attr["pathlib.Path"] = path
        if stat.S_ISDIR(attr.st_mode):
            dirs.append(attr)
        else:
            files.append(attr)
    dirs = list(sorted(dirs, key=lambda x: x.path))
    files = list(sorted(files, key=lambda x: x.path))
    yield dir_root, dirs, files
    for attr in dirs:
        yield from walk(sftp_client, attr.path)


def rmtree(
    sftp_client: SFTPClient,
    dir_root: "PathType",
):
    """
    Recursively remove the directory tree.

    :param sftp_client:
    :param dir_root:
    :return:
    """
    to_remove_dirs = []
    for p_cwd, dirs, files in walk(sftp_client, dir_root):
        for attr in files:
            sftp_client.remove(str(attr.path))
        to_remove_dirs.extend(dirs)
    for attr in to_remove_dirs[::-1]:
        try:
            sftp_client.rmdir(str(attr.path))
        except FileNotFoundError:
            pass
