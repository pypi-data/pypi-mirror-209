"""Tool for handling end-to-end primary engineering pipelines."""

import logging
from pyspark import StorageLevel
from pyspark.sql import functions as F
from pyspark.sql.types import (
    DataType, StringType, StructField, StructType, TimestampType)
from typing import Union, Optional

from de_utils._logging_utils import get_logger_name
from de_utils.spark_utils._column_utils import (
    flag_invalid_regex, flag_invalid_values, guid, sha256_hash)
from de_utils._utils import enforce_type_hints


def _type_check(val, val_type, message):
    if not isinstance(val, val_type):
        raise TypeError(message)


def _attribute_check(val, val_type, message):
    if not isinstance(val, val_type):
        raise AttributeError(message)


class ColumnMetadata:
    """Class contaning metadata for individual columns in a table.

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
    >>> col_metadata = ColumnMetadata(
                "col1",
                nullable=False,
                dtype=DateType())
    >>> col_metadata.nullable
    False
    >>> col_metadata.dtype
    DateType
    >>> col_metadata.get_schema_field()
    StructField(col1,DateType,false)
    """

    @enforce_type_hints([
        "dtype", "nullable", "snapshot_raw", "upper", "lower",
        "distinct", "hash_data", "ignore"])
    def __init__(
        self,
        col_name: str,
        dtype: DataType = StringType(),
        nullable: bool = True,
        snapshot_raw: bool = False,
        upper: bool = False,
        lower: bool = False,
        regex_replace: Optional[dict] = None,
        valid_values: Optional[Union[list, set, tuple]] = None,
        valid_regex: Optional[str] = None,
        distinct: bool = False,
        hash_data: bool = False,
        ignore: bool = False
    ):
        """Initialise an instance of ColumnMetadata.

        Initialise an instance of ColumnMetadata with various optional parameters
        for how the column should be processed in an engineering pipeline.

        Parameters
        ----------
        col_name : str
            Name of the column represented by the instance.
        dtype : DataType
            An instance of a pyspark data type that should be used when
            reading the column.
        nullable : bool
            A boolean flag for if the column can contain null values
            (default True).
        snapshot_raw : bool
            A flag for if a snapshot of the raw input should be included in
            the output dataframe (default False).
        upper : bool
            A flag for if strings should be converted to upper case. This can
            only be used for string data type, and lower must not be set
            (default False).
        lower : bool
            A flag for if strings should be converted to lower case. This can
            only be used for string data type, and upper must not be set
            (default False).
        regex_replace : dict(str), None
            A dictionary of regular expressions (keys) and replacements
            (values) that are used to replace the data when there is a match,
            or None (default None).
        valid_values : list, set, tuple, None
            Any valid values that can appear in the column or None (default None).
        valid_regex : str, None
            A regex pattern that valid values must match or None (defualt None).
        distinct : bool
            A flag for if the column cannot contain duplicate values, e.g.,
            a primary key should not contain duplicates (default False).
        hash_data : bool
            Aflag for if the column should be hashed (default False).
        ignore : bool
            A flag that a column should be ignored (default False).

        Raises
        ------
        TypeError
            Raised on intialisation for invalid parameter types.
        ValueError
            Raised on initialisation for invalid, or invalid combinations
            of parameter values.

        Examples
        --------
        To set up a column with default parameters:
        >>> col = ColumnMetadata('column1')

        To set custom values for parameters, e.g, for a date type columns
        that cannot be null:
        >>> col = ColumnMetadata('dob', dtype=DateType(), nullable=False)

        """
        # test for imcompatible parameter combinations
        if ignore:
            if any([
                not isinstance(dtype, StringType), not nullable,
                snapshot_raw, upper, lower, regex_replace is not None,
                valid_values is not None, valid_regex is not None, distinct,
                hash_data
            ]):
                raise ValueError(
                    "ignore must be False if any other arguments, except "
                    "col_name, are set to non-default values"
                )
        if not isinstance(dtype, StringType):
            if any([
                upper, lower, regex_replace is not None, hash_data
            ]):
                raise ValueError(
                    "dtype must be StringType() if any of upper, lower, "
                    "regex_replace or hash_data are set to "
                    "non-default values"
                )
        if valid_values is not None and valid_regex is not None:
            raise ValueError(
                "valid_values and valid_regex cannot be set simultaneously"
            )
        if upper and lower:
            raise ValueError(
                "upper and lower cannot be set simultaneously"
            )

        # regex_replace must be a dictionary with string keys and values
        if regex_replace is not None:
            try:
                regex_replace = {
                    str(key): str(val) for key, val in regex_replace.items()
                }
            except AttributeError:
                raise TypeError(
                    f"-\"regex_replace\" should be type {type({})} "
                    f"but instead got {type(regex_replace)}"
                )
        if isinstance(valid_values, (list, set, tuple)):
            valid_values = tuple(valid_values)
        elif valid_values is not None:
            raise TypeError(
                f"-\"regex_replace\" should be type {type([])}, {type(())} "
                f"or {type(set())} but instead got {type(valid_values)}"
            )
        valid_regex = str(valid_regex) if valid_regex is not None else None
        self.__dict__.update({"col_name": str(col_name)})
        self.__dict__.update({
            "_metadata": {
                key: value
                for key, value in locals().items()
                if key not in ["self", "col_name", "kwargs"]}})

    def __repr__(self):
        return (
            f"ColumnMetadata('{self.col_name}', "
            + self.string_schema.replace(": ", "=").strip("{}")
            + ")"
        )

    def __str__(self):
        return f"ColumnMetadata('{self.col_name}')"

    def __getattr__(self, name):
        try:
            return self._metadata[name]
        except KeyError:
            raise AttributeError(
                f"{self.__class__.__name__} has no attribute {name}")

    def __setattr__(self, name, value):
        raise AttributeError(f"cannot set attribute {name}")

    def get_schema_field(self):
        """Create a pyspark schema struct field object.

        Returns
        -------
        pyspark.sql.types.StructField
            The schema structfield for the object.
        """
        return StructField(self.col_name, self.dtype, self.nullable)

    @property
    def schema(self):
        """Get a schema dictionary of the column."""
        schema = {}
        for attribute in self._metadata.keys():
            schema[attribute] = getattr(self, attribute)
        return schema

    @property
    def string_schema(self):
        """Get a string version of the column schema."""
        schema_strings = [
            f"{key}: {str(val)}" if key != "dtype"
            else f"{key}: {str(val)}()"
            for key, val in self.schema.items()
        ]
        return "{" + ", ".join(schema_strings) + "}"


class TableLoader:
    """Tools for building engineering pipelines.

    This is intended to be inherited into child classes for
    for building ETL pipelines with specific read methods.

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
    source_file : str, list(str)
        Value of source_file input.
    target database : str
        Name of the target database.
    target_table : str
        Name of the target table.

    raises
    ----------
    NotImplementedError
        If the read_file method is called. This class should be inherited
        and the read_file method overwritten for specific file-types.

    Notes
    -----
        This class relies on dictionaries being ordered,
        so is only compatible with CPython 3.6+ or Python 3.7+.
    """

    def __init__(
        self,
        schema: dict,
        source_file: Union[str, list],
        *args, **kwargs
    ):
        """Initialise  an instance of TableLoader.

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
        TableLoader can be initialised just the schema and source file.
        >>> loader = TableLoader(
        ...     schema={'col1': {'dtype': DateType()},
        ...             'col2': {'dtype': IntegerType()}},
        ...     source_file='/path/to/the/source/file')

        TableLoader can be initialised with a target_table using positional arguments
        >>> loader = TableLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db.target_table')

        Or with keyword arguments
        >>> loader = TableLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_table = 'target_db.target_table')

        TableLoader can be initialised with separate target_db and target_table
        positional arguments
        >>> loader = TableLoader(
        ...     {'col1': {'dtype': DateType()},
        ...      'col2': {'dtype': IntegerType()}},
        ...     '/path/to/the/source/file',
        ...     'target_db',
        ...     'target_table')

        Or with keyword arguments
        >>> loader = TableLoader(
        ...     schema = {'col1': {'dtype': DateType()},
        ...               'col2': {'dtype': IntegerType()}},
        ...     source_file = '/path/to/the/source/file',
        ...     target_db = 'target_db',
        ...     target_table = 'target_table')
        """
        self.logger = logging.getLogger(get_logger_name(__name__, "TableLoader"))
        _type_check(schema, dict, "schema must be dict type")
        _type_check(source_file, (str, list),
                    "source file must be string or list of strings")
        self._cols = tuple(schema.keys())
        self._metadata = {
            col: ColumnMetadata(col, **schema[col])
            for col in self.cols}
        self._source_file = source_file

        if len(args) > 2:
            raise TypeError(
                f"{self.__class__.__name__} "
                f"expected up to 4 arguments, got {2 + len(args)}")

        unexpected_kwargs = [
            kwarg for kwarg in kwargs.keys()
            if kwarg not in ["target_table", "target_db"]]
        if unexpected_kwargs != []:
            raise TypeError(
                f"{self.__class__.__name__} got {len(unexpected_kwargs)} unexpected "
                f"keyword argument(s) {', '.join(unexpected_kwargs)}"
            )

        args_dict = dict(zip(["target_table", "target_db"], args[::-1]))
        target_db = kwargs.get("target_db", args_dict.get("target_db", None))
        target_table = kwargs.get("target_table", args_dict.get("target_table", None))

        self.target_db = target_db
        self.target_table = target_table
        self._filter_cols = []

    def __call__(
        self,
        guid: bool = True,
        num_partitions: Optional[int] = None,
        persist: bool = False,
        persist_storage_level: StorageLevel = StorageLevel.MEMORY_AND_DISK,
        salt: str = "",
        source_col: bool = True,
        **kwargs
    ):
        """Run a complete engineering processing pipeline.

        Runs a basic engineering pipeline:
        - read the data
        - optionally repartition the data
        - add columns containing the raw data (snapshot_raw in the schema)
        - flag any corrupt values
        - convert any values to upper or lower case (upper/lower)
        - carry out regular expression replacement (regex_replace)
        - flag any invalid values (valid_values)
        - flag any invalid regex patterns (valid_regex)
        - flag any invalid duplicate values (distinct)
        - hash data using a salt (hash_data)
        - add a column containing the name of the source file
        - load the data table
        - load the error table

        Two tables are created, a table containing only the good data,
        which is stored with the {target_table} name, and a table
        containing all erroneous and malformed data, including the
        additional quality flags, which is stored as
        {target_table}_errors.

        More precise control over running orders of pipelines can be
        achieved by running the individual methods separately.

        This method accepts key-word arguments compatible with the
        built in spark.read.csv method as well as those specified
        below.

        Parameters
        ----------
        guid : bool
            If True, a guid is added to the dataframe (default True).
        num_partitions : int
            The target number of partitions to repartition data after read.
        persist : bool
            Flag to persist the dataframe at the end
            of processing. Note, if False, writing the data and error
            tables may trigger redundant evaluation (default False).
        persist_storage_level : StorageLevel
            Pyspark storage level at which to persist the dataframe
            (default StorageLevel(True, True, False, False, 1))
        salt : str
            A salt to use when hashing data. A single salt is used for all data
            that requires hashing.
        source_col : bool
            If True, a column containing the source file name is added to the
            dataframe (default True).
        **kwargs
            Key-word arguments to be passed to the read_file method.
        """
        self.read_file(**kwargs)
        if num_partitions is not None:
            self.repartition(numPartitions=num_partitions)
        self.add_raw_columns()
        self.flag_corrupt_values()
        self.convert_case()
        self.regex_replace()
        self.flag_invalid_values()
        self.flag_invalid_regex()
        self.flag_duplicates()
        self.hash_data(salt)
        if source_col:
            self.add_source_col()
        if guid:
            self.add_guid()
        if persist:
            self.persist(storageLevel=persist_storage_level)
        try:
            self.load_data_table()
            self.load_error_table()
        except ValueError:
            self.logger.warning("no data or error tables loaded")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        params = {
            key: val for key, val in
            {
                "schema": self._get_schema_text(),
                "source_file": self.source_file,
                "target_db": self.target_db,
                "target_table": self.target_table
            }.items()
            if val is not None}
        return (
            self.__class__.__name__
            + "("
            + ", ".join([f"{key}='{val}'" for key, val in params.items()])
            + ")")

    def _get_schema_text(self):
        schema_text = "{"
        for col, metadata in self.metadata.items():
            schema_text += (
                f"{col}: "
                "{"
                f"{metadata.string_schema}"
                "}")
        schema_text += "}"
        return schema_text

    @property
    def df(self):
        """Get the df attribute."""
        try:
            self._df
        except AttributeError:
            self.logger.warning(
                "source file has not been read - reading source file with "
                "default settings (use read_file method for customisable "
                "settings)")
            self.read_file()
        # Col order matches input schema, any additional columns derived by the
        #  framework appear in arbitrary order after these.
        col_order = list(self._metadata.keys())
        return self._df[
            col_order
            + [c for c in self._df.columns if c not in col_order]
        ]

    @property
    def cols(self):
        """Get the cols attribute."""
        return self._cols

    @property
    def source_file(self):
        """Get the source_file attribute."""
        return self._source_file

    @property
    def metadata(self):
        """Get the metadata attribute."""
        return self._metadata

    @property
    def target_db(self):
        """Get the target_db attribute."""
        return self._target_db

    @target_db.setter
    def target_db(self, val):
        """Set the target_db attribute."""
        val = str(val) if val is not None else None
        self._target_db = val

    @property
    def target_table(self):
        """Get the target_table attribute."""
        return self._target_table

    @target_table.setter
    def target_table(self, val):
        """Set the target_table attribute."""
        val = str(val) if val is not None else None
        self._target_table = val

    @property
    def data_df(self):
        """Get the filtered dataframe (no errors)."""
        return (
            self.df
            .filter(~self._get_error_filter())
            .drop(
                *self._get_ignored_cols(),
                *self._filter_cols,
                "_corrupt_record",
                "_input_file_name"))

    @property
    def error_df(self):
        """Get the filtered errors dataframe."""
        return (
            self.df
            .filter(self._get_error_filter())
            .drop(
                *self._get_ignored_cols(),
                "_input_file_name"))

    @classmethod
    def _date_to_time(cls, df):
        """Convert DateType to TimestampType.

        A method to convert all DateType columns in a spark dataframe
        into TimestampType columns. This is used when saving hive tables
        in parquet format, which is incompatible with DateType columns.

        Parameters
        ----------
        df : pyspark.sql.dataframe.DataFrame
            The dataframe to convert.

        Return
        ----------
        pyspark.sql.dataframe.DataFrame
            Tthe input dataframe with date columns converted to timestamps.
        """
        to_convert = (item[0] for item in df.dtypes if item[1] == "date")
        for col in to_convert:
            df = df.withColumn(col, F.col(col).cast(TimestampType()))
        return df

    @classmethod
    def _load_table(cls, df, target_table, **kwargs):
        """Load a dataframe to a table.

        Load a dataframe into a table in a specified hive
        database. Existing tables with the same name are overwritten.

        Parameters
        ----------
        df : pyspark.sql.dataframe.DataFrame
            The dataframe to load into a table.
        target_table : str
            The name of the target table.
        """
        df = cls._date_to_time(df)
        df.write.saveAsTable(target_table, **kwargs)

    def _get_schema(self):
        """Get a pyspark data schema.

        Return
        ----------
        pyspark.sql.types.StructType
            The data schema.
        """
        return StructType([self.metadata[col].get_schema_field()
                           for col in self.cols])

    def read_file(self, **kwargs):
        """Read the source file using the data schema.

        Raises
        ----------
        NotImplementedError
            This class should be inherited and this method overwritten
            with a method to read particular file types. The method
            should set self._df equal to the data in a pyspark
            dataframe, with two additional columns, _corrupt_values,
            containing non-null strings when data cannot be read
            with the specified schema, and _input_file_name.
        """
        raise NotImplementedError(
            "table_loader should be inherited not used directly")

    def add_raw_columns(self):
        """Add raw value colums to the dataframe.

        For each column where snapshot_raw is True, an additional
        column is created in the dataframe containing the value
        as it was read (i.e., post type enforcement and null checks
        as these are implemented on read in the read_file method).
        """
        raw_snapshot_cols = [
            col for col in self.cols
            if self.metadata[col].snapshot_raw is True]
        for col in raw_snapshot_cols:
            self.logger.info(f"adding snapshots of raw data for {col}")
            new_col = f"{col}_raw"
            if new_col in self.cols:
                raise ValueError(
                    f"cannot create raw snapshot column {new_col} "
                    f"as {new_col} already exists")
            self._df = self.df.withColumn(new_col, F.col(col))

    def flag_corrupt_values(self):
        """Create corrupt_record flag column.

        Create a boolean column, corrupt_record,
        to filter corrupt records in the data.
        """
        self.logger.info("flagging corrupt values")
        self._df = self.df.withColumn(
            "corrupt_record",
            F.when(F.col("_corrupt_record").isNotNull(),
                   F.lit(True))
            .otherwise(F.lit(False)))
        self._filter_cols += ["corrupt_record"]

    def flag_invalid_values(self):
        """Flag invalid values in the dataframe.

        Create a boolean column flagging invalid
        values for any column where valid_values were specified
        in the schema. New columns take the name of the data
        column appended with _invalid.
        """
        validation_cols = {
            col: self.metadata[col].valid_values
            for col in self.cols
            if self.metadata[col].valid_values is not None}
        for col in validation_cols.keys():
            self.logger.info(f"flagging invalid values in {col}")
            self._df = self.df.withColumn(
                f"{col}_invalid",
                flag_invalid_values(F.col(col), *validation_cols[col]))
            self._filter_cols += [f"{col}_invalid"]

    def flag_invalid_regex(self):
        """Flag invalid values using the valid regex check.

        Create a boolean column flagging invalid
        values for any column where values to not match specified
        regex in the schema. New columns take the name of the data
        column appended with _invalid_regex.
        """
        validation_cols = {
            col: self.metadata[col].valid_regex
            for col in self.cols
            if self.metadata[col].valid_regex is not None}
        for col in validation_cols.keys():
            self.logger.info(f"flagging invalid regex in {col}")
            self._df = self.df.withColumn(
                f"{col}_invalid_regex",
                flag_invalid_regex(F.col(col), validation_cols[col]))
            self._filter_cols += [f"{col}_invalid_regex"]

    def flag_duplicates(self):
        """Flag Duplicate values.

        Create a boolean column flagging duplicate
        values for any column that was specified as distinct: True
        in the schema. New columns take the name of the data column
        appended with _duplicates.
        """
        distinct_cols = (
            col for col in self.cols if self.metadata[col].distinct)
        for col in distinct_cols:
            self.logger.info(f"flagging duplicate values in {col}")
            duplicates = self.df.groupby(col).agg(
                (F.count("*") > 1)
                .alias(f"{col}_duplicates"))
            self._df = self.df.join(duplicates, col, "left")
            self._filter_cols += [f"{col}_duplicates"]

    def regex_replace(self):
        """Carry out regex replacements.

        Apply regex replacements in any columns with regex_replace dictionary.
        Columns are compared against the key and replaced by the corresponding
        value.
        """
        replace_cols = (
            col for col in self.cols
            if self.metadata[col].regex_replace is not None)
        for col in replace_cols:
            self.logger.info(f"carrying out regex replacement in {col}")
            replace_dict = self.metadata[col].regex_replace
            for regex, replace in replace_dict.items():
                self._df = self.df.withColumn(
                    col,
                    F.regexp_replace(
                        self.df[col], regex, replace))

    def convert_case(self):
        """Convert values to upper or lower case.

        Convert values in any column where upper or lower are set to True
        to upper or lowercase, respectively.
        """
        upper_cols = (col for col in self.cols if self.metadata[col].upper)
        for col in upper_cols:
            self.logger.info(f"converting {col} to upper case")
            self._df = self.df.withColumn(col, F.upper(F.col(col)))
        lower_cols = (col for col in self.cols if self.metadata[col].lower)
        for col in lower_cols:
            self.logger.info(f"converting {col} to lower case")
            self._df = self.df.withColumn(col, F.lower(F.col(col)))

    def hash_data(self, salt=""):
        """Hash data in the dataframe to obscure it, not for serious security.

        Hash the data in the specified columns using SHA256. Data
        to be hashed are prepended with an optional salt. Note,
        the same salt is used for every record in the data.

        Parameters
        ----------
        salt : str, pyspark.sql.column.Column, optional
            A salt to prepend to data (defaults to an empty string).
        """
        if not isinstance(salt, str):
            raise TypeError("salt must be a string")
        hash_cols = [
            col for col in self.metadata.keys()
            if self.metadata[col].hash_data]
        for col in hash_cols:
            self.logger.info(f"hashing data in {col}")
            self._df = self.df.withColumn(
                col, sha256_hash(self.df[col], salt))

    def add_source_col(self, name="source_file"):
        """Add a source file column to the dataframe.

        Add a column to the dataframe containing the
        file name, which is extracted from the file path.

        Parameters
        ----------
        name : str, optional
            Name of the new column (defaults to 'source_file').
        """
        self.logger.info("adding source column")
        if name in self.df.columns:
            raise ValueError(
                f"cannot insert column name '{name}' column already exists")
        self._df = self.df.withColumn(
            name,
            F.col("_input_file_name"))

    def add_guid(self, name="guid"):
        """Add a guid column to the dataframe.

        Parameters
        ----------
        name : str, optional
            Name of the new column (defaults to 'guid').
        """
        self.logger.info("adding guid column")
        if name in self.df.columns:
            raise ValueError(
                f"cannot insert column name '{name}' column already exists")
        self._df = self.df.withColumn(name, guid())

    def _get_error_filter(self):
        """Get a filter combining all error checks.

        Construct a Boolean column combining
        all data checks (corrupt values, invalid values and
        duplicated values). The returned column is True where
        invalid data were found and False elsewhere.

        Return
        --------
        pyspark.sql.column.Column
            a Boolean column for filtering all invalid values in the dataframe.
        """
        error_filter = F.lit(False)
        for col in self._filter_cols:
            error_filter = error_filter | F.col(col)
        return error_filter

    def _get_ignored_cols(self):
        """Get names of ignored columns.

        Produces a tuple of column names for which
        the ColumnMetadata.ignore field is set to True

        Return
        ------
        tuple(str)
            Names of columns to be ignored.
        """
        return (col for col in self.cols if self.metadata[col].ignore)

    def _check_target(self):
        """Raise a value error if the target table or database are None."""
        if self.target_table is None:
            raise ValueError("cannot load table when target_table is None")

    def load_error_table(self, **kwargs):
        """Load all flagged errors in the dataframe into the error table."""
        self._check_target()
        self.logger.info(
            f"loading error table {self.target_table}_errors")
        cnt = self.error_df.count()
        if cnt > 0:
            self.logger.warning(f"{cnt} records flagged as errors")
        else:
            self.logger.info("no records flagged as errors")
        target_table = ".".join(filter(None, (self.target_db, self.target_table)))
        TableLoader._load_table(self.error_df, f"{target_table}_errors", **kwargs)

    def load_data_table(self, **kwargs):
        """Load all good data in the dataframe into the target table."""
        self._check_target()
        self.logger.info(f"loading table {self.target_table}")
        self.logger.info(f"{self.data_df.count()} good records found")
        target_table = ".".join(filter(None, (self.target_db, self.target_table)))
        TableLoader._load_table(self.data_df, target_table, **kwargs)

    def sample_columns(self, n):
        """Get a sample of n random values from each dataframe column.

        Returns a n independently sampled non-null values from each
        data column in the dataframe.

        Parameters
        ----------
        n : int
            The number of random samples required.

        Return
        ------
        dict
            The random sample from the dataframe.
        """
        self.logger.info("sampling dataframe")
        samples = {}
        for col in self.data_df.columns:
            one_col_df = self.data_df.select(col).where(F.col(col).isNotNull())
            sample = [
                row[col] for row in one_col_df.rdd.takeSample(False, n)]
            samples[col] = sample
        return samples

    def repartition(self, *args, **kwargs):
        """Repartition the dataframe.

        Args and kwargs can be passed as per
        pyspark.sql.dataframe.DataFrame.repartition.

        Parameters
        ----------
        *args
            Positional arguments passed to the pyspark df.repartition method.
        **kwargs
            Key word aruments passed to the pyspark df.repartition method.
        """
        self.logger.info("repartitioning dataframe")
        self._df = self.df.repartition(*args, **kwargs)

    def coalesce(self, *args, **kwargs):
        """Coalesce the dataframe.

        Args and kwargs can be passed as per
        pyspark.sql.dataframe.DataFrame.coalesece.

        Parameters
        ----------
        *args
            Positional arguments passed to the pyspark df.coalesce method.
        **kwargs
            Key word aruments passed to the pyspark df.coalesce method.
        """
        self.logger.info("coalescing dataframe")
        self._df = self.df.coalesce(*args, **kwargs)

    def persist(self, *args, **kwargs):
        """Persist the dataframe.

        Args and kwargs can be passed as per
        pyspark.sql.dataframe.DataFrame.persist.

        Parameters
        ----------
        *args
            Positional arguments passed to the pyspark df.persist method.
        **kwargs
            Key word aruments passed to the pyspark df.persist method.
        """
        self.logger.info("persisting dataframe")
        self._df.persist(*args, **kwargs)
