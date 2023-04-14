from typing import Iterator, SupportsInt, overload

from .omer_date import OmerDate, _hebrew_year


class OmerCalendar:
    """A collection of Omer dates for a given year.

    Args:
        hebrew_year: The Hebrew year of the Omer. If omitted, gregorian_year must be provided.
        gregorian_year: The Gregorian year of the Omer. If omitted, hebrew_year must be provided.
    """

    __slots__ = ("_hebrew_year",)

    def __init__(
        self,
        *,
        hebrew_year: int | None = None,
        gregorian_year: int | None = None,
    ) -> None:
        self._hebrew_year = _hebrew_year(hebrew_year, gregorian_year)

    @overload
    def __getitem__(self, day: int | SupportsInt) -> OmerDate:
        """Get an OmerDate for a given day."""
        ...

    @overload
    def __getitem__(self, day: slice) -> list[OmerDate]:
        """Get a list of OmerDates for a given slice."""
        ...

    def __getitem__(self, day: int | SupportsInt | slice) -> OmerDate | list[OmerDate]:
        if isinstance(day, slice):
            return [self[i] for i in range(*day.indices(49))]
        index = int(day)
        return OmerDate(
            index + 1 if index >= 0 else 50 + index, hebrew_year=self._hebrew_year
        )

    def __iter__(self) -> Iterator[OmerDate]:
        """Iterate over all the Omer dates in the calendar."""
        return iter(self[i] for i in range(49))

    def __len__(self) -> int:
        """The number of Omer dates in the calendar."""
        return 49

    @property
    def hebrew_year(self) -> int:
        """The Hebrew year of this Omer calendar."""
        return self._hebrew_year

    @property
    def gregorian_year(self) -> int:
        """The Gregorian year of this Omer calendar."""
        return self._hebrew_year - 3760

    def __repr__(self) -> str:
        return f"{type(self).__name__}(hebrew_year={self._hebrew_year})"

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._hebrew_year})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return self._hebrew_year == other._hebrew_year
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._hebrew_year)

    def __contains__(self, omer_date: OmerDate) -> bool:
        return self._hebrew_year == omer_date.hebrew.year
