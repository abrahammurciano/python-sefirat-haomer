import pytest

from sefirat_haomer.weeks_and_days import WeeksAndDays


@pytest.fixture(
    params=[
        (0, 0, 0),
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
def weeks_and_days(request):
    """A fixture that provides a WeeksAndDays instance for each test."""
    return WeeksAndDays(request.param[0]), request.param[1], request.param[2]


def test_weeks_and_days(weeks_and_days):
    """Test that the number of weeks and days is calculated correctly."""
    weeks_and_days, weeks, days = weeks_and_days
    assert weeks_and_days.weeks == weeks
    assert weeks_and_days.days == days


def test_unpack(weeks_and_days):
    """Test that the WeeksAndDays instance can be unpacked into weeks and days."""
    weeks_and_days, weeks, days = weeks_and_days
    unpack_weeks, unpack_days = weeks_and_days
    assert (unpack_weeks, unpack_days) == (weeks, days)
