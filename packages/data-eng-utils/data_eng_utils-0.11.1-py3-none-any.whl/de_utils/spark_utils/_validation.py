from pyspark.sql import functions as F
from functools import reduce


def _check_nhs_format(col):
    return col.rlike("^\\d{10}$")


def _check_vat_format(col):
    return col.rlike("^\\d{9}$")


def _nhs_check_digit(nhs_no):
    """Get a check digit from an NHS number."""
    return nhs_no.substr(10, 1).cast("int")


def _nhs_check_sum(nhs_no):
    """Get a check sum from an NHS number."""
    return (11 - reduce(
        lambda x, y:
        x + nhs_no.substr(y + 1, 1).cast("int") * (10 - y),
        range(9),
        F.lit(0)
    ) % F.lit(11)) % F.lit(11)


def validate_nhs_no(nhs_no):
    """Validate an NHS number.

    Checek that the column contains only 10 digits and asserts
    the checksum is equal to checkdigit.

    :returns: a pyspark column of boolean values
    :rtype: pyspark.sql.column.Column
    """
    return (_check_nhs_format(nhs_no)
            & (_nhs_check_sum(nhs_no) == _nhs_check_digit(nhs_no)))


def _vat_check_digit(vat_no):
    """Get checkdigit from vat number."""
    return vat_no.substr(8, 2).cast("int")


def validate_vat_no(vat_no):
    """Validat VAT number.

    Checek that the column contains only 9 digits and asserts
    the checksum is equal to checkdigit.
    Note: this function only checks the 'standard' 9 digit vat number.
    Branch traders, governemt departments and health authorities
    are not currently checked.

    :returns: a pyspark column of boolean values
    :rtype: pyspark.sql.column.Column
    """
    return (_check_vat_format(vat_no)
            & (_vat_check_sum(vat_no) == _vat_check_digit(vat_no)))


def _vat_check_sum(vat_no):
    """Get check digit from VAT number."""
    subtotal = reduce(
        lambda x, y:
        x + vat_no.substr(y + 1, 1).cast("int") * (8 - y),
        range(7),
        F.lit(0)
    )
    return (97 * F.ceil(subtotal / 97)) - subtotal
