"""A framework for extracting data from excel files."""

import pandas as pd
import re
import string
from typing import Dict, List, Tuple


class ExcelMapper:
    """Framework for mapping values from excel files to pandas dataframes."""

    def __init__(
        self,
        path: str,
        engine: str = "openpyxl"
    ):
        """Initialise the ExcelMapper.

        Parameters
        ----------
        path : str
            The path to the excel file.
        engine : str
            Specify the engine to use to read the Excel file (e.g.,
            'openpyxl' (default), or 'xlrd').
        """
        self._excel_file = pd.ExcelFile(path, engine=engine)

    @property
    def sheets(self) -> List[str]:
        """Read only list of sheet names."""
        return self._excel_file.sheet_names

    def __getattr__(self, attr: str) -> pd.DataFrame:
        """Override the getattr method so sheets are attributes."""
        if attr in self.sheets:
            df = self._excel_file.parse(attr, header=None)
            setattr(self, attr, df)
            return df
        else:
            raise AttributeError(f"{type(self).__name__} has no attribute '{attr}'")

    @staticmethod
    def get_column_number(col_letters: str) -> int:
        """Convert an excel column letter into a 0-indexed integer."""
        letter_mapper = dict(zip(string.ascii_uppercase, range(1, 27)))
        return sum([
            letter_mapper[col_letters[::-1][i].upper()] * 26**i
            for i in range(len(col_letters))]) - 1

    @staticmethod
    def split_coords(coords: str) -> Tuple[str, int]:
        """Split excel coordinates (e.g., F24) into two elements."""
        regex = r"^([a-zA-Z]+|\*)([1-9]\d*|\*)$"
        match = re.match(regex, coords)
        if match:
            letter = match[1].upper() if match[1] != "*" else None
            number = int(match[2]) if match[2] != "*" else None
            return letter, number
        else:
            raise ValueError(f"invalid excel coordinate '{coords}'")

    @staticmethod
    def split_range(coords: str) -> Tuple[str, int, str, int]:
        """Split an excel range (e.g., A1:Z4) into four elements."""
        coord_list = coords.split(":")
        if len(coord_list) == 2:
            return (
                ExcelMapper.split_coords(coord_list[0])
                + ExcelMapper.split_coords(coord_list[1]))
        else:
            raise ValueError(f"invalid excel range '{coords}'")

    def get_values(self, sheet: str, *coords: str) -> List[List]:
        """Get values from one of more cells or ranges of cells.

        Parameters
        ----------
        sheet : str
            Name of the excel sheet to get values from.
        coords : str
            One or more excel coordinates or coordinate ranges.
            This can contain wildcards, e.g., 'A*', 'A5:A*', 'A*:A7',
            'C4:*4', or '*5:E5' to specify open ended ranges.

        Returns
        -------
        list
            List of values from the excel sheet.

        Examples
        --------
        To get a single value:
        >>> mapper = ExcelMapper(/path/to/my/file)
        ... mapper.get_values("sheet_1", "A1")
        [[1.4]]

        To get a single range:
        >>> mapper = ExcelMapper(/path/to/my/file)
        ... mapper.get_values("sheet_1", "A1:A4")
        [[1.4, 3.2, 3.1, 4.2]]

        To get a mix of single values and ranges:
        >>> mapper = ExcelMapper(/path/to/my/file)
        ... mapper.get_values("sheet_1", "A1", "A1:A4")
        [[1.4], [1.4, 3.2, 3.1, 4.2]]
        """
        df = getattr(self, sheet)
        output = []
        for cr in coords:
            cr = f"{cr}:{cr}" if ":" not in cr else cr
            (x0, y0, x1, y1) = self.split_range(cr)
            x0 = x0 if x0 is not None else string.ascii_uppercase[df.columns[0]]
            x1 = x1 if x1 is not None else string.ascii_uppercase[df.columns[-1]]
            y0 = y0 if y0 is not None else df.index[0] + 1
            y1 = y1 if y1 is not None else df.index[-1] + 1
            x0 = self.get_column_number(x0)
            x1 = self.get_column_number(x1)
            if (x0 == x1) & (y0 == y1):
                output += [[df.loc[y0 - 1, x0]]]
            elif x0 == x1:
                output += [list(df.iloc[y0 - 1: y1, x0])]
            elif y0 == y1:
                output += [list(df.iloc[y0 - 1, x0: x1 + 1])]
            else:
                output += [[list(df.iloc[y, x0: x1 + 1])
                           for y in range(y0 - 1, y1)]]
        return output

    def map_data(self, config: List[Dict[str, str]]) -> pd.DataFrame:
        """Map excel coordinates to a dataframe row.

        Parameters
        ----------
        config
            List of dictionaries corresponding to the data items. The
            dictionaries must contain key-value pairs for the sheet,
            coords and target. The 'coords' can contain wild cards,
            e.g., 'A*', 'A5:A*', 'A*:A7', 'C4:*4', or '*5:E5' to
            specify open ended ranges.

        Returns
        -------
        pd.DataFrame
            The requested data in a pandas dataframe.

        Examples
        --------
        A single row dataframe can be built by specifying single cells.
        >>> mapper = ExcelMapper(/path/to/my/file)
        ... mapper.map_data([
        ... {"sheet": "sheet1", "coords": "F5", "target": "variable_1"},
        ... {"sheet": "sheet2", "coords": "A6", "target": "variable_2"}
        ... ])
          variable_1 variable_2
        0        abc        def

        A multi row dataframe can be built by passing cell ranges.
        Note, ranges do not have to be in the same direction, but must be
        the same length.
        >>> mapper = ExcelMapper(/path/to/my/file)
        ... mapper.map_data([
        ... {"sheet": "sheet1", "coords": "F5:F7", "target": "variable_1"},
        ... {"sheet": "sheet2", "coords": "A6:C6", "target": "variable_2"}
        ... ])
          variable_1 variable_2
        0        1.0        2.0
        1        1.1        2.1
        2        1.2        2.2
        """
        required_sheets = set([item["sheet"] for item in config])
        data = {}
        for sheet in required_sheets:
            items = [item for item in config if item["sheet"] == sheet]
            keys = [item["target"] for item in items]
            values = self.get_values(sheet, *[item["coords"] for item in items])
            data = {**data, **dict(zip(keys, [val for val in values]))}
        return pd.DataFrame(data)[[item["target"] for item in config]]
