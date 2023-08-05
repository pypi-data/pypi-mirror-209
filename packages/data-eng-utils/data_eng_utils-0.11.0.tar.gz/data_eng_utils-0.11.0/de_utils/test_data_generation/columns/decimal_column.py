"""Column class for DecimalType values."""

import re

from typing import Tuple

from de_utils.test_data_generation import common
from de_utils.test_data_generation.columns.base_columns import BaseColumn, NumericMixin


class DecimalColumn(BaseColumn, NumericMixin):
    """Column for generating decimal type values.

    Attributes
    ----------
    col_name : str
        name of the column
    precision : int
        the maximum number of digits
    scale : int
        the number of digits after the decimal place
    """

    def __init__(self, col_name: str, precision: int = 10, scale: int = 0, **kwargs):
        """Initialise DecimalColumn."""
        self.precision = precision
        self.scale = scale

        super().__init__(col_name, **kwargs)

    @property
    def precision(self) -> int:
        """Get the maximum number of digits, in total."""
        return self._precision

    @property
    def scale(self) -> int:
        """Get the number of digits after the decimal place."""
        return self._scale

    @precision.setter
    def precision(self, precision: int):
        if 0 <= precision <= 38:
            self._precision = precision
        else:
            raise ValueError("`precision` should be a positive integer less "
                             "than or equal to 38.")

    @scale.setter
    def scale(self, scale: int):
        if (-self.precision + 1) <= scale <= self.precision:
            self._scale = scale
        else:
            raise ValueError("`scale` should be an integer less than "
                             f"or equal to `precision` ({self.precision}).")

    @staticmethod
    def parse_dtype(dtype: str) -> Tuple[int, int]:
        """Parse a DecimalType string containing the precision and scale values.

        Parameters
        ----------
        dtype : str
            a string representation of a decimal type from a schema

        Returns
        -------
        tuple(int, int)
            precision and scale from the given type
        """
        pattern = r"DecimalType\((\d+),(\d+)\)"

        match = re.match(pattern, dtype)

        # If two values are not matched, given type is invalid
        if match and len(match.groups()) == 2:
            precision, scale = map(lambda x: int(x) if x else 0, match.groups())
        else:
            raise ValueError(f"Given dtype is not valid: {dtype}.")

        return precision, scale

    @classmethod
    def from_dtype_string(
            cls,
            col_name: str,
            dtype: str,
            *args,
            **kwargs
    ) -> 'DecimalColumn':
        """Create a DecimalColumn object from its dtype (str).

        Parameters
        ----------
        col_name : str
            name of the column
        dtype : str
            a string representation of a decimal type from a schema
        args : list
            extra positional arguments
        kwargs: dict
            extra keyword arguments

        Returns
        -------
        DecimalColumn
            a newly created decimal column
        """
        precision, scale = cls.parse_dtype(dtype)

        return cls(
            col_name=col_name,
            precision=precision,
            scale=scale,
            *args,
            **kwargs
        )

    @BaseColumn._repeat_until_distinct()
    def _generate_value(self, negatives_enabled: bool = None) -> str:
        """Generate a Decimal type row.

        Parameters
        ----------
        negatives_enabled : bool
            whether the row should contain negative values

        Returns
        -------
        str
            a floating point number in a string representation
        """
        # Highest number supported is 10**(precision - scale)
        # e.g. Decimal(5,2) supports numbers up to 1000.00 (5 - 2 = 3 -> 10**3 = 1000)
        max_pow = self._precision - self._scale
        min_pow = max_pow - 1

        value = common.random_float(
            min_val=10 ** min_pow,
            max_val=10 ** max_pow - 1,
            round_no=self._scale
        )

        if negatives_enabled:
            value *= DecimalColumn.get_random_sign()

        # Suppress Python scientific float notation
        return f"{value:.{self._scale}f}"
