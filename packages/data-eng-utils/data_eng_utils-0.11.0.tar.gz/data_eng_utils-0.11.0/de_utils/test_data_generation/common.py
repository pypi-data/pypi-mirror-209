"""Common test data generation functions."""

import datetime
import random
import string


def random_date(
        min_year=2010,
        max_year=datetime.datetime.now().year,
) -> datetime.datetime:
    """Random date generator.

    Parameters
    ----------
    min_year: int
        starting year, defaults to 2010
    max_year: int
        ending year, defaults to current year

    Returns
    -------
    str
        a random date between min_year and max_year
    """
    start_date = datetime.date(year=min_year, month=1, day=1)
    end_date = datetime.date(year=max_year, month=12, day=31)

    day_range = (end_date - start_date).days

    days_delta = random.randint(0, day_range)

    _random_date = (start_date + datetime.timedelta(days=days_delta))
    _random_time = datetime.time(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
        microsecond=random.randint(0, 999999)
    )

    return datetime.datetime.combine(_random_date, _random_time)


def random_a_to_z() -> str:
    """Return a char between A and Z.

    Returns
    ----------
    str
        a char between A and Z
    """
    return random.choice(string.ascii_uppercase)


def random_month_generator() -> int:
    """Return a random value between 1 and 12.

    Returns
    -------
    int
        value between 1 and 12
    """
    return random.randint(1, 12)


def random_country_code() -> str:
    """Return random value from list of country codes.

    Returns
    -------
    str
        2 char country code
    """
    return random.choice(
        ["GB", "FR", "US", "AU", "IN", "NZ", "DE", "DK", "IT", "IE", "IS"]
    )


def random_int(min_val: int, max_val: int) -> int:
    """Return random int value, between min_val (inclusive) and max_val (exclusive).

    Parameters
    ----------
    min_val : int
        min value
    max_val : int
        max value

    Returns
    -------
    int
        a random int value
    """
    return random.randint(min_val, max_val)


def random_float(min_val: float, max_val: float, round_no: int) -> float:
    """Return random float value, between min_val (inclusive) and max_val (exclusive).

     rounded to given int value.

    Parameters
    ----------
    min_val : float
        min number
    max_val : float
        max number
    round_no : int
        rounded for given int value

    Returns
    -------
    float
        a random float value

    """
    return round(random.uniform(min_val, max_val), round_no)


def random_y_or_n() -> str:
    """Return  Y or N or None.

    Returns
    ----------
    str
        returns Y or N
    """
    return random.choice(["Y", "N"])


def random_postcode() -> str:
    """Generate a postcode that adheres to the basic UK standard.

    Terminology of components found at:
    https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation

    Returns
    -------
    str
        a random postcode
    """
    postcode = ""

    # Outward code area (1 or 2 characters)
    for _ in range(random.randint(1, 2)):
        postcode += random.choice(string.ascii_uppercase)

    # Outward code district (1 or 2 digits)
    for _ in range(random.randint(1, 2)):
        postcode += str(random.choice(string.digits))

    # Seperator
    postcode += " "

    # Inward code sector (1 digit)
    postcode += str(random.choice(string.digits))

    # Inward code unit (2 characters)
    for _ in range(2):
        postcode += random.choice(string.ascii_uppercase)

    return postcode


def random_chars(max_len: int) -> str:
    """Return a random string, length of the given max_len int value.

    Parameters
    ----------
    max_len : int
        value for maximum length of random string

    Returns
    -------
    str
        a random string of length `max_len`
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=max_len))


def random_status() -> str:
    """Return random status from list of status values.

    Returns
    -------
    str
        a random status
    """
    return random.choice(
        ["closed", "inprogress", "pending", "active", "archived", "inactive"]
    )


def random_gender() -> str:
    """Return random F or M.

    Returns
    -------
    str
        F or M
    """
    return random.choice(["F", "M"])


def random_title() -> str:
    """Return random initials from list of values.

    Returns
    -------
    str
        initials like Mr, Mrs, Ms, Jr, Dr
    """
    return random.choice(["Mr", "Mrs", "Ms", "Jr", "Dr"])


def random_email() -> str:
    """Return a randomly generated email address.

    Returns
    -------
    str
        an email address
    """
    username = random_chars(max_len=15)

    domain = random.choice([
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "aol.com",
        "hotmail.co.uk",
        "icloud.com"
    ])

    return f"{username}@{domain}"


def random_mobile_number() -> str:
    """Return a randomly generated email address.

    Returns
    -------
    str
        a random mobile phone number
    """
    return "07" + "".join(
        random.choice(string.digits) for _ in range(9)
    )


def random_account_number() -> str:
    """Return a randomly generated bank account number.

    Returns
    -------
    str
        a random bank account number
    """
    return "".join(
        random.choice(string.digits) for _ in range(8)
    )


def random_sort_code() -> str:
    """Return a randomly generated bank sort code.

    Returns
    -------
    str
        a random bank sort code
    """
    parts = [
        "".join(random.choice(string.digits)
                for _ in range(2))
        for _ in range(3)]

    return "-".join(parts)
