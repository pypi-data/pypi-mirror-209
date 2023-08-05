"""Base column classes for shared functionality between Columns."""
import random

from functools import wraps
from itertools import cycle
from string import (
    ascii_letters as letters,
    digits
)
from typing import Any, Iterable, Union

from de_utils.test_data_generation import common


class BaseColumn:
    """
    Base class for a table column.

    Each Column subclass implements __generate() which creates a
    generated random value on each call.

    Attributes
    ----------
    col_name : str
        name of the column
    distinct : bool
        flag for whether the column's values should be unique
    nullable : bool
        flag for whether the column's values can be null
    values : Iterable
        a collection of values to emit instead of generated values
    """

    def __init__(
            self,
            col_name: str,
            distinct: bool = False,
            nullable: bool = True,
            values: Iterable[Any] = [],
            track_generated_values: bool = True
    ):
        """Initialise the Column object."""
        self.col_name = col_name
        self.distinct = distinct
        self.nullable = nullable

        self._values_iter = cycle(values) if values else None

        if track_generated_values:
            self._generated_values = []

    @property
    def col_name(self):
        """Get _col_name."""
        return self._col_name

    @property
    def distinct(self):
        """Get _distinct."""
        return self._distinct

    @property
    def generated_values(self):
        """Get _generated_values."""
        try:
            return self._generated_values
        except AttributeError:
            return None

    @property
    def values(self):
        """Get _values_iter."""
        return self._values_iter

    @col_name.setter
    def col_name(self, col_name: str):
        """Ensure that a column name can only contain alphanumeric chars (and `_`)."""
        if all(c in letters + digits + '_' for c in col_name):
            self._col_name = col_name
        else:
            raise ValueError("col_name must only contain letters,"
                             " digits, or underscores.")

    @distinct.setter
    def distinct(self, distinct: bool):
        if distinct:
            self._generated_values = []

        self._distinct = distinct

    @values.setter
    def values(self, values: Iterable):
        self._values_iter = cycle(values)

    def _store_value(self, value):
        """Save a value to a list of already produced values.

        Used in order to track a distinct condition per column.

        Parameters
        ----------
        value : Any
            an already used value to be recorded
        """
        self._generated_values.append(value)

    def _disable_distinct(self):
        self.distinct = False

    def _generate(self, *args, **kwargs):
        # Handle null indicator
        if kwargs.pop('null_ind', None) and self.nullable:
            return ""

        # Skip generation and return a preset value
        if self._values_iter:
            try:
                return next(self._values_iter)
            except StopIteration:
                return next(self._values_iter)

        try:
            value = self._generate_value(*args, **kwargs)

            if getattr(self, "_generated_values") is not None:
                self._store_value(value)

            return value
        except AttributeError:
            raise NotImplementedError(
                "Each Column class must implement a _generate_value() method."
            )

    @staticmethod
    def _repeat_until_distinct(attempts: int = 2):
        """Repeats a generation function until distinct or for N attempts.

        A decorator that allows for repetition of column _generate() methods
        until either a distinct value is found, or the maximum number of
        `attempts` is met.

        Parameters
        ----------
        attempts : int
            the number of times to attempt to generate a unique value

        Returns
        -------
        decorator
        """
        def decorator(func):
            @wraps(func)
            def inner(*args, **kwargs):
                self = args[0]

                if self.distinct:
                    for _ in range(attempts):
                        value = func(*args, **kwargs)

                        if value in self._generated_values:
                            continue
                        else:
                            self._store_value(value)
                            return value
                else:
                    return func(*args, **kwargs)
            return inner
        return decorator


class BaseDateTimestampColumn(BaseColumn):
    """
    Base class for Date and Timestamp columns.

    These columns share the same functionality with the only difference
    being the default datetime formats they use.

    Attributes
    ----------
    col_name : str
        name of the column
    format : str
        datetime format for values to be formatted as
    min_year : int
        the lower year bound for generated dates
    max_year : int
        the upper year bound for generated dates
    """

    def __init__(
            self,
            col_name: str,
            format: str,
            min_year: int,
            max_year: int,
            **kwargs
    ):
        """Initialise BaseDateTimestampColumn."""
        self._format = format
        self._min_year = min_year
        self._max_year = max_year

        super().__init__(col_name, **kwargs)

    @property
    def format(self):
        """Get _format."""
        return self._format

    @property
    def min_year(self):
        """Get _min_year."""
        return self._min_year

    @property
    def max_year(self):
        """Get _max_year."""
        return self._max_year

    @format.setter
    def format(self, format: str):
        self._format = format

    @min_year.setter
    def min_year(self, min_year: int):
        if min_year > 0:
            self._min_year = min_year
        else:
            raise ValueError("`min_year` must be a positive integer.")

    @max_year.setter
    def max_year(self, max_year: int):
        if max_year > 0:
            self._max_year = max_year
        else:
            raise ValueError("`max_year` must be a positive integer.")

    @BaseColumn._repeat_until_distinct()
    def _generate_value(self) -> str:
        """Generate a Date or Timestamp row."""
        date = common.random_date(
            min_year=self._min_year,
            max_year=self._max_year
        )
        value = date.strftime(self._format)

        return value


class NumericMixin:
    """Mixin containing common functions for numberic Column classes."""

    @staticmethod
    def get_random_sign() -> int:
        """Generate either a -1 or +1 randomly."""
        return int((random.getrandbits(1) - 0.5) * 2)


class BaseNumericColumn(BaseColumn, NumericMixin):
    """Base class for numeric type columns."""

    def __init__(
        self,
        *args,
        min_value: Union[int, float] = 0,
        max_value: Union[int, float] = 10**6,
        **kwargs
    ):
        """Initialise a BaseNumericColumn.

        Parameters
        ----------
        args : list
            extra arguments to pass to BaseColumn
        min_value : int or float
            the smallest value this column will produce
        max_value : int or float
            the largest value this column will produce
        kwargs : dict
            extra keyword arguments to pass to BaseColumn
        """
        self.set_value_bounds(min_value, max_value)
        super().__init__(*args, **kwargs)

    @property
    def min_value(self):
        """Get the smallest value this column will produce."""
        return self._min_value

    @property
    def max_value(self):
        """Get the largest value this column will produce."""
        return self._max_value

    def set_value_bounds(
            self,
            min_value: Union[int, float],
            max_value: Union[int, float]
    ):
        """Validate the min/max values before setting.

        Parameters
        ----------
        min_value : int or float
            the smallest value this column will produce
        max_value : int or float
            the largest value this column will produce
        """
        if min_value <= max_value:
            self._min_value = min_value
            self._max_value = max_value
        else:
            raise ValueError("`min_value` should be less than or equal to `max_value`.")

    def _generate(self, *args, **kwargs):
        value = super()._generate(*args, **kwargs)

        if kwargs.pop("negatives_enabled", None):
            value *= BaseNumericColumn.get_random_sign()

        return value


class BaseFloatDoubleColumn(BaseNumericColumn):
    """Base class for FloatColumn and DoubleColumn."""

    def __init__(self, *args, round_no: int = 2, **kwargs):
        """Initialise BaseFloatDoubleColumn."""
        self.round_no = round_no
        super().__init__(*args, **kwargs)

    def _generate_value(self) -> str:
        return str(common.random_float(
            min_val=self._min_value,
            max_val=self._max_value,
            round_no=self.round_no
        ))


class BaseIntegerLongColumn(BaseNumericColumn):
    """Base class for IntegerColumn and LongColumn."""

    def __init__(self, *args, **kwargs):
        """Initialise BaseIntegerLongColumn."""
        super().__init__(*args, **kwargs)

    def _generate_value(self) -> str:
        return str(common.random_int(
            min_val=self._min_value,
            max_val=self._max_value,
        ))
