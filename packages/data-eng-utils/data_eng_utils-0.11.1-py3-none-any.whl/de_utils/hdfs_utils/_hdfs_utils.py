"""A collection of HDFS utils."""
# python imports
import re
import subprocess
from typing import List, Union

# import local modules
from de_utils._utils import enforce_type_hints
from de_utils.hdfs_utils._hdfs_utils_exception import HdfsUtilsException


def _perform(command, str_output=False, shell=False):
    """Run shell command in subprocess returning exit code or full string output."""
    process = subprocess.Popen(
        command,
        shell=shell,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    stdout, stderr = process.communicate()

    if str_output:
        if stderr:
            raise HdfsUtilsException(stderr.decode("UTF-8").strip("\n"))
        return stdout.decode("UTF-8").strip("\n")

    return process.returncode


def isfile(path):
    """
    Test if file exists. Uses 'hadoop fs -test -f.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.

    Note:
        If checking that directory with partitioned files (i.e. csv, parquet)
        exists this will return false use isdir instead.
    """
    command = ["hadoop", "fs", "-test", "-f", path]
    return _perform(command)


def isdir(path):
    """
    Test if directory exists. Uses 'hadoop fs -test -d'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-test", "-d", path]
    return _perform(command)


def create_dir(path):
    """
    Create a directory. Uses 'hadoop fs -mkdir'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-mkdir", path]
    return _perform(command)


def delete_file(path):
    """
    Delete a file. Uses 'hadoop fs -rm'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-rm", path]
    return _perform(command)


def delete_dir(path):
    """
    Delete a directory. Uses 'hadoop fs -rmdir'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-rmdir", path]
    return _perform(command)


def rename(from_path, to_path, overwrite=False):
    """
    Rename (i.e. move using full path) a file. Uses 'hadoop fs -mv'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    # move fails if target file exists and no -f option available
    if overwrite:
        delete_file(to_path)

    command = ["hadoop", "fs", "-mv", from_path, to_path]
    return _perform(command)


def copy(from_path, to_path, overwrite=False):
    """
    Copy a file. Uses 'hadoop fs -cp'.

    Args: path (String)

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    if overwrite:
        return _perform(["hadoop", "fs", "-cp", "-f", from_path, to_path])
    else:
        return _perform(["hadoop", "fs", "-cp", from_path, to_path])


def copy_local_to_hdfs(from_path, to_path):
    """
    Move or copy a local file to HDFS.

    Args:
        from_path (String): path to local file
        to_path (String): path of where file should be placed in HDFS

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-copyFromLocal", from_path, to_path]
    return _perform(command)


def copy_hdfs_to_local(from_path, to_path):
    """
    Move or copy a HDFS file to local.

    Args:
        from_path (String): path to HDFS file.
        to_path (String): path of where file should be placed locally.

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-copyToLocal", from_path, to_path]
    return _perform(command)


def move_local_to_hdfs(from_path, to_path):
    """
    Move a local file to HDFS.

    Args:
        from_path (String): path to local file
        to_path (String): path of where file should be placed in HDFS

    Returns:
        bool: Returns True for successfully completed operation. Else False.
    """
    command = ["hadoop", "fs", "-moveFromLocal", from_path, to_path]
    return _perform(command)


def read_header(path, n=1):
    """Reads the first n lines of a file on HDFS."""
    return _perform(f"hadoop fs -cat {path} | head -{n}", shell=True, str_output=True, ignore_error=True)


def hdfs_size(path):
    """Return file size in bytes, not to be confused space consumed on disk which factors in replication."""
    command = ["hadoop", "fs", "-du", "-s", path]
    return _perform(command, str_output=True).split(" ")[0]


def hdfs_md5sum(path):
    """Get md5sum of a specific file on HDFS."""
    cmd = f"hadoop fs -cat '{path}' | md5sum"
    return _perform(cmd, shell=True, str_output=True).split(" ")[0]


def dir_size(path):
    """
    Get HDFS directory size.

    Args:
        path (String): path to HDFS directory

    Returns:
        str - [size] [disk space consumed] [path]
        Hadoop replicates data for resilience, disk space consumed is size x replication.
    """
    command = ["hadoop", "fs", "-du", "-s", "-h", path]
    return _perform(command, True)


@enforce_type_hints(['level', 'recursive'])
def list_contents(
    paths: Union[str, List[str]],
    level: str = 'path',
    recursive: bool = False,
) -> List[str]:
    """Read contents of a directory returning the full path or metadata for each file.

    Parameters
    ----------
    paths : str or List[str]
        single path or a list of paths.

    level : str
        The default is 'path' of the object, 'metadata' will all metadata and 'filename'
        only the name of all objects in the dir.

    recursive : bool
        Default is False.

    Note
    ----
    Accepts wildcard/ glob pattern filtering syntax, e.g. the below will only return
    files names that are .gz files from the 2010's (201[0,1,2,..,9]) e.g.
    >>> list_contents('/dapsen/landing_zone/retailer/historic/201*/v1/*.gz', 'filename')
    """
    valid_args = ['path', 'filename', 'metadata']
    if level not in [None] + valid_args:
        raise ValueError(
            f"`level` accepted arguments are {', '.join(valid_args)}")

    if isinstance(paths, list):
        return [p for ps in paths for p in list_contents(ps, level, recursive)]

    command = ["hadoop", "fs", "-ls"]

    if recursive:
        command.append("-R")

    ls = subprocess.Popen([*command, paths],
                          stdout=subprocess.PIPE)
    files = []

    for line in ls.stdout:
        f = line.decode("utf-8")
        if 'Found' not in f:
            metadata, file_path = re.split(r'[ ](?=/)', f)
            files.append(metadata.split() + [file_path[:-1]])

    if level == 'metadata':
        return files

    elif level == 'path':
        return [f[-1] for f in files]

    elif level == 'filename':
        return [f.split('/')[-1] for f in [f[-1] for f in files]]
