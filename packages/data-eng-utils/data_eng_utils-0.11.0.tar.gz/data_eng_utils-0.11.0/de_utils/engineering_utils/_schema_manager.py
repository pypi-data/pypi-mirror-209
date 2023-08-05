"""Create, save and read schema in json format."""
# python imports
import os
import json
import logging
from copy import deepcopy
from collections import Counter

# third party imports
from pyspark.sql.types import (BinaryType, BooleanType, ByteType,
                               DateType, DecimalType, DoubleType, FloatType,
                               IntegerType, LongType, NullType,
                               ShortType, StringType, TimestampType)

# local imports
from de_utils.engineering_utils._table_loader import ColumnMetadata
from de_utils._logging_utils import get_logger_name

logger = logging.getLogger(get_logger_name(name=__name__))


def _dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate column names."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate column name: %r" % (k,))
        else:
            d[k] = v
    return d


class SchemaManager:
    """A class used to create and read schema.

    Create, save and read data schemas in a python dict.
    This class creates a template of a dataframe schema
    with defaults, which can be modified as required.
    Specific data types can be applied for specified columns.

    Example:
    Make a schema with columns 'a', 'b', 'c'. Column 'b' is IntegerType,
    column 'c' is DateType

    sm = SchemaManager()
    sm.all_cols = ["a", "b", "c"]
    sm.integer_type_cols = ["b"]
    sm.date_type_cols = ["c"]
    sm.save_schema("filepath")

    {'a': {'distinct': False,
           'dtype': 'StringType',
           'ignore': False,
           'lower': False,
           'nullable': True,
           'regex_replace': None,
           'upper': False,
           'valid_regex': None,
           'valid_values': None,
           'snapshot_raw': False},
     'b': {'distinct': False,
           'dtype': 'IntegerType',
           'ignore': False,
           'lower': False,
           'nullable': True,
           'regex_replace': None,
           'upper': False,
           'valid_regex': None,
           'valid_values': None,
           'snapshot_raw': False},
     'c': {'distinct': False,
           'dtype': 'DateType',
           'ignore': False,
           'lower': False,
           'nullable': True,
           'regex_replace': None,
           'upper': False,
           'valid_regex': None,
           'valid_values': None,
           'snapshot_raw': False}
    }

    Each filed in the data is represented by its own property.
    The property name is the data field name, the property
    value contains options for data read (see ColumnMetadata)

    Attributes
    ----------
    :param schema: Schema of the data with apropriate
                   pyspark.sql.types as values for dtype.
                   e.g:
                   {"distinct": False,
                    "dtype": StringType,
                    "ignore": False,
                    "lower": False,
                    "nullable": True,
                    "upper": False,
                    "valid_regex": None,
                    "valid_values": None,
                    "snapshot_raw": False}
    :type schema:  dict
    :param binary_type_cols: List of column names in the data
                             which are of
                             pyspark.sql.types.BinaryType
    :type binary_type_cols:  list
    :param boolean_type_cols: List of column names in the data
                              which are
                              pyspark.sql.types.BooleanType
    :type boolean_type_cols: list
    :param byte_type_cols: List of column names in the data
                           which are pyspark.sql.types.ByteType
    :type byte_type_cols: list
    :param date_type_cols: List of column names in the data
                           which are pyspark.sql.types.DateType
    :type date_type_cols: list
    :param decimal_type_cols: List of column names in the data
                              which are
                              pyspark.sql.types.DecimalType
    :type decimal_type_cols: list
    :param double_type_cols: List of column names in the data
                             which are pyspark.sql.types.DoubleType
    :type double_type_cols: list
    :param float_type_cols: List of column names in the data
                            which are pyspark.sql.types.FloatType
    :type float_type_cols: list
    :param integer_type_cols: List of column names in the data
                              which are
                              pyspark.sql.types.IntegerType
    :type integer_type_cols: list
    :param long_type_cols: List of column names in the data
                           which are pyspark.sql.types.LongType
    :type long_type_cols: list
    :param null_type_cols: List of column names in the data
                           which are pyspark.sql.types.NullType
    :type null_type_cols: list
    :param short_type_cols: List of column names in the data
                            which are pyspark.sql.types.ShortType
    :type short_type_cols: list
    :param string_type_cols: List of column names in the data
                             which are pyspark.sql.types.StringType
    :type string_type_cols: list
    :param timestamp_type_cols: List of column names in the data
                                which are
                                pyspark.sql.types.TimestampType
    :type timestamp_type_cols: list
    :param path: path to a file to read
    :type path: string

    Methods
    -------
    SchemaManager().read_schema(path):
        Read a already created data schema from file at path.
        Sets schema_data property.
    SchemaManager().save_schema_template(path="",
                                         pretty=True,
                                         force=False):
        Saves schema_template to file in path
    """

    def __init__(self):
        """Initialise the schema manager."""
        self._schema = {}

    _default_item = {k: v for (k, v) in ColumnMetadata("").schema.items()}
    _valid_dtypes = (
        BinaryType,
        BooleanType,
        ByteType,
        DateType,
        DecimalType,
        DoubleType,
        FloatType,
        IntegerType,
        LongType,
        NullType,
        ShortType,
        StringType,
        TimestampType)

    @property
    def schema(self):
        """Get the engineering pipeline schema."""
        return self._schema

    @property
    def printable_schema(self):
        """Get a printable version of the schema.

        Data types are replaced with string representations.
        """
        schema = deepcopy(self.schema)
        for key in schema.keys():
            schema[key]["dtype"] = str(schema[key]["dtype"])
        return schema

    def add_col(self, col_name, **kwargs):
        """Add a column to the schema.

        Parameters
        ----------
        col : str
            Name of the column to add to the schema.
        **kwwargs
            Optional key word arguments corresponding to schema values.

        Example
        -------
        >>> sm = SchemaManager()
        >>> sm.add_col(
            "col1", dtype=IntegerType(), nullable=False)
        """
        if not isinstance(col_name, str):
            raise TypeError("column name must be a string")
        if col_name in self._schema.keys():
            raise ValueError(f"column {col_name} already exists")
        self._schema[col_name] = self._upd_col_schema(
            self._default_item.copy(),
            **kwargs)

    def del_col(self, col_name):
        """Delete a column from the schema.

        Parameters
        ----------
        col_name : str
            Name of the column to delete.
        """
        self._schema.pop(col_name)

    def upd_col(self, col_name, **kwargs):
        """Update a column already in the schema.

        Parameters
        ----------
        col : str
            Name of the column to update..
        **kwwargs
            Optional key word arguments corresponding to schema values.

        Example
        -------
        >>> sm = SchemaManager()
        >>> sm.all_cols = ["col1"]
        >>> sm.upd_col(
            "col1", dtype=IntegerType(), nullable=False)
        """
        if col_name not in self.all_cols:
            raise ValueError(f"column {col_name} not in schema")
        self._schema[col_name] = self._upd_col_schema(
            self._schema[col_name],
            **kwargs)

    def add_cols(self, *cols, **kwargs):
        """Add one or more columns in a schema.

        Parameters
        ----------
        *cols : str
            Names of columns to add to the schema.
        **kwwargs
            Optional key word arguments corresponding to schema values.

        Example
        -------
        >>> sm = SchemaManager()
        >>> sm.add_cols(
            "col1", "col2", "col3",
            dtype=IntegerType(),
            nullable=False)
        """
        if not cols:
            raise AttributeError("no cols specified")
        duplicate_cols = [
            col for col in cols if col in self.all_cols]
        if duplicate_cols:
            raise ValueError(
                "cannot add columns that already exist: {}".format(
                    ", ".join(duplicate_cols)))
        for col in cols:
            self.add_col(col, **kwargs)

    def del_cols(self, *cols):
        """Delete one or more columns in a schema.

        Parameters
        ----------
        *cols : str
            Names of columns to delete from the schema.

        Example
        -------
        >>> sm = SchemaManager()
        >>> sm.all_cols = ["col1", "col2", "col3"]
        >>> sm.del_cols("col1", "col2")
        """
        if not cols:
            raise AttributeError("no cols specified")
        missing_cols = [col for col in cols if col not in self.all_cols]
        if missing_cols:
            raise ValueError(
                "cannot delete columns that are not in schema: {}".format(
                    ", ".join(missing_cols)))
        for col in cols:
            self.del_col(col)

    def upd_cols(self, *cols, **kwargs):
        """Update one or more columns in a schema.

        Parameters
        ----------
        *cols : str
            Names of columns to update
        **kwargs
            Optional key word arguments corresponding to schema values.

        Example
        -------
        >>> sm = SchemaManager()
        >>> sm.all_cols = ["col1", "col2", "col3"]
        >>> sm.upd_cols(
            "col1", "col2",
            dtype=IntegerType(),
            nullable=False)
        """
        if not cols:
            raise AttributeError("no cols specified")
        missing_cols = [col for col in cols if col not in self.all_cols]
        if missing_cols:
            raise ValueError(
                "cannot update columns that are not in schema: {}".format(
                    ", ".join(missing_cols)))
        for col in cols:
            self.upd_col(col, **kwargs)

    def _upd_col_schema(self, col_schema, **kwargs):
        if not all([key in col_schema.keys() for key in kwargs.keys()]):
            raise ValueError(
                f"Invalid kwarg. Acceptable kwargs are {col_schema.keys()}")
        if "dtype" in kwargs.keys():
            dtype = kwargs.pop("dtype")
            if not isinstance(dtype, self._valid_dtypes):
                raise ValueError(
                    "Invalid dtype. Valid types are instances of "
                    f"{self._valid_dtypes}.")
            col_schema["dtype"] = dtype
        for (kwarg, value) in kwargs.items():
            col_schema[kwarg] = value
        return col_schema

    def _set_dtype(self, col_list, dtype):
        if not isinstance(col_list, list):
            raise TypeError("List of columns expected.")
        if not all([col in self.all_cols for col in col_list]):
            raise ValueError(
                f"Invalid column name. Valid column names are {self.all_cols}."
            )
        self._assert_non_duplicates(*col_list)
        for col in col_list:
            if col not in self.string_type_cols:
                logger.warning(f"Changing dtype of {col}.")
            self.upd_col(col, dtype=dtype)

    @property
    def all_cols(self):
        """Get a list of all columns."""
        return list(self.schema.keys())

    @all_cols.setter
    def all_cols(self, col_names):
        if isinstance(col_names, str):
            col_names = [col_names]
        if len(set(col_names)) != len(col_names):
            raise ValueError("Duplicate column names.")
        for col_name in list(self.schema.keys()):
            if col_name not in col_names:
                self.del_col(col_name)
        for col_name in col_names:
            if col_name not in self.schema.keys():
                self.add_col(col_name)

    def _get_cols_of_type(self, dtype):
        return [
            key for (key, val) in self.schema.items()
            if isinstance(val["dtype"], dtype)]

    @property
    def binary_type_cols(self):
        """List of columns which are BinaryType."""
        return self._get_cols_of_type(BinaryType)

    @binary_type_cols.setter
    def binary_type_cols(self, col_list):
        self._set_dtype(col_list, BinaryType())

    @property
    def boolean_type_cols(self):
        """List of columns which are BooleanType."""
        return self._get_cols_of_type(BooleanType)

    @boolean_type_cols.setter
    def boolean_type_cols(self, col_list):
        self._set_dtype(col_list, BooleanType())

    @property
    def byte_type_cols(self):
        """List of columns which are ByteType."""
        return self._get_cols_of_type(ByteType)

    @byte_type_cols.setter
    def byte_type_cols(self, col_list):
        self._set_dtype(col_list, ByteType())

    @property
    def date_type_cols(self):
        """List of columns which are DateType."""
        return self._get_cols_of_type(DateType)

    @date_type_cols.setter
    def date_type_cols(self, col_list):
        self._set_dtype(col_list, DateType())

    @property
    def decimal_type_cols(self):
        """List of columns which are DecimalType."""
        return self._get_cols_of_type(DecimalType)

    @decimal_type_cols.setter
    def decimal_type_cols(self, decimal_cols):
        self._assert_non_duplicates(*[col[0] for col in decimal_cols])
        try:
            for (col, precision, scale) in decimal_cols:
                self._set_dtype(
                    [col],
                    DecimalType(int(precision), int(scale)))
        except (IndexError, TypeError, ValueError) as e:
            raise ValueError(
                "Expected list of lists, with the inner list containing "
                "the column name, precision and scale of a decimal column "
                "as integers."
            ) from e

    @property
    def double_type_cols(self):
        """List of columns which are DoubleType."""
        return self._get_cols_of_type(DoubleType)

    @double_type_cols.setter
    def double_type_cols(self, col_list):
        self._set_dtype(col_list, DoubleType())

    @property
    def float_type_cols(self):
        """List of columns which are FloatType."""
        return self._get_cols_of_type(FloatType)

    @float_type_cols.setter
    def float_type_cols(self, col_list):
        self._set_dtype(col_list, FloatType())

    @property
    def integer_type_cols(self):
        """List of columns which are IntegerType."""
        return self._get_cols_of_type(IntegerType)

    @integer_type_cols.setter
    def integer_type_cols(self, col_list):
        self._set_dtype(col_list, IntegerType())

    @property
    def long_type_cols(self):
        """List of columns which are LongType."""
        return self._get_cols_of_type(LongType)

    @long_type_cols.setter
    def long_type_cols(self, col_list):
        self._set_dtype(col_list, LongType())

    @property
    def null_type_cols(self):
        """List of columns which are NullType."""
        return self._get_cols_of_type(NullType)

    @null_type_cols.setter
    def null_type_cols(self, col_list):
        self._set_dtype(col_list, NullType())

    @property
    def short_type_cols(self):
        """List of columns which are ShortType."""
        return self._get_cols_of_type(ShortType)

    @short_type_cols.setter
    def short_type_cols(self, col_list):
        self._set_dtype(col_list, ShortType())

    @property
    def string_type_cols(self):
        """List of columns which are StringType."""
        return self._get_cols_of_type(StringType)

    @string_type_cols.setter
    def string_type_cols(self, col_list):
        self._set_dtype(col_list, StringType())

    @property
    def timestamp_type_cols(self):
        """List of columns which are TimestampType."""
        return self._get_cols_of_type(TimestampType)

    @timestamp_type_cols.setter
    def timestamp_type_cols(self, col_list):
        self._set_dtype(col_list, TimestampType())

    def _format_json(self, jsn):
        """Convert to pretty json.

        A method to format a given JSON (self.schema_data)
        to correct indentation and new line syntax

        """
        if jsn == "{}":
            raise ValueError("Cannot format empty schema. "
                             "Make schema first.")
        else:
            return json.dumps(jsn, indent=2)

    def _read_schema_as_string(self, schema_path):
        with open(schema_path, "r") as f:
            schema = f.read()
        if "\\" in schema.replace("\\\\", "¬#"):
            raise ValueError("Unescaped backslash '\\' "
                             "found in schema")
        return schema

    def _read_schema_as_dict(self, schema_path):
        """Read a schema JSON file."""
        schema_string = self._read_schema_as_string(schema_path)
        try:
            schema = json.loads(
                schema_string,
                object_pairs_hook=_dict_raise_on_duplicates)
            for col in schema.keys():
                for d_key in self._default_item.keys():
                    if d_key not in schema[col].keys():
                        if d_key == "dtype":
                            schema[col][d_key] = str(self._default_item[d_key])
                        else:
                            schema[col][d_key] = self._default_item[d_key]
                dtype = schema[col]["dtype"]
                if dtype[-1] != ")":
                    dtype += "()"
                schema[col]["dtype"] = eval(dtype)
            return schema

        except json.decoder.JSONDecodeError:
            if (int(Counter(schema_string)["{"])
                    != int(Counter(schema_string)["}"])):
                raise json.decoder.JSONDecodeError(
                    f"Number of opening braces ({{ "
                    f"{Counter(schema_string)['{']}) "
                    f"and closing braces (}} "
                    f"{Counter(schema_string)['}']})"
                    f"does not match. Check block around",
                    pos=self._find_missing_bracket(schema_string),
                    doc=schema_string)
            raise json.decoder.JSONDecodeError(
                "Something went wrong when reading schema, "
                + "check structure from",
                doc=schema_string,
                pos=0)

    def _find_missing_bracket(self, schema_string):
        def _most_keys(*args):
            assert all(isinstance(x, dict) for x in args)
            key_count = 0
            for i in args:
                if (len(i) < key_count) | (key_count == 0):
                    key_count = len(i)
                    d = i
            return d

        def _largest_key(d):
            return max(d.keys()), d[max(d.keys())]

        def _get_index(line, col):
            string_until_error = "\n".join(
                schema_string.split("\n")[:line])
            return len(string_until_error) + col

        open_bracket = {}
        close_bracket = {}

        for i in enumerate(schema_string.split("\n")):
            if "{" in i[1]:
                open_bracket[i[0]] = i[1].index("{")
            if "}" in i[1]:
                close_bracket[i[0]] = i[1].index("}")

        lc = _largest_key(_most_keys(open_bracket, close_bracket))
        return _get_index(lc[0], lc[1])

    def _assert_all_string(self, *args):
        if all(isinstance(x, str) for x in args):
            pass
        else:
            raise TypeError("All args must be of type string")

    def _assert_non_duplicates(self, *args):
        if sorted(args) == sorted(list(set(args))):
            pass
        else:
            raise ValueError(
                "Duplicates found. "
                + f"{[k for k in Counter(args) if Counter(args)[k] > 1]} "
                + "duplicated")

    @staticmethod
    def _type_check(var, tp):
        if tp not in [str, int, float, complex, list, tuple, range,
                      dict, set, frozenset, bool, bytes,
                      bytearray, memoryview]:
            raise TypeError(f"{tp} is not a valid data type")
        if not isinstance(var, tp):
            raise TypeError(f"var is of type {type(var)}, expected {tp}")

    def read_schema(self, path):
        """Read schema from JSON file specified in path.

        Reads a schema from path in json format and
        Sets a schema to attribute self.schema_data

        :param path: path to a file to read
        :type path: string
        """
        if os.path.isfile(path):
            self._schema = self._read_schema_as_dict(path)
        else:
            raise FileNotFoundError(f"{path}, not found")

    def save_schema(
        self,
        path="",
        pretty=True,
        force=False
    ):
        """Save column schema.

        A method to save a schema to file.

        :param path: location to save schema
        :type path: str
        :param pretty: indicate if JSON should be formatted,
                       default isTrue.
        :type pretty: Boolean
        :param force: Overwrites file if file exists in path
                      default is False.
        :type force: Boolean
        :returns: file in location path
        :rtype: file
        """
        if pretty:
            save_json = self._format_json(self.printable_schema)
        else:
            save_json = self.printable_schema

        if force or (os.path.exists(path) is False):
            with open(path, "w") as f:
                f.write(save_json)
        else:
            raise FileExistsError("File already exists, "
                                  "to overwrite set force=True")

    def save_schema_template(self, *args, **kwargs):
        """Save column schema.

        Alternative call for save_schema for backward compatibility.
        """
        self.save_schema(*args, **kwargs)
