from typing import Iterator


class OmerDay:
    """This class simply represents a day in the Omer count. Essentially it is just contains a number from 1 to 49.

    Args:
        day: The day of the Omer. Must be between 1 and 49.

    Raises:
        ValueError: If the day is not between 1 and 49.
    """

    def __init__(self, day: int) -> None:
        if not 1 <= day <= 49:
            raise ValueError("Omer day must be between 1 and 49")
        self._day = day

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

    def __iter__(self) -> Iterator[int]:
        return iter(divmod(self.day, 7))
