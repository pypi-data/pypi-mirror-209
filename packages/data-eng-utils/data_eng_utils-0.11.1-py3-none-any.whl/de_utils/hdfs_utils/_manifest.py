import json
import os

from de_utils.hdfs_utils import isfile, hdfs_md5sum, hdfs_size


def _add_manifest_entry(filepath):
    return {
        "file": os.path.basename(filepath),
        "relativePath": os.path.dirname(filepath),
        "sizeBytes": hdfs_size(filepath),
        "md5sum": hdfs_md5sum(filepath),
    }


def create_manifest(filepaths, name, path = None):
    """Create manifest of files in the format NiFi accepts for CIA to migrate data from DAP.

    Parameters
    ------
    filepaths: List[str]
        List of filepaths

    name: string
        The name of the manifest

    path: string
        Default is to save to current working directory, alternatively provide path
        to save to

    Notes
    -----
    To get filepaths from HDFS programatically use hdfs_utils.list_contents
    """
    d = {
        'files': [_add_manifest_entry(fp) for fp in filepaths if isfile(fp)==0],
        'headers':''
    }
    with open(f"{name}.mani", 'w') as fp:
        json.dump(d, fp, sort_keys=True, indent=4)
