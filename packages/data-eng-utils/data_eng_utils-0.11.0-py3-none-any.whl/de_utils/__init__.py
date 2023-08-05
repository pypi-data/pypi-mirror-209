"""Utilities for engineering data.

Documentation can be found (outside of DAP) in
file://fa1rpwapxx272/ons/ci/jenkins_home/userContent/de-utils/build/index.html
"""
import logging as _logging

from . import catalog_utils
from . import engineering_utils
from . import engineering_utils as engineering_framework
from . import hdfs_utils
from . import lookups
from . import spark_utils
from . import test_data_generation
from ._de_utils_exception import DEUtilsException
from ._utils import rm_pre_wrap, enforce_type_hints, to_list
from ._version import __version__

_log = _logging.getLogger(__name__)
_log.setLevel("INFO")
_log.addHandler(_logging.StreamHandler())


__all__ = [
    # modules
    "engineering_utils", "engineering_framework", "hdfs_utils", "spark_utils",
    "catalog_utils", "lookups", "test_data_generation",
    # functions
    "rm_pre_wrap", "enforce_type_hints", "to_list",
    # base exception
    "DEUtilsException"
]
