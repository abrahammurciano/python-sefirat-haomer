from dataclasses import dataclass

from .weeks_and_days import WeeksAndDays


@dataclass
class OmerDay:
    """This class simply represents a day in the Omer count. Essentially it is just contains a number from 1 to 49."""

    day: int

    def __post_init__(self):
        if not 1 <= self.day <= 49:
            raise ValueError("Omer day must be between 1 and 49")

    def weeks_and_days(self) -> WeeksAndDays:
        """The number of weeks and days in the Omer count.

        Examples:
            >>> weeks, days = OmerDay(33).weeks_and_days
            >>> weeks = OmerDay(33).weeks_and_days.weeks
            >>> days = OmerDay(33).weeks_and_days.days
        """
        return WeeksAndDays(self.day)
