import datetime
from itertools import chain

caps_exceptions = ("am", "pm", "gmt", "utc")


def _capitalize(s, exceptions=None):
    """Capitalize a string.

    Parameters
    ----------
    s : str
        String to capitalize.
    exceptions : list[str], None
        List of exceptions strings. If s appears in exceptions,
        the upper-case version is returned instead of the
        capitalized version.

    Returns
    -------
    str
        Capitalized string.

    """
    exceptions = [] if exceptions is None else exceptions
    exceptions = [excep.lower() for excep in exceptions]
    if (exceptions is not None) and (s.lower() in exceptions):
        return s.upper()
    else:
        return s.capitalize()


def _get_string_variations(strings, capitalize_exceptions=None):
    """Get a list of upper/lower/capitalised versions of a list of strings.

    Parameters
    ----------
    strings : list[str]
        List of string to return variations of.

    capitalize_exceptions : list[str], None
        If specified, list of strings that should not be capitalised. Only
        upper or lower case versions are returned.

    Returns
    -------
    list[str]
        Variations of the input strings.

    """
    return list(set(
        chain.from_iterable([
            (item.lower(), item.upper(),
             _capitalize(item, capitalize_exceptions))
            for item in strings])))


def _get_regex_or(strings, caps_variations=True, caps_exceptions=None):
    """Combine an iterable of strings into a non-capturing regex or group.

    Parameters
    ----------
    strings : list[str], tuple[str], set[str]
        Iterable of items to combine in the or statement.
    caps_variations : bool = True
        Flags for if different capitalization styles should be included in
        the or statement. If True, upper-case, lower-case and capitalized
        versions of each input are all included in the output. If False,
        only the exact inputs are used.
    caps_exceptions : list[str], tuple[str], set[str], None
        Exception words that should not be capitalised. Only upper and
        lower case versions are returned for these words.

    Returns
    -------
    str
        Non-capturing regex combining inputs using or statements.

    Examples
    --------
    >>> _get_regex_or(["one", "two", "three"])
    '(?:Three|three|One|Two|TWO|THREE|two|one|ONE)'

    >>> _get_regex_or(["one", "Two", "tHREe"], False)
    '(?:one|Two|tHREe)'

    >>> _get_regex_or(["one", "two", "three"], caps_exceptions=["one"])
    '(?:Three|three|Two|TWO|THREE|two|one|ONE)'

    """
    return "(?:{})".format("|".join(
        _get_string_variations(strings, caps_exceptions)
        if caps_variations else strings))


pattern_lookup = {
    "%a": _get_regex_or(
        [datetime.date(1, 1, i).strftime('%a') for i in range(1, 8)],
        caps_exceptions=caps_exceptions),
    "%A": _get_regex_or(
        [datetime.date(1, 1, i).strftime('%A') for i in range(1, 8)],
        caps_exceptions=caps_exceptions),
    "%w": "[0-6]",
    "%d": r"(?:0[1-9]|[12]\d|3[01])",
    "%-d": "(?:[1-9]|[12][0-9]|3[01])",
    "%b": _get_regex_or(
        [datetime.date(1, i, 1).strftime('%b') for i in range(1, 13)],
        caps_exceptions=caps_exceptions),
    "%B": _get_regex_or(
        [datetime.date(1, i, 1).strftime('%B') for i in range(1, 13)],
        caps_exceptions=caps_exceptions),
    "%m": "(?:0[1-9]|1[012])",
    "%-m": "(?:[1-9]|1[012])",
    "%y": "[0-9]{2}",
    "%-y": "(?:[0-9]|[1-9][0-9])",
    "%Y": r"(?:\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3})",
    "%H": r"(?:[01]\d|2[0-3])",
    "%-H": "(?:[0-9]|1[0-9]|2[0-3])",
    "%I": "(?:0[1-9]|1[0-2])",
    "%-I": "(?:[1-9]|1[0-2])",
    "%p": _get_regex_or(["AM", "PM"], caps_exceptions=caps_exceptions),
    "%M": r"[0-5]\d",
    "%-M": "(?:[0-9]|[1-5][0-9])",
    "%S": r"[0-5]\d",
    "%-S": "(?:[0-9]|[1-5][0-9])",
    "%f": r"\d{6}",
    "%z": r"(?:[+-](?:0[1-9]|1[0-2])[0-5]\d(?:[0-5]\d)?(?:\.\d{6})?|)",
    "%Z": _get_regex_or(["UTC", "GMT"], caps_exceptions=caps_exceptions),
    "%j": r"(?:00[1-9]|0[1-9]\d|[12]\d{2}|3[0-5]\d|36[0-6])",
    "%-j": "(?:[0-9]|[1-9][0-9]|[12][0-9][0-9]|3[0-5][0-9]|36[0-6])",
    "%U": r"(?:[0-4]\d|5[0-3])",
    "%W": r"(?:[0-4]\d|5[0-3])",
    "%G": r"(?:\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3})",
    "%u": "[1-7]",
    "%V": r"(?:0[1-9]|[1-4]\d|5[0-3])",
    "%%": "%"}


def get_datetime_regex(datetime_format: str) -> str:
    """Construct regex from datetime format that follows datetime module string format.

    Parameters
    ----------
    datetime_format : str
        A datetime format containing datetime format codes.

    Returns
    -------
    str
        A string containing a regex corresponding to the input datetime format.

    Example
    -------
    >>> get_datetime_regex('%Y-%m-%d')

    Notes
    -----
    Currently only GMT and UTC timezones are supported for the %Z format code.
    Format codes %c, %x and %X are not currenylu supported.
    """
    if "%" not in datetime_format:
        raise ValueError("Ensure at least one date format character is passed")

    percent_count = datetime_format.count("%%")

    for code, replace in pattern_lookup.items():
        datetime_format = datetime_format.replace(code, replace)

    if datetime_format.count("%") != percent_count:
        raise ValueError("input contains an invalid datetime format code")

    return datetime_format


def get_nino_regex(nino_type):
    """Lookup for National Insurance numbers (NINOs).

    Provides regular expressions for different types of National Insurance numbers
    (NINOs) taking into account both upper and lower case cases. Rules for each NINO
    are described below.

    **valid_nino**

    | First two letters can't be D,F,I,Q,U or V
    | Second letter can't be O
    | Final letter can be A-D or empty string (issue with no suffix in 2013)

    | Match: ["JP371820A", "JP371820", "JP371820A", "jp371820a", "Jp371820"]
    | Non-match: ["JP371820 ", "JP371820E", "JP3718", "DP371820A", "JQ371820A",
                  "JO371820A", "JQ37182056"]

    **valid_nino_truncated**

    As valid, but only 4 digits after the first two characters.

    | Match: ["JP3718"]
    | Non-match: ["JP37", "JP371820", "JP371820A"]

    **invalid_final_char_nino**

    As valid, but final character is E-Z (small number issued).

    | Match: ["JP371820G"]
    | Non-match: ["JP371820A"]

    **temp_nino**

    | Starts with TN
    | Ends with F or M or P

    | Match: ["TN123456F", "tn123456f", "Tn123456F]
    | Non-match: ["TN123456R", "AB123456F", "TN1234D", "TN123434"]

    **temp_nino_truncated**

    As temporary, but only 4 digits after the first two characters.

    | Match: ["TN1234"]
    | Non-match: ["Tn12", "TN123456", "AN1234", "TB1234", "TB1234Z"]

    **administrative_nino**

    | First two characters are in: CR, MW, NC, PY, PZ, MA, JY, GY
    | Rest follows valid nino

    | Match: ["PY123456B", "PY123456", "py123456b", "Py123456b"]
    | Non-match: ["PY1234567", "PY12345", "MA123456G", "AA12345", "NC1234A"]

    **administrative_nino_truncated**

    As administrative, but only 4 digits after the first two characters.

    | Match: ["CR1234"]
    | Non-match: ["PY1234B", "PY123456", "AA12345", "NC123"]

    **unallocated_prefix_nino**

    | First two characters are in: BG, GB, NK, KN, TN, NT, ZZ
    | O is allowed as second letter
    | Rest follows valid nino

    | Match: ["NK123456C", "nk123456c", "Nk123456c", "Zz123456"]
    | Non-match: ["BG1234567", "BG123456F", "YY1234", "BG123", "BG1234T"]

    **unallocated_prefix_nino_truncated**

    As unallocated, but only 4 digits after the first two characters.

    | Match: ["BG1234"]
    | Non-match: ["BG1234567", "BG1234F", "YY1234", "BG123", "BG1234T"]

    **ni_nino**

    | Starts with BT
    | Rest follows valid nino

    | Match: ["BT123456A", "BT123456", "bt123456a", "bT123456a"]
    | Non-match: ["BT123456 ", "BT123456g", "BT12345", "BT123454567d",
                  "CT123454567d", "Bz123454567d", "BT1234T"]

    **ni_nino_truncated**

    As Northern Ireland, but only 4 digits after the first two characters.

    | Match: ["BT1234"]
    | Non-match: ["BT123456", "Cy1234", "BT123", "BT1234T"]

    Parameters
    ----------
    nino_type : str
        A string to select the nino regex to return *(valid_nino, valid_nino_truncated,
        invalid_final_char_nino, temp_nino, temp_nino_truncated, administrative_nino,
        administrative_nino_truncated, unallocated_prefix_nino,
        unallocated_prefix_nino_truncated, ni_nino, ni_nino_truncated).*

    Returns
    -------
    str
        A string containing regex corresponding to the nino.

    Example
    -------
    >>> get_nino_regex('valid_nino')

    Notes
    -----
    | Rules for NINOs have been sourced from the following sites
    | https://en.wikipedia.org/wiki/National_Insurance_number
    | https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim39110
    """
    # Nino components
    valid_first_char = '^(?![dfiquvDFIQUV])[a-zA-Z]'
    valid_second_char = '(?![dfiquvoDFIQUVO])[a-zA-Z]'
    digits = '[0-9]{6}'
    digits_truncated = '[0-9]{4}'
    final_char = '([a-dA-D]|$)'
    invalid_final_char = '[e-zE-Z]'
    ni_start = '^[bB][tT]'
    temp_start = '^[tT][nN]'
    temp_end = '[fmpFMP]'
    administrative_start = ('(^[cC][rR]|^[mM][wW]|^[nN][cC]|^[pP][yY]|'
                            '^[pP][zZ]|^[mM][aA]|^[jJ][yY]|^[gG][yY])'
                            )
    unallocated_start = ('(^[bB][gG]|^[gG][bB]|^[nN][kK]|^[kK][nN]|^[tT][nN]|'
                         '^[nN][tT]|^[zZ][zZ]|^([a-zA-Z]oO))'
                         )

    # Nino lookup
    nino_regex = {'valid_nino': f'{valid_first_char}{valid_second_char}{digits}'
                                f'{final_char}$',
                  'valid_nino_truncated': f'{valid_first_char}{valid_second_char}'
                                          f'{digits_truncated}$',
                  'invalid_final_char_nino': f'{valid_first_char}{valid_second_char}'
                                             f'{digits}{invalid_final_char}$',
                  'temp_nino': f'{temp_start}{digits}{temp_end}$',
                  'temp_nino_truncated': f'^{temp_start}{digits_truncated}$',
                  'administrative_nino': f'{administrative_start}{digits}{final_char}$',
                  'administrative_nino_truncated': f'{administrative_start}'
                                                   f'{digits_truncated}$',
                  'unallocated_prefix_nino': f'{unallocated_start}{digits}{final_char}$',
                  'unallocated_prefix_nino_truncated': f'{unallocated_start}'
                                                       f'{digits_truncated}$',
                  'ni_nino': f'{ni_start}{digits}{final_char}$',
                  'ni_nino_truncated': f'{ni_start}{digits_truncated}$'
                  }

    if nino_regex.get(nino_type) is None:
        raise ValueError(
            f"Invalid nino name, valid values are: {', '.join(nino_regex.keys())}"
        )

    return nino_regex[nino_type]
