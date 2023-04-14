from functools import total_ordering
from typing import Iterator, SupportsInt


@total_ordering
class OmerDay:
    """This class simply represents a day in the Omer count. Essentially it is just contains a number from 1 to 49.

    Args:
        day: The day of the Omer. Must be between 1 and 49.

    Raises:
        ValueError: If the day is not between 1 and 49.
    """

    __slots__ = ("_day",)

    def __init__(self, day: SupportsInt) -> None:
        self._day = int(day)
        if not 1 <= self._day <= 49:
            raise ValueError("Omer day must be between 1 and 49")

    @property
    def day(self) -> int:
        """The day of the Omer."""
        return self._day

    @property
    def weeks(self) -> int:
        """The number of complete weeks in the total number of days."""
        return self.day // 7

    @property
    def days(self) -> int:
        """The number of days in the total number of days that are not part of a complete week."""
        return self.day % 7

    def __int__(self) -> int:
        return self.day

    def __iter__(self) -> Iterator[int]:
        return iter(divmod(self.day, 7))

    def __str__(self) -> str:
        return f"Omer day {self.day}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.day})"

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return self.day == other.day  # type: ignore
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.day)

    def __lt__(self, other: object) -> bool:
        if type(self) is type(other):
            return self.day < other.day  # type: ignore
        return NotImplemented
