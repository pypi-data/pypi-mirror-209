# -*- coding: utf-8 -*-

import typing as T
from sftp_to_s3.sftp_pathlib import (
    write_bytes,
    write_text,
    read_bytes,
    read_text,
    walk,
    rmtree,
)
from sftp_to_s3.tests import sftp_client, sftp_dir_home


def _test_walk():
    dir_root = sftp_dir_home.joinpath("sftp_pathlib/walk")

    rmtree(sftp_client, dir_root)

    p_readme = dir_root.joinpath("readme.txt")

    p_folder1 = dir_root.joinpath("folder1")
    p_folder1_file1 = p_folder1.joinpath("file11.txt")
    p_folder1_file2 = p_folder1.joinpath("file12.txt")

    p_folder2 = dir_root.joinpath("folder2")
    p_folder2_file1 = p_folder2.joinpath("file21.txt")
    p_folder2_file2 = p_folder2.joinpath("file22.txt")

    p_folder_subfolder11 = p_folder1.joinpath("subfolder11")
    p_folder_subfolder11_file = p_folder_subfolder11.joinpath("subfolderfile11.txt")

    p_folder_subfolder21 = p_folder2.joinpath("subfolder21")
    p_folder_subfolder21_file = p_folder_subfolder21.joinpath("subfolderfile21.txt")

    write_text(sftp_client, p_readme, "Read me please!")
    write_text(sftp_client, p_folder1_file1, "file11 content")
    write_text(sftp_client, p_folder1_file2, "file12 content")
    write_text(sftp_client, p_folder2_file1, "file21 content")
    write_text(sftp_client, p_folder2_file2, "file22 content")
    write_text(sftp_client, p_folder_subfolder11_file, "subfolderfile11 content")
    write_text(sftp_client, p_folder_subfolder21_file, "subfolderfile21 content")

    p_cwd_list: T.List[str] = list()
    dirs_list: T.List[str] = list()
    files_list: T.List[str] = list()
    for p_cwd, dirs, files in walk(sftp_client, dir_root):
        p_cwd_list.append(str(p_cwd.relative_to(dir_root)))
        dirs_list.extend([str(p.path.relative_to(dir_root)) for p in dirs])
        files_list.extend([str(p.path.relative_to(dir_root)) for p in files])
    #     print("-" * 80)
    #     print(f"p_cwd = {p_cwd}")
    #     print(f"dirs = {dirs}")
    #     print(f"files = {files}")
    #     pass
    #
    # print(p_cwd_list)
    # print(dirs_list)
    # print(files_list)

    assert p_cwd_list == [
        ".",
        "folder1",
        "folder1/subfolder11",
        "folder2",
        "folder2/subfolder21",
    ]
    assert dirs_list == [
        "folder1",
        "folder2",
        "folder1/subfolder11",
        "folder2/subfolder21",
    ]
    assert files_list == [
        "readme.txt",
        "folder1/file11.txt",
        "folder1/file12.txt",
        "folder1/subfolder11/subfolderfile11.txt",
        "folder2/file21.txt",
        "folder2/file22.txt",
        "folder2/subfolder21/subfolderfile21.txt",
    ]

    rmtree(sftp_client, dir_root)


def test():
    print("")
    _test_walk()


if __name__ == "__main__":
    from sftp_to_s3.tests import run_cov_test

    run_cov_test(__file__, "sftp_to_s3.sftp_pathlib", preview=False)
