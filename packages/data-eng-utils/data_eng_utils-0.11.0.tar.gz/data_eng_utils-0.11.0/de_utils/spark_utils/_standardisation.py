"""A collection of Spark utils that only work in DAP."""
# import pyspark libraries
from pyspark.sql.utils import AnalysisException
from pyspark.sql import (
    functions as F,
    DataFrame,
    Column,
)

# local imports
from de_utils.spark_utils._spark_utils import get_ss


def _get_latest_lookup() -> DataFrame:
    """
    Get the latest postcode lookup table name from national_statistics_postcode_lookup.

    Returns
    --------
    DataFrame
    """
    spark = get_ss()
    db = 'national_statistics_postcode_lookup'

    # format of file name to extract date and convert back to file name
    dt_format = "'nspl_'MMM'_'yyyy'_uk_std'"

    try:
        # get name of the latest lookup table
        latest_lookup = (
            spark.sql(f"show tables from {db}")
            .agg(F.date_format(F.max(F.to_date('tableName', dt_format)), dt_format))
            .collect()[0][0]
        )
    except AnalysisException as e:
        raise FileNotFoundError(f"{e}, this function can only be used in DAP where the NSPL lookup exists")

    return spark.table(f'{db}.{latest_lookup.lower()}')


def rm_spaces(col: str) -> Column:
    """
    Remove any whitespace from a string.

    Parameters
    ----------
    col : str
    column name in the table

    Returns
    -------
    Column object with whitespaces removed
    """
    return F.regexp_replace(F.col(col), " ", "")
