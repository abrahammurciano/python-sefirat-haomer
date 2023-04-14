import pytest

from sefirat_haomer import OmerDate, OmerDay

from .utils import tst_compare


def test_legal_omer_day():
    """Test that numbers within 1 and 49 and other omer days are accepted."""
    for day in (1, 33, 49):
        OmerDay(day)
        OmerDay(OmerDay(day))


def test_illegal_omer_day():
    """Test that numbers outside 1 and 49 are rejected."""
    for day in (-1, 0, 50, 51):
        with pytest.raises(ValueError):
            OmerDay(day)


@pytest.fixture(
    params=[
        (1, 0, 1),
        (7, 1, 0),
        (8, 1, 1),
        (14, 2, 0),
        (15, 2, 1),
        (21, 3, 0),
        (22, 3, 1),
        (28, 4, 0),
        (29, 4, 1),
        (35, 5, 0),
        (36, 5, 1),
        (42, 6, 0),
        (43, 6, 1),
        (49, 7, 0),
    ]
)
def omer_day(request) -> tuple[OmerDay, int, int]:
    """A fixture that provides a OmerDay instance for each test with the expected number of weeks and days for each one."""
    return OmerDay(request.param[0]), request.param[1], request.param[2]


def test_weeks_and_days(omer_day):
    """Test that the number of weeks and days is calculated correctly."""
    omer_day, weeks, days = omer_day
    assert omer_day.weeks == weeks
    assert omer_day.days == days


def test_unpack(omer_day):
    """Test that the WeeksAndDays instance can be unpacked into weeks and days."""
    omer_day, weeks, days = omer_day
    unpack_weeks, unpack_days = omer_day
    assert (unpack_weeks, unpack_days) == (weeks, days)


def test_int(omer_day):
    """Test that the OmerDay instance can be converted to an int."""
    omer_day, _, _ = omer_day
    assert int(omer_day) == omer_day.day


def test_eq(omer_day):
    """Test that the OmerDay instance can be compared to other OmerDay instances but not subclasses or other types."""
    omer_day, _, _ = omer_day
    assert omer_day == OmerDay(omer_day.day)
    assert omer_day != OmerDay((omer_day.day + 1) % 49 + 1)
    assert omer_day != OmerDate(omer_day.day, hebrew_year=5783)
    assert omer_day != 1


def test_hash(omer_day):
    """Test that the OmerDay instance can be hashed."""
    omer_day, _, _ = omer_day
    assert hash(omer_day) == hash(OmerDay(omer_day))


def test_lt(omer_day):
    """Test that less than works correctly."""
    omer_day, _, _ = omer_day
    if omer_day.day == 49:
        return
    next_day = OmerDay(omer_day.day + 1)
    tst_compare(
        omer_day,
        next_day,
        lambda a, b: a < b,
        match_itself=False,
        illegal=(
            (omer_day, 1),
            (1, omer_day),
            (omer_day, OmerDate(omer_day, hebrew_year=5783)),
            (OmerDate(omer_day, hebrew_year=5783), omer_day),
        ),
    )


def test_le(omer_day):
    """Test that less than or equal works correctly."""
    omer_day, _, _ = omer_day
    if omer_day.day == 49:
        return
    next_day = OmerDay(omer_day.day + 1)
    tst_compare(
        omer_day,
        next_day,
        lambda a, b: a <= b,
        match_itself=True,
        illegal=(
            (omer_day, 1),
            (1, omer_day),
            (omer_day, OmerDate(omer_day, hebrew_year=5783)),
            (OmerDate(omer_day, hebrew_year=5783), omer_day),
        ),
    )


def test_gt(omer_day):
    """Test that greater than works correctly."""
    omer_day, _, _ = omer_day
    if omer_day.day == 1:
        return
    prev_day = OmerDay(omer_day.day - 1)
    tst_compare(
        omer_day,
        prev_day,
        lambda a, b: a > b,
        match_itself=False,
        illegal=(
            (omer_day, 1),
            (1, omer_day),
            (omer_day, OmerDate(omer_day, hebrew_year=5783)),
            (OmerDate(omer_day, hebrew_year=5783), omer_day),
        ),
    )


def test_ge(omer_day):
    """Test that greater than or equal works correctly."""
    omer_day, _, _ = omer_day
    if omer_day.day == 1:
        return
    prev_day = OmerDay(omer_day.day - 1)
    tst_compare(
        omer_day,
        prev_day,
        lambda a, b: a >= b,
        match_itself=True,
        illegal=(
            (omer_day, 1),
            (1, omer_day),
            (omer_day, OmerDate(omer_day, hebrew_year=5783)),
            (OmerDate(omer_day, hebrew_year=5783), omer_day),
        ),
    )
