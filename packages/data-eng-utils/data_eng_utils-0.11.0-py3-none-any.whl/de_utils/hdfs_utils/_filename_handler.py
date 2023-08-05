import datetime
import re
from typing import List, Union, Callable

from de_utils.hdfs_utils._hdfs_utils import list_contents
from de_utils.lookups._lookups import get_datetime_regex

valid_tokens = (
    "file_datetime",
    "file_version",
    "path_datetime",
    "path_version")


def get_filename(path):
    """Get a file name from a file path."""
    return path.split("/")[-1]


def drop_filename(path):
    """Get a file path from a file name."""
    return "/".join(path.split("/")[:-1])


class FileMetadataHandler:
    """A collection of methods for file paths.

    A collection of methods for validating and sorting filepaths, and
    extracting version numbers and datetimes.
    """

    def __init__(
        self,
        filepath_pattern: str,
        file_dt_format: str = "%Y-%m-%d",
        path_dt_format: str = "%Y-%m-%d"
    ):
        """Initialise the FileMetadataHandler.

        Parameters
        ----------
        filepath_pattern : str
            The patten for identiying valid file paths. This can include
            tokens for file/path date-times and versions: {file_datetime},
            {path_datetime}, {file_version} and {path_version}.
        file_dt_format : str
            (1989) C standard date-time format for datetimes in file names.
        path_dt_format : str
            (1989) C standard date-time format for datetimes in paths outside
            of file names.
        """
        self.filepath_pattern = filepath_pattern
        self.file_dt_format = file_dt_format
        self.path_dt_format = path_dt_format

    def _get_regex(self, token=None):
        """Get a regex for extracting a valid token from a filepath."""
        regex_string = "^" + self.filepath_pattern + "$"
        if token is not None:
            if token not in valid_tokens:
                raise ValueError("Invalid token value.")
            token = "{" + token + "}"
            if token not in self.filepath_pattern:
                return None
            regex_string = regex_string.replace(token, f"({token})")

        try:
            file_dt_regex = get_datetime_regex(self.file_dt_format)
        except ValueError as err:
            raise ValueError("Invalid file_dt_format") from err

        try:
            path_dt_regex = get_datetime_regex(self.path_dt_format)
        except ValueError as err:
            raise ValueError("Invalid path_dt_format") from err

        return (
            regex_string
            .replace(".", "\\.")
            .replace("{file_version}", r"\d+")
            .replace("{path_version}", r"\d+")
            .replace("{file_datetime}", file_dt_regex)
            .replace("{path_datetime}", path_dt_regex))

    def _get_datetime(self, path, regex, dt_format):
        """Get a datetime from a file path."""
        if regex is None:
            return
        try:
            datetime_string = re.search(regex, path)[1]
        except TypeError as err:
            raise ValueError(f"invalid input path: {path}") from err
        return datetime.datetime.strptime(datetime_string, dt_format)

    def _get_version(self, path, regex):
        """Get a version number from a file path."""
        if regex is None:
            return
        try:
            version_string = re.search(regex, path)[1]
        except TypeError as err:
            raise ValueError(f"invalid input path: {path}") from err
        return int(version_string)

    def validate_path(self, path):
        """Validate a file path.

        Parameters
        ----------
        path : str
            Path to validate.

        Returns
        -------
        bool
            Flag for if the path is valid based on regex checks.
        """
        try:
            self.get_file_datetime(path)
            self.get_path_datetime(path)
        except ValueError:
            return False
        return re.match(self._get_regex(), path) is not None

    def get_file_datetime(self, path):
        """Get a file datetime from a path.

        Parameters
        ----------
        path : str
            Path to extract the file datetime from.

        Returns
        -------
        datetime.datetime
            File datetime extracted from the path.
        """
        return self._get_datetime(
            path,
            self._get_regex("file_datetime"),
            self.file_dt_format)

    def get_path_datetime(self, path):
        """Get a path datetime from a path.

        Parameters
        ----------
        path : str
            Path to extract the path datetime from.

        Returns
        -------
        datetime.datetime
            Path datetime extracted from the path.
        """
        return self._get_datetime(
            path,
            self._get_regex("path_datetime"),
            self.path_dt_format)

    def get_file_version(self, path):
        """Get a file version number from a path.

        Parameters
        ----------
        path : str
            Path to extract the file version from.

        Returns
        -------
        int
            The file version.
        """
        return self._get_version(path, self._get_regex("file_version"))

    def get_path_version(self, path):
        """Get a path version number from a path.

        Parameters
        ----------
        path : str
            Path to extract the path version from.

        Returns
        -------
        int
            The path version.
        """
        return self._get_version(path, self._get_regex("path_version"))

    def sort_by_file_datetime(self, paths):
        """Sort a list of files by their file datetimes.

        Parameters
        ----------
        paths : list[str]
            List of paths to sort.

        Returns
        -------
        list[str]
            The sorted list of paths.
        """
        return sorted(paths, key=lambda path: self.get_file_datetime(path))

    def sort_by_path_datetime(self, paths):
        """Sort a list of files by their path datetimes.

        Parameters
        ----------
        paths : list[str]
            List of paths to sort.

        Returns
        -------
        list[str]
            The sorted list of paths.
        """
        return sorted(paths, key=lambda path: self.get_path_datetime(path))

    def sort_by_file_version(self, paths):
        """Sort a list of files by their file version numbers.

        Parameters
        ----------
        paths : list[str]
            List of paths to sort.

        Returns
        -------
        list[str]
            The sorted list of paths.
        """
        return sorted(paths, key=lambda path: self.get_file_version(path))

    def sort_by_path_version(self, paths):
        """Sort a list of files by their path version numbers.

        Parameters
        ----------
        paths : list[str]
            List of paths to sort.

        Returns
        -------
        list[str]
            The sorted list of paths.
        """
        return sorted(paths, key=lambda path: self.get_path_version(path))

    def sort_paths(self, paths, sort_by):
        """Sort list of paths by tokens.

        Parameters
        ----------
        paths : list[str]
            List of paths to sort.
        sort_by : list[str]
            List of items to sort by (file_datetime, path_datetime,
            file_version and path_version).

        Returns
        -------
        list[str]
            The sorted list of paths.
        """
        if not all([item in valid_tokens for item in sort_by]):
            raise ValueError(
                "invalid item in sort_by, valid items are: {}".format(
                    ", ".join(item for item in valid_tokens)))
        method_lookup = {
            "file_datetime": self.sort_by_file_datetime,
            "path_datetime": self.sort_by_path_datetime,
            "file_version": self.sort_by_file_version,
            "path_version": self.sort_by_path_version}
        for sort_item in sort_by[::-1]:
            paths = method_lookup.get(sort_item)(paths)
        return paths

    @staticmethod
    def _group_list(lst: List, func: Callable) -> List[List]:
        """Group a list into a list of lists based on the result of a function.

        Each element of the list is passed to the function, and the list is sliced
        into sub-lists, where each sub-list shares the same function output.

        Parameters
        ----------
        lst : List
            List to sort.
        func : Callable
            Function that takes a single positional agrument that is used for
            slicing the list.

        Returns
        -------
        List[List]
            A list of lists, sliced based on the output of the function.

        Example
        -------
        In this example a lambda function is passed to group strings by their
        second character.
        >>> group_list(["red", "green", "yellow", "blue"], lambda x: x[1])
        [['red', 'yellow'], ['green'], ['blue']]
        """
        group = [func(item) for item in lst]
        return [
            [item for item, grp2 in zip(lst, group) if grp2 == grp]
            for grp in set(group)
        ]

    def filter_latest_path_version(self, paths):
        """Filter a list of paths to the latest versions.

        This filters based on the path version, keeping only
        the max path version for each unique file name.

        Parameters
        ----------
        paths : list[str]
            List of paths to filter.

        Returns
        -------
        list[str]
            Filtered list of paths.
        """
        return [
            path for group in FileMetadataHandler._group_list(paths, get_filename)
            for path in group
            if self.get_path_version(path) == max([
                self.get_path_version(path)
                for path in group])]


class FileNameHandler:
    """Tools for finding files on HDFS."""

    def __init__(
        self,
        filepath_pattern: str,
        file_dt_format: str = "%Y-%m-%d",
        path_dt_format: str = "%Y-%m-%d"
    ):
        """Initialise an instance of the FileNameHandler.

        Parameters
        ----------
        filepath_pattern : str
            The patten for identiying valid file paths. This can include
            tokens for file/path date-times and versions: {file_datetime},
            {path_datetime}, {file_version} and {path_version}.
        file_dt_format : str
            (1989) C standard date-time format for datetimes in file names.
        path_dt_format : str
            (1989) C standard date-time format for datetimes in paths outside
            of file names.

        Example
        -------
        If we have files in HDFS:
        /path/to/files/2022-01/v1/file_2022_01_01_v1.csv
        /path/to/files/2022-01/v1/file_2022_01_01_v2.csv
        /path/to/files/2022-01/v2/file_2022_01_01_v1.csv
        /path/to/files/2022-01/v1/file_2022_01_02_v1.csv
        /path/to/files/2022-02/v1/file_2022_02_01_v1.csv

        >>> file_handler = FileNameHandler(
                "/path/to/files/{path_datetime}/v{path_version}/"
                "file_{file_datetime}_v{file_version}.csv",
                path_dt_format="%Y-%m",
                file_dt_format="%Y_%m_%d")
        """
        self.filepath_pattern = filepath_pattern
        self.file_dt_format = file_dt_format
        self.path_dt_format = path_dt_format

    @property
    def filepath_pattern(self):
        """str: The file path pattern. Tokens are checked when this is set."""
        return self._filepath_pattern

    @filepath_pattern.setter
    def filepath_pattern(self, val):
        file_tokens = ["{file_datetime}", "{file_version}"]
        if any([token in drop_filename(val) for token in file_tokens]):
            raise ValueError(
                f"invalid filepath_pattern ({val}) "
                "- file tokens can only be in file name")
        path_tokens = ["{path_datetime}", "{path_version}"]
        if any([token in get_filename(val) for token in path_tokens]):
            raise ValueError(
                f"invalid filepath_pattern ({val}) - "
                "path tokens cannot be in file name")
        self._filepath_pattern = val

    @property
    def _metadata_handler(self):
        return FileMetadataHandler(
            self.filepath_pattern,
            self.file_dt_format,
            self.path_dt_format)

    def _get_root(self):
        """Get the path root in which to search for files.

        The root is the invariable part of the path before any
        datetime/version tokens.
        """
        return re.split(
            "|".join(["{" + token + "}" for token in valid_tokens]),
            self.filepath_pattern)[0]

    def _get_all_paths(self):
        """Get a list of all paths on the filepath root."""
        return list_contents(self._get_root(), recursive=True)

    def _get_valid_paths(self):
        """Get a list of valid filepaths."""
        return [
            path for path in self._get_all_paths()
            if self._metadata_handler.validate_path(path)]

    def get_filepaths(
        self,
        sort_by: Union[List[str], None] = None,
        latest_path_version: bool = False,
        reverse: bool = False
    ):
        """Get a list of file paths.

        Method to extract and optionally sort or filter (to the
        latest version) a list of valid file paths.

        Parameters
        ----------
        sort_by : list[str]
            Attributes on which to sort the file paths. File paths
            are sorted in the order that the arguments are provided.
            Valid attributes are: file_datetime, path_datetime,
            file_version and path_version.
        latest_path_version : bool
            If true, only the latest version of each unique file name
            (not path) will be included in the output, based on the
            version in the path. Note, this does not guarantee that
            each file name in the output is unique, as paths can
            still differ by the path date-time.
        reverse : bool
            Flag for if the sorted list should be reversed.

        Returns
        -------
        list[str]
            A list of file paths.

        Examples
        --------
        | If we have files in HDFS:
        | /path/to/files/2000-01/v1/file_2000_01_01_v1.csv
        | /path/to/files/2000-01/v1/file_2000_01_01_v99.csv
        | /path/to/files/2000-01/v5/file_2000_01_01_v1.csv
        | /path/to/files/2000-01/v5/file_2000_01_01_v99.csv
        | /path/to/files/2022-12/v1/file_2000_01_01_v1.csv
        | /path/to/files/2022-12/v1/file_2020_12_31_v1.csv
        | /path/to/files/2022-12/v1/file_2000_01_01_v99.csv
        | /path/to/files/2022-12/v4/file_2000_01_01_v1.csv
        | /path/to/files/2022-12/v4/file_2000_12_31_v1.csv
        | /path/to/files/2022-12/v3/file_2000_01_01_v99.csv


        >>> file_handler = FileNameHandler(
        ...     "/path/to/files/{path_datetime}/v{path_version}/"
        ...     "file_{file_datetime}_v{file_version}.csv",
        ...     path_dt_format="%Y-%m",
        ...     file_dt_format="%Y_%m_%d")

        >>> file_handler.get_filepaths()
        ['/path/to/files/2000-01/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v1/file_2020_12_31_v1.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v4/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_12_31_v1.csv',
         '/path/to/files/2022-12/v3/file_2000_01_01_v99.csv']

        >>> file_handler.get_filepaths(sort_by=['file_version'])
        ['/path/to/files/2000-01/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v1/file_2020_12_31_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_12_31_v1.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v3/file_2000_01_01_v99.csv']

        >>> file_handler.get_filepaths(sort_by=['file_version'], reverse=True)
        ['/path/to/files/2022-12/v3/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v4/file_2000_12_31_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v1/file_2020_12_31_v1.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v1.csv']

        >>> file_handler.get_filepaths(
        ...     sort_by=[file_datetime", "path_version",
        ...              "file_version", "path_datetime"],
        ...     reverse=True)
        ['/path/to/files/2022-12/v1/file_2020_12_31_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_12_31_v1.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_01_01_v1.csv',
         '/path/to/files/2022-12/v3/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v99.csv',
         '/path/to/files/2022-12/v1/file_2000_01_01_v1.csv',
         '/path/to/files/2000-01/v1/file_2000_01_01_v1.csv']


        >>> file_handler.get_filepaths(
        ...     sort_by=[file_datetime", "path_version",
        ...              "file_version", "path_datetime"],
        ...     reverse=True,
        ...     latest_path_version=True)
        ['/path/to/files/2022-12/v1/file_2020_12_31_v1.csv',
         '/path/to/files/2022-12/v4/file_2000_12_31_v1.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v99.csv',
         '/path/to/files/2000-01/v5/file_2000_01_01_v1.csv']
        """
        paths = self._get_valid_paths()
        if latest_path_version:
            paths = self._metadata_handler.filter_latest_path_version(paths)
        if sort_by is not None:
            paths = self._metadata_handler.sort_paths(paths, sort_by)
        if reverse:
            paths = paths[::-1]
        return paths
