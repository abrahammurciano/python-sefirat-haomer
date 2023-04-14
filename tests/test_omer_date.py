from datetime import date

import pytest
from pyluach.dates import HebrewDate

from sefirat_haomer import OmerDate, OmerDay

from .utils import tst_compare


@pytest.fixture(
    params=[
        (8, 5783, 1, 23, 2023, 4, 14),
        (49, 5783, 3, 5, 2023, 5, 25),
        (33, 5784, 2, 18, 2024, 5, 26),
    ]
)
def omer_dates(request) -> tuple[OmerDate, HebrewDate, date]:
    (
        day,
        hebrew_year,
        hebrew_month,
        hebrew_day,
        gregorian_year,
        gregorian_month,
        gregorian_day,
    ) = request.param
    return (
        OmerDate(day, hebrew_year=hebrew_year),
        HebrewDate(year=hebrew_year, month=hebrew_month, day=hebrew_day),
        date(year=gregorian_year, month=gregorian_month, day=gregorian_day),
    )


def test_omer_dates(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test that the OmerDate is created correctly."""
    omer_date, hebrew_date, gregorian_date = omer_dates
    assert omer_date.hebrew == hebrew_date
    assert omer_date.gregorian == gregorian_date


def _tst_from_date(
    created: OmerDate,
    omer_date: OmerDate,
    hebrew_date: HebrewDate,
    gregorian_date: date,
) -> None:
    """Test that the OmerDate is created correctly from a HebrewDate or Gregorian date."""
    assert created == omer_date
    assert created.hebrew == hebrew_date
    assert created.gregorian == gregorian_date
    assert created.day == omer_date.day


def test_from_hebrew(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test that the OmerDate can be created from a HebrewDate."""
    omer_date, hebrew_date, greogrian_date = omer_dates
    _tst_from_date(
        OmerDate.from_hebrew(hebrew_date), omer_date, hebrew_date, greogrian_date
    )


def test_from_gregorian(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test that the OmerDate can be created from a Gregorian date."""
    omer_date, hebrew_date, greogrian_date = omer_dates
    _tst_from_date(
        OmerDate.from_gregorian(greogrian_date), omer_date, hebrew_date, greogrian_date
    )


def test_eq(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test that the OmerDate can be compared to other OmerDate instances but not subclasses or other types."""
    omer_date, hebrew_date, _ = omer_dates
    assert omer_date == OmerDate(omer_date, hebrew_year=hebrew_date.year)
    assert omer_date.day == 49 or omer_date != OmerDate(
        omer_date.day + 1, hebrew_year=hebrew_date.year
    )
    assert omer_date != OmerDate(omer_date.day, hebrew_year=hebrew_date.year + 1)
    assert omer_date != OmerDay(omer_date)
    assert omer_date != 1


def test_hash(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test that the OmerDate can be hashed correctly."""
    omer_date, hebrew_date, _ = omer_dates
    assert hash(omer_date) == hash(OmerDate(omer_date, hebrew_year=hebrew_date.year))
    assert omer_date.day == 49 or hash(omer_date) != hash(
        OmerDate(omer_date.day + 1, hebrew_year=hebrew_date.year)
    )
    assert hash(omer_date) != hash(
        OmerDate(omer_date.day, hebrew_year=hebrew_date.year + 1)
    )
    assert hash(omer_date) != hash(OmerDay(omer_date))
    assert hash(omer_date) != hash(1)


def test_lt(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test less than comparison."""
    omer_date, hebrew_date, _ = omer_dates
    other = OmerDate(omer_date, hebrew_year=hebrew_date.year + 1)
    tst_compare(
        omer_date,
        other,
        lambda a, b: a < b,
        match_itself=False,
        illegal=(
            (1, omer_date),
            (omer_date, 1),
            (OmerDay(omer_date), omer_date),
            (omer_date, OmerDay(omer_date)),
        ),
    )
    if omer_date.day != 49:
        other = OmerDate(omer_date.day + 1, hebrew_year=hebrew_date.year)
        tst_compare(omer_date, other, lambda a, b: a < b, match_itself=False)


def test_le(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test less than or equal comparison."""
    omer_date, hebrew_date, _ = omer_dates
    other = OmerDate(omer_date, hebrew_year=hebrew_date.year + 1)
    tst_compare(
        omer_date,
        other,
        lambda a, b: a <= b,
        match_itself=True,
        illegal=(
            (1, omer_date),
            (omer_date, 1),
            (OmerDay(omer_date), omer_date),
            (omer_date, OmerDay(omer_date)),
        ),
    )
    if omer_date.day != 49:
        other = OmerDate(omer_date.day + 1, hebrew_year=hebrew_date.year)
        tst_compare(omer_date, other, lambda a, b: a <= b, match_itself=True)


def test_gt(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test greater than comparison."""
    omer_date, hebrew_date, _ = omer_dates
    other = OmerDate(omer_date, hebrew_year=hebrew_date.year - 1)
    tst_compare(
        omer_date,
        other,
        lambda a, b: a > b,
        match_itself=False,
        illegal=(
            (1, omer_date),
            (omer_date, 1),
            (OmerDay(omer_date), omer_date),
            (omer_date, OmerDay(omer_date)),
        ),
    )
    if omer_date.day != 1:
        other = OmerDate(omer_date.day - 1, hebrew_year=hebrew_date.year)
        tst_compare(omer_date, other, lambda a, b: a > b, match_itself=False)


def test_ge(omer_dates: tuple[OmerDate, HebrewDate, date]) -> None:
    """Test greater than or equal comparison."""
    omer_date, hebrew_date, _ = omer_dates
    other = OmerDate(omer_date, hebrew_year=hebrew_date.year - 1)
    tst_compare(
        omer_date,
        other,
        lambda a, b: a >= b,
        match_itself=True,
        illegal=(
            (1, omer_date),
            (omer_date, 1),
            (OmerDay(omer_date), omer_date),
            (omer_date, OmerDay(omer_date)),
        ),
    )
    if omer_date.day != 1:
        other = OmerDate(omer_date.day - 1, hebrew_year=hebrew_date.year)
        tst_compare(omer_date, other, lambda a, b: a >= b, match_itself=True)
