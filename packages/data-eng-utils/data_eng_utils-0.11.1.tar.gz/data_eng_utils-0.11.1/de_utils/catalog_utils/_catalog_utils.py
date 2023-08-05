"""Data catalog utility functions."""
from typing import List, Dict, Optional

from pyspark.sql import (functions as F, SQLContext)

from de_utils.spark_utils._spark_utils import get_ss


def set_table_properties(database: str, table: str, **properties: str):
    """Set table properties on an existing hive table.

    Set any number arbitrary properties on a hive data frame. Arbitrary
    table properties are set using key argument name-value pairs.

    Note, property names are case sensitive.

    Certain property names will be not be set in the tblproperties,
    so will not be accessible to the get_table_properties function.
    For instance, a property called 'comment' will create a metadata
    item called 'Comment' that is used for the table description
    (see set_table_description).

    :param database: hive database name.
    :type database: str

    :param table: hive table name.
    :type table: str

    :keyword arguments: (str) arbitrary metadata properties to set on the
    hive table.
    """
    if len(properties) == 0:
        raise TypeError("set_table_properties: one or "
                        "more keyword arguments required")

    properties_string = ", ".join(
        [f"'{key}' = '{value}'"
         for key, value in properties.items()])

    get_ss().sql(f"ALTER TABLE {database}.{table} "
                 f"SET TBLPROPERTIES ({properties_string})")


def set_table_description(database: str, table: str, description: str):
    """Set the description of an existing hive table.

    The description will appear on the table info view in hive,
    or can be recovered using de_utils.spark_utils.describe_tables
    or de_utils.catalog_utils.get_table_description.

    :param database: hive database name.
    :type database: str

    :param table: hive table name.
    :type table: str

    :param description: description to add to the hive table.
    :type description: str
    """
    set_table_properties(database, table, comment=description)


def get_table_properties(database: str, table: str, *properties: str) -> Dict[str, str]:
    """Get table properties from an existing hive table.

    Properties are accessed through the spark sql command
    > SHOW TBLPROPERTIES
    Metatadata stored elsewhere will not be returned.

    An arbitrary number of specific properties can be obtained by
    passing property names as positional arguments. Only properties
    that exist for a given table are returned. If no properties
    are specified, the entire contents of TBLPROPERTIES is returned.
    If properties are specified but none exist in TBLPROPERTIES, an
    empty dictionary is retured.

    :param database: hive database name.
    :type database: str

    :param table: hive table name.
    :type table: str

    :positional arguments: (optional) arbitrary number of
    string property names to retrieve. If none are provided,
    all table properties are returned.

    :returns: table properties.
    :rtype: dict
    """
    table_properties = get_ss().sql(f"SHOW TBLPROPERTIES {database}.{table}")

    if len(properties) > 1:
        table_properties = table_properties.filter(
            F.col("key").isin(*properties))

    return dict(table_properties.collect())


def set_column_description(database: str, table: str, column: str, description: str):
    """Set a comment on a database table column.

    :param database: hive database name.
    :type database: str

    :param table: hive table name.
    :type table: str

    :param column: column name.
    :type column: str

    :param description: metadata text to record against the column.
    :type comment: str
    """
    data_type = describe_columns(database, table)[column]["type"]
    get_ss().sql(f"ALTER TABLE {database}.{table} CHANGE {column} "
                 f"{column} {data_type} COMMENT '{description}'")


def table_exists(table_path: str) -> bool:
    """Check if a table or view exists in a database.

    Parameters
    ----------
    table_path : str
        Path to table including database.

    Returns
    -------
    bool
        Flag for if the table exists in the database.

    Example
    -------
    >>> table_exists('database.table_name')
    """
    return get_ss().catalog._jcatalog.tableExists(table_path)


def list_tables(database: str) -> List[str]:
    """Return list of with names of all tables in specified database."""
    return SQLContext._instantiatedContext.tableNames(database)


def describe_tables(
    database: str,
    table: Optional[str] = None,
) -> Dict[str, Dict[str, str]]:
    """Return dictionary with table names and their metadata."""
    jc = get_ss().catalog._jcatalog

    def to_dict(t):
        return {
            'description': t.description(),
            'type': t.tableType(),
            'database': t.database()
        }
    if table:
        t = jc.getTable(database, table)
        return {t.name(): to_dict(t)}
    else:
        tables = jc.listTables(database).toLocalIterator()
        return {t.name(): to_dict(t) for t in tables}


def describe_columns(database: str, table: str) -> Dict[str, Dict[str, str]]:
    """Return dictionary with column names and metadata."""
    cols = get_ss().catalog._jcatalog.listColumns(database, table).toLocalIterator()
    return {
        c.name(): {
            'description': c.description(),
            'type': c.dataType(),
            'nullable': c.nullable(),
        }
        for c in cols
    }


def DDL_schema(database: str, table: str) -> str:
    """Return DDL formatted schema.

    This func and Hive don't handle NOT NULL constrains.
    """
    return get_ss().table(f'{database}.{table}')._jdf.schema().toDDL()


def print_DDL_schema(database: str, table: str):
    """Print formatted DDL schema for a table."""
    print(DDL_schema(database, table).replace(",", ",\n"))
