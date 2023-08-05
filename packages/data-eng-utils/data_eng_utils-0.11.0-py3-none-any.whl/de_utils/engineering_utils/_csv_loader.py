"""Tool for handling end-to-end primary engineering pipelines."""

import logging
from pyspark.sql.types import StructField, StringType
from pyspark.sql.functions import input_file_name
from typing import Union, List

from de_utils._logging_utils import get_logger_name
from de_utils.engineering_utils._table_loader import TableLoader
from de_utils.spark_utils._spark_utils import get_ss


class CsvLoader(TableLoader):
    """Tools for building engineering pipelines for csv inputs.

    A class used to construct ETL pipelines for csv files,
    including compressed csv files compatible with the built-in
    spark.read.csv method, held on HDFS.

    The input data schema should contain fields for each column
    in the data, containing sub-dictionaries with fields containing
    metadata for the individual column. See de_utils.engineering_tools.
    ColumnMetadata for details of available fields.

    The class instance can be called directly to run a default
    pipeline. Customised pipelines can be run by calling individual methods
    directly.

    Note, this class relies on dictionaries being ordered,
    so is only compatible with CPython 3.6+ or Python 3.7+.

    Attributes
    ----------
    cols : tuple(str)
        Tuple of column names in the schema
    data_df : spark.sql.dataframe.DataFrame
        Dataframe containing only non-error data.
    df : spark.sql.dataframe.DataFrame
        Dataframe containing all data, note, if this is accessed before
        the data have been read , it will attempt to run the read_file
        method with no key-word arguments.
    error_df : spark.sql.dataframe.DataFrame
        Dataframe containing data flagged as errors.
    metadata :
        Input data schema with default values for missing elements.
    source_file : str
        Value of source_file input.
    target database : str
        Name of the target database.
    target_table : str
        Name of the target table.

    Example
    -------
    >>> schema = SchemaManager.read_schema("/path/to/my/schema.json")
    >>> loader = CsvLoader(
            schema=schema,
            source_file="/hdfs/path/to/my/data.csv",
            target_table = "target_database.target_table")
    >>> loader(
            header=True, dateFormat="dd/MM/yyyy",
            timestampFormat="yyyy-MM-dd hh:mm:ss",
            enforceSchema=True)

    Note, most keyword arguments passed to the loader call are passed
    to spark.read.csv. The only exception is the keyword argument,
    salt, which expects a string and is used when hashing data.

    Once the pipeline instance has been called, the data and error
    dataframes can simply be read from the target database or accessed
    through the CsvLoader instance (note, this may trigger re-evaluation
    if data are not cached or persisted):

    >>> loader.data_df
    >>> loader.error_df

    If a pipeline needs to be run in a non-standard order, methods
    can be called individually in the desired order rather than
    calling the CsvLoader instance directly. Most methods can
    effectively be turned off by using default values in the
    schema.
    """

    def __init__(
        self,
        schema: dict,
        source_file: Union[str, List[str]],
        *args, **kwargs
    ):
        """Initialise an instance of CsvLoader.

        The input schema dict should contain an item for each column
        in the data, containing sub-dictionaries with fields containing
        metadata for the individual column. See de_utils.engineering_tools.
        ColumnMetadata for details of available fields.

        Parameters
        ----------
        schema : dict
            The data schema dictionary for the table being processed.
        source_file : str, list(str)
            String, or list of strings, for input path(s).
        target_db : str, optional
            The name of the target database.
        target_table : str, optional
            The name of the target table.

        Notes
        -----
        For backwards compatability, the behaviour of positional arguments differs
        based on the number of such arguments.

        If three positional arguments are passed, the third is interpreted as
        target_table.

        If four positional arguments are passed, the third and fourth are interpreted
        as target_db and target_table, respectively.

        Examples
        --------
        CsvLoader can be initialised just the schema and source file.
        >>> loader = CsvLoader(
        ...     schema={'col1': {'dtype': DateType()},
        ...             'col2': {'dtype': IntegerType()}},
        ...     source_file='/path/to/the/source/file')

        CsvLoader can be initialised with a target_table using positional arguments
        >>> loader = CsvLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db.target_table')

        Or with keyword arguments
        >>> loader = CsvLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_table = 'target_db.target_table')

        CsvLoader can be initialised with separate target_db and target_table
        positional arguments
        >>> loader = CsvLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db',
        ...     'target_table')

        Or with keyword arguments
        >>> loader = CsvLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_db = 'target_db',
        ...     target_table = 'target_table')
        """
        super().__init__(schema, source_file, *args, **kwargs)
        self.logger = logging.getLogger(get_logger_name(__name__, "CsvLoader"))

    def read_file(self, **kwargs):
        """Read the csv file using the data schema.

        An additional column, _corrupt_record, is created to
        store string values of any corrupt records in the data.

        A further column, _input_file_name, is created containing the
        filepath for each record.

        Once run, a spark dataframe can be accessed through self.df.

        This method accepts key-word arguments compatable with the
        built in spark.read.csv method, other than path and schema,
        which are built from values passed when CsvLoader is initialised.

        Parameters
        ----------
        **kwargs
            Keyword arguments passed to the built-in spark.read.csv
            method.

        Example
        -------
        >>> schema = SchemaManager.read_schema("/path/to/my/schema.json")
        >>> loader = CsvLoader(
                schema=schema,
                source_file="/hdfs/path/to/my/data.csv",
                target_table = "target_database.target_table")
        >>> loader.read_file(
                header=True, dateFormat="dd/MM/yyyy",
                timestampFormat="yyyy-MM-dd hh:mm:ss",
                enforceSchema=True)
        """
        self.logger.info(f"reading file {self.source_file}")
        schema = self._get_schema()
        schema.add(StructField("_corrupt_record", StringType(), True))
        self._df = (
            get_ss()
            .read.csv(
                self.source_file,
                schema=schema,
                **kwargs)
            .withColumn("_input_file_name", input_file_name())
            .cache())
