import pytest

from sefirat_haomer import OmerCalendar, OmerDate


@pytest.fixture(params=[5783, 5784])
def omer_calendars(request) -> tuple[OmerCalendar, int]:
    """Return an OmerCalendar and its Hebrew year."""
    hebrew_year = request.param
    return OmerCalendar(hebrew_year=hebrew_year), hebrew_year


def test_init():
    """Test that the OmerCalendar can be initialized correctly."""
    assert OmerCalendar(hebrew_year=5783) == OmerCalendar(gregorian_year=2023)


@pytest.mark.parametrize(
    "index", [0, 1, 7, 8, 14, 15, 21, 22, 28, 29, 35, 36, 42, 43, 48]
)
def test_get_item(omer_calendars: tuple[OmerCalendar, int], index: int):
    """Test that the OmerCalendar can be indexed."""
    omer_calendar, hebrew_year = omer_calendars
    assert omer_calendar[index] == OmerDate(index + 1, hebrew_year=hebrew_year)


@pytest.mark.parametrize(
    "slc",
    [
        slice(None, 1),
        slice(None, 33),
        slice(None, 49),
        slice(None, 100),
        slice(-1, 33),
        slice(33, 40),
        slice(33, 100),
        slice(0, 49, 2),
        slice(None, None, -1),
        slice(49, 0, -1),
    ],
)
def test_get_item_slice(omer_calendars: tuple[OmerCalendar, int], slc: slice):
    """Test that the OmerCalendar can be sliced."""
    omer_calendar, hebrew_year = omer_calendars
    assert (
        omer_calendar[slc]
        == [OmerDate(i, hebrew_year=hebrew_year) for i in range(1, 50)][slc]
    )


def test_iter(omer_calendars: tuple[OmerCalendar, int]):
    """Test that the OmerCalendar can be iterated over."""
    omer_calendar, hebrew_year = omer_calendars
    assert list(omer_calendar) == [
        OmerDate(i, hebrew_year=hebrew_year) for i in range(1, 50)
    ]


def test_len(omer_calendars: tuple[OmerCalendar, int]):
    """Test that the OmerCalendar has a length of 49."""
    omer_calendar, _ = omer_calendars
    assert len(omer_calendar) == 49


def test_eq(omer_calendars: tuple[OmerCalendar, int]):
    """Test that the OmerCalendar can be compared for equality."""
    omer_calendar, hebrew_year = omer_calendars
    assert omer_calendar == OmerCalendar(hebrew_year=hebrew_year)
    assert omer_calendar != OmerCalendar(hebrew_year=hebrew_year + 1)


def test_hash(omer_calendars: tuple[OmerCalendar, int]):
    """Test that the OmerCalendar can be hashed."""
    omer_calendar, hebrew_year = omer_calendars
    assert hash(omer_calendar) == hash(OmerCalendar(hebrew_year=hebrew_year))
    assert hash(omer_calendar) != hash(OmerCalendar(hebrew_year=hebrew_year + 1))


def test_contains(omer_calendars: tuple[OmerCalendar, int]):
    """Test that the OmerCalendar can be checked for containment."""
    omer_calendar, hebrew_year = omer_calendars
    assert OmerDate(1, hebrew_year=hebrew_year) in omer_calendar
    assert OmerDate(49, hebrew_year=hebrew_year) in omer_calendar
    assert OmerDate(1, hebrew_year=hebrew_year + 1) not in omer_calendar
