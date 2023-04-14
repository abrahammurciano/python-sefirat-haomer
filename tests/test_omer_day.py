import pytest

from sefirat_haomer.omer_day import OmerDay


def test_legal_omer_day():
    """Test that numbers within 1 and 49 are accepted."""
    for day in (1, 33, 49):
        OmerDay(day)


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
