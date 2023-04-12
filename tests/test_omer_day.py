import pytest

from sefirat_haomer.omer_day import OmerDay


def test_legal_omer_day():
    """Test that numbers within 1 and 49 are accepted."""
    for day in range(1, 50):
        OmerDay(day)


def test_illegal_omer_day():
    """Test that numbers outside 1 and 49 are rejected."""
    for day in (-1, 0, 50, 51):
        with pytest.raises(ValueError):
            OmerDay(day)
