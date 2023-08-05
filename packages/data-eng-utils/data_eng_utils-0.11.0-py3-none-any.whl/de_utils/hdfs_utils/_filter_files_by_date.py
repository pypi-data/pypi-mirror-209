import re
from datetime import datetime
from typing import List

from de_utils.lookups import get_datetime_regex


def _extract_datetime(date_string: str,
                      result_number: int,
                      datetime_format: str) -> datetime:
    """Find date formats within string and convert to datetime object.

    Parameters
    ----------
    date_string : str
        String containing at least one date or datetime

    result_number : int
        In the case where there are multiple dates or datetimes in `date_string`, which
        occurence of the date should be extracted (in order of occurence in the string).
        First occurence is 0.

    datetime_format : str
        format of the datetime in the file path to be extracted, the formatting
        follows that of the datetime module.

    Returns
    -------
    result_as_datetime : datetime
        datetime object of the specified occurence of datetime in `date_string`
    """
    # dynamically create regex based on date_format passed
    date_regex = get_datetime_regex(datetime_format)

    # find dates in the file path matching the created regex
    dates_list = re.findall(date_regex, date_string, re.IGNORECASE)

    result = dates_list[result_number]
    result_as_datetime = datetime.strptime(result, datetime_format)

    return result_as_datetime


def filter_files_by_datetime(files_list: List[str],
                             before: datetime = datetime(3000, 12, 31),
                             after: datetime = datetime(1900, 1, 1),
                             include_bounds: bool = True,
                             dt_format: str = "%Y%m%d",
                             res_num: int = 0) -> List[str]:
    """
    Filter files, before, after or between specified dates by date in the file.

    All date formats in the files/file paths must match to be able to filter
    the files successfully.

    Parameters
    ----------
    files_list : list
      list of files containing at least one date to be filtered by

    before : datetime, default = datetime(3000,12,31)
        filter for files on or before if `include_bounds = True` and before if
        `include_bounds = False`

    after : datetime, default = datetime(1900,1,1)
        filter for files on or after if `include_bounds = True` and after if
        `include_bounds = False`

    include_bounds: bool, default = True
        whether to have a soft boundry including the before and after dates or hard
        boundry which excludes those dates when filtering

    dt_format : str, default = '%Y%m%d'
      format of the date in the file path to be extracted, do NOT include optional
      separator characters such as -, these are accounted for already within the
      function. The formatting follows that of the datetime module. Refer to the
      documentation
      (https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
      for format codes. Only those refering to the year, month, day or week
      are valid for this function.

    res_num : int, default = 0
      in searching for dates in the file path, multiple may be found, specify the
      index of the date which is to be used as the date in which to filter the
      files, must be the same for all files in files_list


    Returns
    -------
    List
        list of files filtered by the specified dates

    """
    if before < after:
        raise ValueError(f"""before ({before}) should be on or after
        after ({after})""")

    # filter the files for only those that match the specified date range
    if include_bounds:
        filtered_list = list(
            filter(
                lambda file: (
                    after <= _extract_datetime(file, res_num, dt_format) <= before
                ), files_list
            )
        )

    else:
        filtered_list = list(
            filter(
                lambda file: (
                    after < _extract_datetime(file, res_num, dt_format) < before
                ), files_list
            )
        )

    return filtered_list
