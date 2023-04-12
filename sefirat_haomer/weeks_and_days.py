from typing import Iterator


class WeeksAndDays:
    """Represents a number of days split into weeks and days.

    Instances of this class are also iterable with exactly two items: the number of weeks and the number of days. This is so that they can be easily unpacked into separate variables.

    Args:
        days: The total number of days to split into weeks and days.

    Attributes:
        weeks: The number of weeks in the total number of days.
        days: The number of days in the total number of days.
    """

    def __init__(self, total_days: int) -> None:
        self._total_days = total_days

    @property
    def weeks(self) -> int:
        """The number of complete weeks in the total number of days."""
        return self._total_days // 7

    @property
    def days(self) -> int:
        """The number of days in the total number of days that are not part of a complete week."""
        return self._total_days % 7

    @property
    def total_days(self) -> int:
        """The total number of days."""
        return self._total_days

    def __iter__(self) -> Iterator[int]:
        yield self.weeks
        yield self.days
