# -*- coding: utf-8 -*-

"""
This module contains the logics for splitting large number of files into
smaller batches, and download them in parallel with workers.
"""

import typing as T
import json
import dataclasses
from pathlib import Path

from paramiko import SFTPClient
from s3pathlib import S3Path
from func_args import NOTHING
from boto_session_manager import BotoSesManager

from .sftp_pathlib import walk


if T.TYPE_CHECKING:
    from pathlib_mate import Path as Path1

    PathType = T.Union[str, Path, Path1]


@dataclasses.dataclass
class Base:
    """
    Base class for dataclass.
    """

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


# ------------------------------------------------------------------------------
# Micro batch download worker logics
# ------------------------------------------------------------------------------
@dataclasses.dataclass
class Batch(Base):
    """
    Represent a batch of files to download from sftp server.

    :param dir_root: where the files are located on sftp server.
    :param files: list of file absolute path on sftp server.
    :param n_files: number of files in this batch.
    :param total_size: total size of all files in this batch.
    :param s3uri_root: where the files will be copied to on s3.

    When ``dir_root`` is ``/home/user``, ``s3uri_root`` is ``s3://mybucket/home/user``.
    Then all files in ``/home/user`` will be copied to ``s3://mybucket/home/user``.

    Example SFTP server::

        /home/user/folder/file.txt
        /home/user/folder/
        /home/user/log.txt

    Example S3 bucket::

        s3://mybucket/home/user/folder/file.txt
        s3://mybucket/home/user/folder/
        s3://mybucket/home/user/log.txt
    """

    dir_root: str
    files: T.List[str]
    n_files: int
    total_size: int
    s3uri_root: str

    @classmethod
    def from_s3(
        cls,
        bsm: BotoSesManager,
        s3uri: str,
    ) -> "Batch":
        """
        Create a :class:`Batch` object from a S3 file where the batch data is
         stored in JSON.

        :param bsm: boto session manager object.
        :param s3uri: the S3 URI where the batch data is stored.
        :return: a :class:`Batch` object.
        """
        s3path = S3Path(s3uri)
        data = json.loads(s3path.read_text(bsm=bsm))
        return cls(
            dir_root=data["dir_root"],
            files=data["files"],
            n_files=data["n_files"],
            total_size=data["total_size"],
            s3uri_root=data["s3uri_root"],
        )

    def to_s3(
        self,
        bsm: BotoSesManager,
        s3uri: str,
    ) -> S3Path:
        """
        Dump a :class:`Batch` object to a S3 file.

        :param bsm: boto session manager object.
        :param s3uri: the S3 URI where the batch data will be stored.
        :return: S3Path object of where the batch data will be stored.
        """
        s3path = S3Path(s3uri)
        s3path.write_text(
            json.dumps(dataclasses.asdict(self)),
            content_type="application/json",
            bsm=bsm,
        )
        return s3path


@dataclasses.dataclass
class Request(Base):
    """
    Represent a request sent from coordinator to worker to download a batch of files
    from SFTP server to S3 bucket.

    A request is a very light-weight object, it only contains the information of
    identifier of the batch data on S3. The real batch data is stored on S3.
    The request object is always small enough to be sent over network.

    :param partition_key: the partition name, e.g. ``part0001``.
    :param request_id: unique identifier for this request, can be used to track the status
        of this request.
    :param s3uri_batch: the S3 URI where the batch data is stored. It has to be
        a JSON file on S3.
    """

    partition_key: str
    request_id: str
    s3uri_batch: str

    def get_batch(
        self,
        bsm: BotoSesManager,
    ) -> Batch:
        """
        Get the batch data from S3. A wrapper of :meth:`Batch.from_s3`.

        :param bsm: boto session manager object.
        :return: a :class`Batch` object.
        """
        return Batch.from_s3(bsm=bsm, s3uri=self.s3uri_batch)

    @classmethod
    def from_batch(
        cls,
        bsm: BotoSesManager,
        partition_key: str,
        request_id: str,
        batch: Batch,
        s3uri_requests_dir: str,
    ) -> "Request":
        """
        Create a request object from a batch object.

        :param bsm: boto session manager object.
        :param partition_key: the partition name, e.g. ``part0001``.
        :param request_id: unique identifier for this request, can be used to track the status
            of this request.
        :param batch: a :class`Batch` object.
        :param s3uri_requests_dir: where you store the request metadata,
            it has to be an S3 folder. And the final S3 file would be
            ``${s3uri_requests_dir}/${partition_key}/${request_id}.json``
        :return: a :class`Request` object.
        """
        s3path_batch = S3Path(s3uri_requests_dir).joinpath(
            partition_key, f"{request_id}.json"
        )
        batch.to_s3(bsm=bsm, s3uri=s3path_batch.uri)
        return cls(
            partition_key=partition_key,
            request_id=request_id,
            s3uri_batch=s3path_batch.uri,
        )


def download_file(
    sftp_client: SFTPClient,
    path: "PathType",
    dir_root: "PathType",
    bsm: BotoSesManager,
    s3uri_root: str,
    metadata: T.Dict[str, str] = NOTHING,
    tags: T.Dict[str, str] = NOTHING,
) -> S3Path:
    """
    Download one file from SFTP server to S3 bucket.

    :param sftp_client: SFTP client object.
    :param path: the absolute path of the file on SFTP server.
    :param dir_root: the logical "root directory" of the file on SFTP server.
    :param bsm: boto session manager object.
    :param s3uri_root: the logical "root directory" of the file on S3 bucket.
        the final s3uri of the file will be ``s3uri_root/path.relative_to(dir_root)``.
    :param metadata: S3 object metadata.
    :param tags: S3 object tagging.
    :return:

    Todo: preserve file metadata on SFTP as s3 object metadata
    Todo: compare file metadata on SFTP and S3, only download if size is different
    """
    path = Path(path)
    dir_root = Path(dir_root)
    s3dir_root = S3Path(s3uri_root)
    s3path = s3dir_root.joinpath(str(path.relative_to(dir_root)))
    with sftp_client.open(str(path), "rb") as f:
        s3path.write_bytes(f.read(), bsm=bsm, metadata=metadata, tags=tags)
    return s3path


def download_batch(
    sftp_client: SFTPClient,
    batch: Batch,
    bsm: BotoSesManager,
    metadata: T.Dict[str, str] = NOTHING,
    tags: T.Dict[str, str] = NOTHING,
) -> T.List[S3Path]:
    """
    Download a batch of files from SFTP server to S3 bucket.

    :param sftp_client: the SFTP client object.
    :param batch: the :class`Batch` object.
    :param bsm: boto session manager object.
    :param metadata: S3 object metadata.
    :param tags: S3 object tagging.
    :return:
    """
    s3path_list = list()
    for path in batch.files:
        s3path = download_file(
            sftp_client=sftp_client,
            path=path,
            dir_root=batch.dir_root,
            bsm=bsm,
            s3uri_root=batch.s3uri_root,
            metadata=metadata,
            tags=tags,
        )
        s3path_list.append(s3path)
    return s3path_list


def process_request(
    sftp_client: SFTPClient,
    request: Request,
    bsm: BotoSesManager,
):
    """
    Process a download request. This function can be used in worker's application
    code.

    :param sftp_client: the SFTP client object.
    :param request: the :class`Request` object.
    :param bsm: boto session manager object.
    :return: the :class`Batch` object.
    """
    batch = request.get_batch(bsm=bsm)
    download_batch(
        sftp_client=sftp_client,
        batch=batch,
        bsm=bsm,
    )
    return batch


# ------------------------------------------------------------------------------
# Coordinator logics
# ------------------------------------------------------------------------------
def yield_files(
    sftp_client: SFTPClient,
    dir_root: "PathType",
) -> T.Iterable[T.Tuple[str, int]]:
    """
    Recursively walk through a folder on SFTP server and yield file path and size
    pairs.

    Example::

        >>> for path, size in yield_files(sftp_client, "/home/user"):
        ...     print(path, size)
        ('/home/user/file1.txt', 100)
        ('/home/user/file2.txt', 200)
        ('/home/user/file3.txt', 300)
        ...

    :param sftp_client:
    :param dir_root:
    :return:
    """
    for p_cwd, dirs, files in walk(sftp_client, dir_root):
        for attr in files:
            yield (str(attr.path), attr.st_size)


def group_files(
    files: T.Iterable[T.Tuple[str, int]],
    max_files: int,
    max_size: int,
) -> T.Iterable[T.Tuple[T.List[str], int, int]]:
    """
    Group files into batches, make sure the total number of files and total size
    not larger than the limit.

    :param files: a list of (path, size) pairs
    :param max_files: maximum number of files in a batch
    :param max_size: maximum total size (in bytes) of files in a batch
    :return:
    """
    grouped_files: T.List[str] = list()
    n_files = 0
    total_size = 0

    for path, size in files:
        n_files += 1
        total_size += size
        grouped_files.append(path)

        if (n_files > max_files) or (total_size > max_size):
            n_files -= 1
            total_size -= size
            grouped_files.pop()
            yield (grouped_files, n_files, total_size)

            grouped_files = [path]
            n_files = 1
            total_size = size

    if len(grouped_files):
        yield (grouped_files, n_files, total_size)


def plan_requests(
    sftp_client: SFTPClient,
    dir_root: "PathType",
    s3uri_root: str,
    max_files: int,
    max_size: int,
) -> T.Iterable[Batch]:
    """
    Given a source folder for downloading and an S3 destination folder
    to store the downloaded files, this function plans the download requests
    before sending them to the download worker.

    :param sftp_client: the SFTP client object.
    :param dir_root: the source folder on SFTP server.
    :param s3uri_root: the destination folder on S3.
    :param max_files: maximum number of files in a batch
    :param max_size: maximum total size (in bytes) of files in a batch
    :return:
    """
    dir_root = Path(dir_root)
    for grouped_files, n_files, total_size in group_files(
        files=yield_files(
            sftp_client=sftp_client,
            dir_root=dir_root,
        ),
        max_files=max_files,
        max_size=max_size,
    ):
        yield Batch(
            dir_root=str(dir_root),
            files=grouped_files,
            n_files=n_files,
            total_size=total_size,
            s3uri_root=s3uri_root,
        )
