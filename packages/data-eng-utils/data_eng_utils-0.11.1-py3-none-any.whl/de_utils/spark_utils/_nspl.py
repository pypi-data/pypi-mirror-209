"""A collection of Spark util that only work inside DAP."""
# import pyspark libraries
from pyspark.sql.utils import AnalysisException
from pyspark.sql import (
    functions as F,
    DataFrame,
    Column,
)

# typing imports
from typing import Union, List

# local imports
from de_utils.spark_utils._spark_utils import get_ss, rm_spaces


def _get_latest_lookup() -> DataFrame:
    """
    Get the latest postcode lookup table name from national_statistics_postcode_lookup.

    Returns
    -------
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
        raise FileNotFoundError(f"{e}, ensure you're in DAP and not in DevTest")

    return spark.table(f'{db}.{latest_lookup.lower()}')


def with_postcode_map_nspl(
    df: DataFrame,
    pcd_col: str,
    nspl_cols: Union[str, Column, List[str], List[Column]],
) -> DataFrame:
    """Map NSPL lookup using a postcode column as the join key.

    Map the information contained in the nspl table onto a DataFrame. This also adds a
    region_names col to the NSPL lookup which contains all GB + isle of man region names
    to go with the 'rgn'/ region codes col.

    Parameters
    ----------
    df: DataFrame
        Spark DataFrame to add the information onto, must have col containing postcodes.

    pcd_col: str
        columns from NSPL mapper to map onto the provided dataset.

    nspl_cols: str or list of strings
        name of columns from NSPL columns (+ region_name) to map onto the data.

    Returns
    ------
    DataFrame:
        original DataFrame with selected NSPL mapped onto.
    """
    if isinstance(nspl_cols, str) or isinstance(nspl_cols, Column):
        nspl_cols = [nspl_cols]

    if 'region_name' in nspl_cols:
        nspl_cols.remove('region_name')
        nspl_cols.append(region_code_to_name('rgn'))

    # select what cols from NSPL to map
    mapper = _get_latest_lookup()
    mapper = mapper[[F.col('pcds').alias(pcd_col)] + nspl_cols]

    # clean and standardise postcode cols
    df = df.withColumn(pcd_col, F.upper(rm_spaces(pcd_col)))
    mapper = mapper.withColumn(pcd_col, F.upper(rm_spaces(pcd_col)))

    return df.join(F.broadcast(mapper), on=pcd_col, how='left')


def region_code_to_name(rgn_code: str) -> Column:
    """Add region_names col for GB + Isle of Man from a column with region codes (LAU1).

    Parameters
    ----------
    rgn_code : str
        Name of column with region codes

    Returns
    -------
    Column
    """
    return (
        F.when(F.col(rgn_code) == "E12000001", "North East (England)")
        .when(F.col(rgn_code) == "E12000002", "North West (England)")
        .when(F.col(rgn_code) == "E12000003", "Yorkshire and The Humber")
        .when(F.col(rgn_code) == "E12000004", "East Midlands (England)")
        .when(F.col(rgn_code) == "E12000005", "West Midlands (England)")
        .when(F.col(rgn_code) == "E12000006", "East of England")
        .when(F.col(rgn_code) == "E12000007", "London")
        .when(F.col(rgn_code) == "E12000008", "South East (England)")
        .when(F.col(rgn_code) == "E12000009", "South West (England)")
        .when(F.col(rgn_code) == "M99999999", "Isle of Man")
        .when(F.col(rgn_code) == "N99999999", "Northern Ireland")
        .when(F.col(rgn_code) == "S99999999", "Scotland")
        .when(F.col(rgn_code) == "W99999999", "Wales")
        .otherwise(None)
        .name('region_name')
    )


def map_pcd_to_regions(df: DataFrame, pcd_col: str):
    """Map region_code (NSPL `rgn` col) and region_name using a custom regions mapper.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame to add the information onto, must have col containing postcodes.

    pcd_col : str
        column name as a string of the column which contains postcodes.

    Returns
    -------
    DataFrame:
        original DataFrame with a region_code and region_name column added.
    """
    return (
        with_postcode_map_nspl(df, pcd_col, nspl_cols=['rgn', 'region_name'])
        .withColumnRenamed('rgn', 'region_code')
    )
