"""Column class for DoubleType values."""

from de_utils.test_data_generation.columns.base_columns import (
    BaseFloatDoubleColumn,
    BaseIntegerLongColumn
)


class DoubleColumn(BaseFloatDoubleColumn):
    """Column for generating double type values.

    Implements BaseFloatDoubleColumn.
    """

    def __init__(self, *args, **kwargs):
        """Initialise DoubleColumn."""
        super().__init__(*args, **kwargs)


class FloatColumn(BaseFloatDoubleColumn):
    """Column for generating float type values.

    Implements BaseFloatDoubleColumn.
    """

    def __init__(self, *args, **kwargs):
        """Initialise FloatColumn."""
        super().__init__(*args, **kwargs)


class IntegerColumn(BaseIntegerLongColumn):
    """Column for generating integer type values.

    Implements BaseFloatDoubleColumn.
    """

    def __init__(self, *args, **kwargs):
        """Initialise IntegerColumn."""
        print(f"args: {args} \n kwargs: {kwargs}")
        super().__init__(*args, **kwargs)


class LongColumn(BaseIntegerLongColumn):
    """Column for generating long type values.

    Implements BaseFloatDoubleColumn.
    """

    def __init__(self, *args, **kwargs):
        """Initialise LongColumn."""
        super().__init__(*args, **kwargs)
