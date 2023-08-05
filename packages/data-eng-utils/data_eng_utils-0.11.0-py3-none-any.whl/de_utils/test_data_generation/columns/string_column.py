"""Column class for StringType values."""
import inspect
import re

from typing import Optional, Dict, Callable, Union

from de_utils._utils import enforce_type_hints
from de_utils.test_data_generation import common
from de_utils.test_data_generation.columns.base_columns import BaseColumn


class StringColumn(BaseColumn):
    """Column for generating string type values.

    Attributes
    ----------
    col_name : str
        name of the column
    size : int
        the maximum character length of the column
    size_mode : int, default=SIZE_TRUNCATE
        an indicator of how to handle generated values that exceed
        a given `size`. See StringColumn._conform_to_size().
    generation_method : str or Callable, optional
        an identifier to an existing generation method
        or a generation function
    """

    SIZE_TRUNCATE = 1
    SIZE_IGNORE = 2
    SIZE_ERROR = 3

    _default_size = 50

    context_mappings = {
        'country_code': common.random_country_code,
        'y_or_n': common.random_y_or_n,
        'postcode': common.random_postcode,
        'status': common.random_status,
        'gender_code': common.random_gender,
        'title': common.random_title,
        'email': common.random_email,
        'mobile_number': common.random_mobile_number,
        'bank_account_number': common.random_account_number,
        'bank_sort_code': common.random_sort_code,
    }

    def __init__(
        self,
        col_name: str,
        size: int = _default_size,
        size_mode: int = SIZE_TRUNCATE,
        generation_method: Optional[Union[str, Callable]] = None,
        **kwargs
    ):
        """Initialise StringColumn."""
        self.size = size
        self.generation_method = generation_method
        self.size_mode = size_mode

        super().__init__(col_name, **kwargs)

    @property
    def size(self) -> int:
        """Get _size."""
        return self._size

    @property
    def size_mode(self) -> int:
        """Get _size_mode."""
        return self._size_mode

    @property
    def generation_method(self) -> Callable:
        """Get _generation_method."""
        return self._generation_method

    @size.setter
    @enforce_type_hints(["size"])
    def size(self, size: int):
        if size >= 0:
            self._size = size
        else:
            raise ValueError(f"size should be a positive integer, got `{size}`.")

    @size_mode.setter
    @enforce_type_hints(["size_mode"])
    def size_mode(self, size_mode: int):
        if size_mode in range(1, 4):
            self._size_mode = size_mode
        else:
            raise ValueError("Size mode should be one of:"
                             f"`SIZE_TRUNCATE`={StringColumn.SIZE_TRUNCATE}, "
                             f"`SIZE_IGNORE`={StringColumn.SIZE_IGNORE} or "
                             f"`SIZE_ERROR`={StringColumn.SIZE_ERROR}.")

    @generation_method.setter
    def generation_method(self, generation_method: Union[str, Callable]):
        """Set a generation_method to a corresponding context or passed function."""
        if type(generation_method) is str:
            context = generation_method.strip().lower()

            if context in StringColumn.context_mappings:
                # Map context to a generation method
                self._generation_method = StringColumn.context_mappings[context]
            else:
                raise ValueError(
                    f"Invalid `generation_method`: `{context}`,"
                    f" generation_method must be one of: "
                    f"{list(StringColumn.context_mappings)}.")
        elif callable(generation_method):
            # Ensure passed function can be called without args
            if StringColumn._check_if_requires_args(generation_method):
                raise ValueError("Given `generation_method` requires arguments. "
                                 "Use `functools.partial` or your own lambda.")
            self._generation_method = generation_method
        else:
            self._generation_method = None

    def _conform_to_size(self, value: str) -> str:
        """Ensure a generated value conforms to set size mode.

        Availiable modes are:
            SIZE_TRUNCATE: if a generated string is larger than given
                size, truncate down to valid size.
            SIZE_IGNORE: allow for generated values to be larger than
                set size.
            SIZE_ERROR: throw a ValueError when a generated value is
                larger than set size.

        Parameters
        ----------
        value : str
            a generated value for this column

        Returns
        -------
        str
            a new string that conforms to size settings
        """
        if self._size_mode == StringColumn.SIZE_TRUNCATE:
            return value[:self._size]
        elif self._size_mode == StringColumn.SIZE_IGNORE:
            return value
        elif self._size_mode == StringColumn.SIZE_ERROR:
            if len(value) > self._size:
                raise ValueError(f"Generated values for {self.col_name}"
                                 f"are larger than size `{self._size}`.")
            else:
                return value
        else:
            raise ValueError("Invalid size mode.")

    @staticmethod
    def parse_length_regex(valid_regex: str) -> Optional[int]:
        """Parse a length restriction regex for its length values.

        Parameters
        ----------
        valid_regex : str
            a regular expression containing length restrictions

        Returns
        -------
        int or None
            the max value found in the regex restriction
        """
        pattern = r"\^\.\{(\d+)?,(\d+)?\}\$"
        match = re.match(pattern, valid_regex)

        if match:
            lengths = list(match.groups())
            cleaned = map(lambda x: int(x) if x else 0, lengths)

            return max(cleaned)

    @classmethod
    def from_json(
            cls,
            col_name: str,
            metadata: Dict,
            *args,
            **kwargs
    ) -> 'StringColumn':
        """Create a StringColumn from a de-utils schema.

        Parameters
        ----------
        col_name : str
            name of the column
        metadata : Dict
            a dictionary containing SchemaManager metadata
        args : list
            extra positional arguments
        kwargs: dict
            extra keyword arguments

        Returns
        -------
        StringColumn
            a newly created string column
        """
        valid_regex = metadata.get('valid_regex')
        if valid_regex:
            length = cls.parse_length_regex(valid_regex)

            if length:
                size = length
            else:
                size = cls._default_size
        else:
            size = cls._default_size

        values = metadata.get('valid_values')

        return cls(
            col_name=col_name,
            size=size,
            values=values if values else [],
            *args,
            **kwargs
        )

    @staticmethod
    def _check_if_requires_args(func: Callable) -> bool:
        """Check whether passed `func` requires any parameters upon calls.

        Using the function's signature, determines whether there are any
        positional only arguments, or any positional or keyword arguments
        that do not have a default value.

        Parameters
        ----------
        func : Callable
            function to be tested for required arguments

        Returns
        -------
        bool
            whether the given `func` has required arguments
        """
        sig = inspect.signature(func)

        def is_arg_required(p: inspect.Parameter):
            return p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD) \
                and p.default == p.empty

        return any(is_arg_required(p) for p in sig.parameters.values())

    @BaseColumn._repeat_until_distinct()
    def _generate_value(self) -> str:
        """Generate a string type row."""
        # If a generation_method is set, call it,
        # otherwise return arbitrary random characters
        if self.generation_method:
            value = self.generation_method()

            # Ensure that value conforms to size
            value = self._conform_to_size(value)
        else:
            value = common.random_chars(max_len=self._size)

        return value
