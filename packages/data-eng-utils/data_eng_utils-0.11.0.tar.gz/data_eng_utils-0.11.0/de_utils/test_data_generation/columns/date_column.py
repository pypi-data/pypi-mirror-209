"""Column class for DateType values."""

import datetime

from de_utils.test_data_generation.columns.base_columns import BaseDateTimestampColumn


class DateColumn(BaseDateTimestampColumn):
    """Column for generating date type values.

    Implements BaseDateTimestampColumn.

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
            format: str = "%Y-%m-%d",
            min_year: int = 2010,
            max_year: int = datetime.datetime.now().year,
            **kwargs
    ):
        """Initialise DateColumn."""
        super().__init__(col_name, format, min_year, max_year, **kwargs)
