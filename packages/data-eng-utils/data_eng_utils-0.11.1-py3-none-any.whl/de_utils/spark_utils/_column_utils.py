"""Utility functions that act on pysark columns."""
from collections import Iterable
from pyspark.sql import functions as F
from pyspark.sql.column import Column


def _check_any_matches(iter1, iter2):
    """Check for any matches between values in two iterables.

    Returns True if there are any values in common.
    """
    return any([item in iter2 for item in iter1])


def _test_column_type(col):
    """Test if a variable is a pyspark column."""
    if not isinstance(col, Column):
        raise TypeError("col must be pyspark.sql.column.Column type")


def flag_invalid_values(col, *valid_values):
    """Check if values in a column are valid.

    :param col: pyspark column to test
    :type col: pyspark.sql.column.Column

    :param *valid_values: one or more valid values
    :type *valid_values: various, to match data in col

    :returns: a column that is True when data are invalid and
    False when data are valid or null
    :rtype: pyspark.sql.column.Column
    """
    _test_column_type(col)
    return (~ col.isin(*valid_values)) & (col.isNotNull())


def flag_invalid_regex(col, regex):
    """Flag values that do not meet a given regular expression.

    Carries out validation of a column by checking whether data
    meets a give regular expression. Values that fail to match
    the regex are deemed to have failed the validation and are
    flagged as True. Null values or values that match the regex
    are flagged as False.
    """
    _test_column_type(col)
    return (~ col.rlike(regex)) & (col.isNotNull())


def sha256_hash(col, salt=None):
    """Hash a column of data.

    Sha256 hash a column of data concatenated with an optional salt.
    The optional salt can be provided as a pyspark column with
    different salts for each record in the data column, or as a single
    string, in which case the same salt is used for every record.

    Note, a null values in either the col will result in null hashes
    being output for the affected records. A null salt will be treated
    as an empty string.

    :param col: column of data to hash
    :type col: pyspark.sql.column.Column

    :param salt: salt to concatenate with data prior to hashing
    :type salt: str or pyspark.sql.column.Column
    """
    _test_column_type(col)
    if salt is not None:
        col = F.concat(salt if isinstance(salt, Column) else F.lit(salt), col)
    return F.sha2(col, 256)


def uuid():
    """Get a column of unique IDs.

    :returns: a universally unique identifier (UUID) string. The value is
    returned as a canonical UUID 36-character string
    :rtype: pyspark.sql.column.Column
    """
    return F.expr("uuid()")


def guid():
    """Get a column of unique IDs.

    Alias for uuid.
    :returns: a universally unique identifier (UUID) string. The value is
    returned as a canonical UUID 36-character string
    :rtype: pyspark.sql.column.Column
    """
    return uuid()
