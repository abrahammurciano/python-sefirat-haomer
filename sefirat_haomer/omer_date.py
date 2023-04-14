from datetime import date
from functools import total_ordering
from typing import SupportsInt

from pyluach.dates import HebrewDate

from .omer_day import OmerDay


@total_ordering
class OmerDate(OmerDay):
    """This class represents a date of the Omer on a certain year.

    Args:
        omer_day: The day of the Omer.
        hebrew_year: The Hebrew year of the Omer. If omitted, gregorian_year must be provided.
        gregorian_year: The Gregorian year of the Omer. If omitted, hebrew_year must be provided.
    """

    __slots__ = "_hebrew_year"

    def __init__(
        self,
        day: SupportsInt,
        *,
        hebrew_year: int | None = None,
        gregorian_year: int | None = None,
    ) -> None:
        super().__init__(day)
        self._hebrew_year = _hebrew_year(hebrew_year, gregorian_year)

    @classmethod
    def from_hebrew(cls, hebrew_date: HebrewDate) -> "OmerDate":
        """Create an OmerDate from a HebrewDate.

        Args:
            hebrew_date: The Hebrew date to convert to an OmerDate.
        """
        return cls(
            hebrew_date - HebrewDate(hebrew_date.year, 1, 15),
            hebrew_year=hebrew_date.year,
        )

    @classmethod
    def from_gregorian(cls, gregorian_date: date) -> "OmerDate":
        """Create an OmerDate from a Gregorian date.

        Args:
            gregorian_date: The Gregorian date to convert to an OmerDate.
        """
        return cls.from_hebrew(HebrewDate.from_pydate(gregorian_date))

    @property
    def hebrew(self) -> HebrewDate:
        """The Hebrew date of the Omer."""
        return HebrewDate(self._hebrew_year, 1, 15) + self.day

    @property
    def gregorian(self) -> date:
        """The Gregorian date of the Omer."""
        return self.hebrew.to_pydate()

    def __str__(self) -> str:
        return f"{super().__str__()} of year {self._hebrew_year}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.day}, hebrew_year={self._hebrew_year})"

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return super().__eq__(other) and self._hebrew_year == other._hebrew_year  # type: ignore
        return NotImplemented

    def __hash__(self) -> int:
        return hash((super().__hash__(), self._hebrew_year))

    def __lt__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return (self._hebrew_year, self.day) < (other._hebrew_year, other.day)
        return NotImplemented


def _hebrew_year(hebrew_year: int | None, gregorian_year: int | None) -> int:
    """Return the Hebrew year from either the Hebrew or Gregorian year.

    Args:
        hebrew_year: The Hebrew year. If omitted, gregorian_year must be provided.
        gregorian_year: The Gregorian year. If omitted, hebrew_year must be provided.

    Returns:
        The Hebrew year.

    Raises:
        ValueError: If neither hebrew_year nor gregorian_year is provided.
    """
    if hebrew_year is None:
        if gregorian_year is None:
            raise ValueError("Either hebrew_year or gregorian_year must be provided.")
        hebrew_year = gregorian_year + 3760
    return hebrew_year
