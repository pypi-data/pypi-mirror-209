import logging
from pyspark.sql import functions as F
from pyspark.sql.types import DateType, TimestampType
from typing import Union, Optional

from de_utils.engineering_utils._table_loader import (
    ColumnMetadata, TableLoader)
from de_utils._logging_utils import get_logger_name
from de_utils.spark_utils._spark_utils import get_ss
from de_utils._utils import enforce_type_hints


class FwfColumnMetadata(ColumnMetadata):
    """Class to hold metadata for individual columns in a fixed-width file.

    The class can be used to store and retrieve metadata for columns, and
    to costruct spark StructField objects for the column.

    Attributes
    ----------
    schema : dict
        Metadata dictionary.
    string_schema : str
        String representation of the schema dict.

    Methods
    -------
    get_schema_field
        Get a pyspark StructField object for the column.

    Example
    -------
    >>> col_metadata = FwfColumnMetadata(
                "col1",
                start=5,
                end=7,
                nullable=False)
    >>> col_metadata.start
    5
    >>> col_metadata.end
    7
    >>> col_metadata.nullable
    False
    >>> col_metadata.dtype
    StringType
    >>> col_metadata.get_schema_field()
    StructField(col1,StringType,false)
    """

    @enforce_type_hints(["start", "end"])
    def __init__(
        self,
        col_name: str,
        start: int,
        end: int,
        **kwargs
    ):
        """Initialise the FwfColumnMetadata class.

        In addition to named parameters, FwfColumnMetadata accepts
        all keyword arguments as for the ColumnMetadata class.

        Parameters
        ----------
        col_name : str
            Name of the column.
        start : int
            Start position of the column in the fixed width file
            (one-based indexing).
        end : int
            End position of the column in the fixed width file
            (one-based indexing).
        **kwargs
            Key word arguments passed to ColumnMetadata.

        Raises
        ------
        TypeError
            Raised on intialisation for invalid parameter types.
        ValueError
            Raised on initialisation for invalid, or invalid combinations
            of parameter values.

        Examples
        --------
        At a minimum, all named arguments must be provided.
        >>> col_metadata = FwfColumnMetadata(
                "col1",
                start=5,
                end=7)

        Additional arguments can be provided as per ColumnMetadata.
        >>> col_metadata = wfColumnMetadata(
                "col1",
                start=5,
                end=7,
                dtype=IntegerType(),
                nullable=False,
                valid_values=[2**i for i in range(100)])
        """
        super().__init__(col_name, **kwargs)
        if (start <= 0) | (end <= 0):
            raise ValueError("start and end keywords must be positive")
        elif end < start:
            raise ValueError("end keyword must be greater than or equal to start")
        self._metadata["start"] = start
        self._metadata["end"] = end

    @property
    def start(self):
        """Get start."""
        return self._metadata["start"]

    @property
    def end(self):
        """Get end."""
        return self._metadata["end"]


class FwfLoader(TableLoader):
    """Tools for building engineering pipelines for fixed width file inputs.

    A class used to construct ETL pipelines for fixed width files held on HDFS.

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
        Input data schema with default values for missing elements stored as
        FwfColumnMetadata objects.
    source_file : str, list(str)
        Value of source_file input.
    target database : str
        Name of the target database.
    target_table : str
        Name of the target table.

    Examples
    --------
    >>> schema = SchemaManager.read_schema("/path/to/my/schema.json")
    >>> loader = FwfLoader(
            schema=schema,
            source_file="/hdfs/path/to/my/data.fwf",
            target_table = "target_database.target_table")
    >>> loader(header=True, dateFormat="dd/MM/yyyy",
            timestampFormat="yyyy-MM-dd hh:mm:ss",
            enforceSchema=True)

    Once the pipeline instance has been called, the data and error
    dataframes can simply be read from the target database or accessed
    through the FwfLoader instance (note, this may trigger re-evaluation
    so should be avoided for large dataframes that are used multiple
    times):

    >>> loader.data_df
    >>> loader.error_df

    If a pipeline needs to be run in a non-standard order, methods
    can be called individually in the desired order rather than
    calling the FwfLoader instance directly. Most methods can
    effectively be turned off by using default values in the
    schema.
    """

    def __init__(
        self,
        schema: dict,
        source_file: Union[str, list],
        *args, **kwargs
    ):
        """Initialise an instance of FwfLoader.

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
        FwfLoader can be initialised just the schema and source file.
        >>> loader = FwfLoader(
        ...     schema={'col1': {'dtype': DateType()},
        ...             'col2': {'dtype': IntegerType()}},
        ...     source_file='/path/to/the/source/file')

        FwfLoader can be initialised with a target_table using positional arguments
        >>> loader = FwfLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db.target_table')

        Or with keyword arguments
        >>> loader = FwfLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_table = 'target_db.target_table')

        FwfLoader can be initialised with separate target_db and target_table
        positional arguments
        >>> loader = FwfLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db',
        ...     'target_table')

        Or with keyword arguments
        >>> loader = FwfLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_db = 'target_db',
        ...     target_table = 'target_table')
        """
        super().__init__(
            {
                key: {
                    k: v
                    for k, v in value.items()
                    if k not in ["start", "end"]}
                for key, value in schema.items()
            },
            source_file,
            *args,
            **kwargs)
        self._metadata = {
            col: FwfColumnMetadata(col, **schema[col])
            for col in self.cols}
        self.logger = logging.getLogger(get_logger_name(__name__, "FwfLoader"))

    def __call__(self, *args, **kwargs):
        """Run a complete engineering processing pipeline.

        Runs a basic engineering pipeline:
        - read the data
        - add columns containing the raw data (snapshot_raw in the schema)
        - flag any corrupt values
        - convert any values to upper or lower case (upper/lower)
        - carry out regular expression replacement (regex_replace)
        - flag any invalid values (valid_values)
        - flag any invalid regex patterns (valid_regex)
        - flag any invalid duplicate values (distinct
        - hash the data using a salt (hash_data)
        - add a column containing the name of the source file
        - load the data table
        - load the error table

        Two tables are created, a table containing only the good data,
        which is stored with the {target_table} name, and a table
        containing all erroneous and malformed data, including the
        additional quality flags, which is stored as
        {target_table}_errors.

        This method accepts key-word arguments header, dateFormat
        and timestampFormat, with functionality equivalent to
        the spark.read.csv method. It also accepts a keyword, salt,
        which is used to hash data.

        Parameters
        ----------
        *args
            All positional arguments are passed to the TableLoader call method.
        **kwargs
            All keyword arguments are passed to the TableLoader call method.
        """
        super().__call__(*args, **kwargs)

    @staticmethod
    def _drop_single_occurence(df, col_name, *value):
        """Drop a single occurence of a specific value/values.

        Parameters
        ----------
        df : pyspark.sql.dataframe.DataFrame
            Dataframe in which to drop values.
        col_name : str
            Name of data column in which to drop values.
        *value
            Value or values to drop first occurence of.

        Returns
        -------
        pyspark.sql.dataframe.DataFrame
            An updated dataframe with specified values dropped.
        """
        id_col = "fwf_loader_flag_first_occurence_temp_col"
        df = df.withColumn(id_col, F.monotonically_increasing_id())
        return df.join(
            df.filter(F.col(col_name).isin(*value))
            .dropDuplicates([col_name]),
            id_col,
            "leftanti").drop(id_col)

    @staticmethod
    def _drop_header(df):
        """Drop the first row from a single column string dataframe."""
        header_value = df.first()[0]
        return FwfLoader._drop_single_occurence(df, "value", header_value)

    @staticmethod
    def _convert_type(col, dtype, dateFormat=None, timestampFormat=None):
        """Convert the type of a pyspark column.

        Parameters
        ----------
        col : pyspark.sql.column.Column
            Column to convert.
        dtype : pyspark.sql.types.DataType
            Type to convert the column to.
        dateFormat : str (optional)
            Format for parsing date strings.
        timestampFormat : str (optional)
            Format for parsing timestamps.

        Returns
        -------
        pyspark.sql.column.Column
            The input column with data converted to the specified type.
        """
        if isinstance(dtype, DateType):
            return F.to_date(col, dateFormat)
        elif isinstance(dtype, TimestampType):
            return F.to_timestamp(col. timestampFormat)
        else:
            return col.cast(dtype)

    @staticmethod
    def _update_corrupt_record(data_col, corrupt_col, error_col,
                               dtype, nullable, **kwargs):
        """Update a _corrupt_record column for a specified data column.

        Parameters
        ----------
        data_col : pyspark.sql.column.Column
            Column containing the data to check.
        corrupt_col : pyspark.sql.column.Column
            The _corrupt_record column to update.
        error_col : pyspark.sql.column.Column
            Column containing values to put in the corrupt_col when there
            is an error.
        dtype : pyspark.sql.types.DataType
            The expected data type in the column
        nullable : bool
            Flag for if null values are allowed in the column.
        **kwargs
            Keyword arguments passed to FwfLoader._convert_type.

        Returns
        -------
        pyspark.sql.column.Column
            The updated corrupt record column.
        """
        return F.when(
            corrupt_col.isNotNull()
            | (
                (F.trim(data_col) != "")
                & FwfLoader._convert_type(
                    data_col, dtype, **kwargs
                ).isNull())
            | ((data_col == "") & ~F.lit(nullable)),
            error_col).otherwise(F.lit(None))

    def _split_cols(self, df, value_col="value",
                    **kwargs):
        """Split a single column as per the data schema.

        Split a single string column in a dataframe into
        individual data columns, as per the data schema.

        Adds a _corrupt_record column to the data, where
        data types cannot be correctly converted, or
        non-nullable fields are null. Note, empty
        strings are interpretted as null.

        Parameters
        ----------
        df : pyspark.sql.dataframe.DataFrame
            Dataframe containing the data.
        value_col : str
            Name of column containing fixed-width string.
        **kwargs
            Keyword arguments passed to FwfLoader._convert_type.

        Returns
        -------
        pyspark.sql.dataframe.DataFrame
            An updated dataframe with data and _corrupt_record columns.
        """
        # the text is put in a column called 'value'
        # rename this in case of conflicts with data
        temp_col = "fwf_loader_split_cols"
        df = df.withColumnRenamed(value_col, temp_col)
        df = df.withColumn("_corrupt_record", F.lit(None))

        cols = self.metadata.keys()
        metadata = zip(
            cols,
            [self.metadata[key].start for key in cols],
            [self.metadata[key].end for key in cols],
            [self.metadata[key].dtype for key in cols],
            [self.metadata[key].nullable for key in cols]
        )

        for col_name, start, end, dtype, nullable in metadata:
            new_col = F.substring(F.col(temp_col), start, 1 + end - start)
            df = df.withColumn(
                col_name,
                FwfLoader._convert_type(new_col, dtype, **kwargs))
            df = df.withColumn(
                "_corrupt_record",
                self._update_corrupt_record(
                    new_col, df["_corrupt_record"], df[temp_col],
                    dtype, nullable, **kwargs))
        return df.select(*cols, "_corrupt_record", "_input_file_name")

    def read_file(
        self,
        header: bool = False,
        dateFormat: Union[str, None] = None,
        timestampFormat: Union[str, None] = None
    ):
        """Read the fixed-width file using the data schema.

        An additional column, _corrupt_record, is created to
        store string values of any corrupt records in the data.

        A further column, _input_file_name, is created containing the
        filepath for each record.

        Once run, a spark dataframe can be accessed through self.df.

        This method accepts key-word arguments header, dateFormat and
        timstampFormat, with functionality equivalent to the
        spark.read.csv method.

        Parameters
        ----------
        header : bool
            Flag for if the file contains a 1-row header. This should be
            set to True if the first row of the source file does not contain
            data.
        dateFormat : str, None
            Format string for interpreting any DateType values.
        timestampFormat : str, None
            Format string for interpreting any TimestampType values.

        Example
        -------
        >>> loader = FwfLoader(
                {'col1': {'start': 1, 'end': 11},
                 'col2': {'start': 11, 'end': 30}},
                '/path/to/source/file')
        >>> loader.read_file(
                header=True,
                dateFormat="dd/MM/yyyy",
                tiestampFormat="yyyy-MM-dd hh:mm:ss")
        """
        df = (
            get_ss()
            .read.text(self.source_file)
            .withColumn("_input_file_name", F.input_file_name()))
        if header:
            df = FwfLoader._drop_header(df)
        self._df = self._split_cols(
            df, dateFormat=dateFormat, timestampFormat=timestampFormat)
