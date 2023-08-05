"""utility script for common test data generation functions."""
import csv
import datetime
import random
import string
from typing import List, Optional

from dateutil.relativedelta import relativedelta


def random_date(format="%Y%m%d%H%M%S", year=None, null_ind=0) -> Optional[str]:
    """Random date generator.

    If year is not specified then from year is 1960 and to year is 2020.

    Parameters
    ----------
    format : str, optional
        string format to convert the date, by default "%Y%m%d%H%M%S"
    year : _type_, optional
        year to generate a random date, by default None
    null_ind : int, optional
        bit 0 or 1, if 1 then None , by default 0

    Returns
    -------
    Optional[str]
        returns a random date for given year and format.
    """
    if null_ind:
        return None

    if year:
        from_year = to_year = year
    else:
        from_year, to_year = 1960, 2020

    start_date = datetime.date(from_year, 1, 1)
    end_date = datetime.date(to_year, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.strftime(format)


def add_years(start_date: str, years=0, format="%Y%m%d") -> str:
    """Add given years to the given date(in string format).

    Example:
        >> input date 20210101, years=2 and format is %Y%m%d then it returns 20230101

    Parameters
    ----------
    start_date : str
        input date to add years
    years : int, optional
        years to add in given date, by default 0
    format : str, optional
        date format to return the date, by default "%Y%m%d"

    Returns
    -------
    str
        a date in required string format.
    """    
    source_date = datetime.datetime.strptime(start_date, format)
    return (source_date + relativedelta(years=+years)).strftime(format)


def random_a_to_z(null_ind=0) -> Optional[str]:
    """"Return a char between A and Z or None if null_ind is 1(True).

    Parameters
    ----------
    null_ind : int, optional
        bit 0 or 1, by default 0

    Returns
    -------
    Optional[str]
        a char between A and Z or None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(string.ascii_uppercase)


def random_country_code(null_ind=0) -> Optional[str]:
    """Return random value from list of country codes.

    Parameters
    ----------
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    Optional[str]
        2 char country code or None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(
        ["GB", "FR", "US", "AU", "IN", "NZ", "DE", "DK", "IT", "IE", "IS"]
    )


def random_int(min_val: int, max_val: int, null_ind: int = 0) -> Optional[int]:
    """Return random int value, each conforming to the given min_val (inclusive) and max_val (exclusive).

    Parameters
    ----------
    min_val : int
        min int value
    max_val : int
        max int value
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    Optional[int]
        random value between min and max value, None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.randint(min_val, max_val)


def get_random_float(
    min_val: float, max_val: float, round_no: int, null_ind=0
) -> Optional[float]:
    """Return  a float value, each conforming to the given min_val (inclusive) and max_val (exclusive).

    Parameters
    ----------
    min_val : float
        min number
    max_val : float
        max number
    round_no : int
        rounded for given int value
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    Optional[float]
        random value between min and max value, None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return round(random.uniform(min_val, max_val), round_no)


def get_indicator(null_ind=0) -> int:
    """Return  0 or 1.

    Parameters
    ----------
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    int
        returns 0 or 1, None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.getrandbits(1)


def random_y_or_n(null_ind=0) -> Optional[str]:
    """"Return  Y or N or None.

    Parameters
    ----------
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    Optional[str]
        returns Y or N, None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(["Y", "N"])


def random_postcode(null_ind=0) -> Optional[str]:
    """Return  random postcode from the list of postcode values.

    Parameters
    ----------
    null_ind : int, optional
        bit 0 or 1, default to 0

    Returns
    -------
    Optional[str]
        None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(
        [
            "E1 8PX",
            "CM3 4PB",
            "IP22 2JY",
            "FK13 6JG",
            "CR0 7EG",
            "TS15 0HS",
            "CF23 5RF",
            "SK5 7EB",
            "FK5 4TW",
            "CO16 8HG",
            "LL70 9DJ",
            "CV7 8HX",
            "B18 7PW",
            "LE3 5FN",
            "CM14 5UF",
            "FY7 8HW",
            "SG8 9NE",
            "MK42 8TP",
            "SO45 5AH",
            "SL6 8DU",
            "EX39 4PD",
            "B65 9AD",
            "SR5 2ST",
            "DN7 6BT",
            "PE13 3DW",
            "FK1 3BL",
            "GU2 9XN",
            "RG24 7HS",
            "IP13 0GA",
            "SM2 5ES",
            "SW6 7BE",
            "BN14 0WA",
            "OL3 7NJ",
            "CB6 3HE",
            "NP26 3LY",
            "DE24 9FJ",
            "NR5 0AT",
            "E17 7AX",
            "CH42 1QG",
            "N7 7LB",
            "NE10 8NX",
            "CV11 6FE",
            "WF10 2GH",
            "BD2 3GD",
            "WF13 2JR",
            "SP4 7HL",
            "LU7 9FW",
            "L32 2DH",
            "YO23 2QG",
            "NG8 3FH",
        ]
    )


def random_chars(
    max_len: int, null_ind=0, special_char_ind=0, replace_spl_char=","
) -> Optional[str]:
    """Return  a random string, length of the given max_len int value.

    Parameters
    ----------
    max_len : int
        int value for maximum length of random string.
    null_ind : int, optional
        0 or 1, by default 0
    special_char_ind : int, optional
        flag to indicate if special chars included in the random string, by default 0
    replace_spl_char : str, optional
        special character to be replaced, by default ","

    Returns
    -------
    Optional[str]
        random set of chars or None null_ind is 1(True) 
    """    
    if null_ind:
        return None
    if special_char_ind:
        random_str = "".join(
            random.choices(
                string.printable + "\\n" + "\\r" + "இந்தியா",
                k=max_len,
            )
        )
        return random_str.replace(replace_spl_char, "!")

    return "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, max_len)))

def random_gender(null_ind=0) -> Optional[str]:
    """"Return  random F or M or None.

    Parameters
    ----------
    null_ind : int, optional
        0 or 1, by default 0

    Returns
    -------
    Optional[str]
        Returns F or M. None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(["F", "M"])


def random_title(null_ind=0) -> Optional[str]:
    """Return  random title from list of values.

    Parameters
    ----------
    null_ind : int, optional
        0 or 1, by default 0

    Returns
    -------
    Optional[str]
        initials like Mr, Mrs, Ms, Jr, Dr. None if null_ind is 1(True)
    """    
    if null_ind:
        return None

    return random.choice(["Mr", "Mrs", "Ms", "Jr", "Dr"])
