"""Utility tools for Spark."""
# import modules
import logging as _logging

from ._spark_utils import (
    get_spark_ui, get_active_session, get_ss, get_hive_context, named_cache,
    named_persist, named_unpersist, align_date_to_a_specific_weekday, any_in,
    assert_active_ss, union_by_name, rm_spaces, eagerEval, melt, cast_columns
)

from ._column_utils import (
    flag_invalid_regex, flag_invalid_values, guid,
    sha256_hash, uuid
)

from ._validation import validate_nhs_no, validate_vat_no

from ._nspl import (
    region_code_to_name,
    with_postcode_map_nspl,
    map_pcd_to_regions,
)

_logging.getLogger(__name__)

__all__ = [
    "align_date_to_a_specific_weekday", "any_in", "assert_active_ss",
    "flag_invalid_regex", "flag_invalid_values", "get_active_session",
    "get_hive_context", "get_spark_ui", "get_ss", "guid",
    "named_cache", "named_persist", "named_unpersist", "sha256_hash", "uuid",
    "validate_nhs_no", "validate_vat_no", "union_by_name", "rm_spaces",
    "map_pcd_to_regions", "region_code_to_name", "with_postcode_map_nspl",
    "rm_spaces", "eagerEval", "melt", "cast_columns"
]
