from typing import Sequence, SupportsInt


class Text:
    """A base for classes which provide the text of the Sefirat HaOmer for the given day.

    Classes which inherit from this one should define the following values.
    - `TEXTS` - A sequence of the texts for each day in order (first day at index 0). Each text should end with the value of `END` and optionally contain a single `PAUSE`. If it does, then `LAOMER` will be inserted before the pause, else it will be inserted before the `END`.
    - `LAOMER` - The text to insert before the `PAUSE` or `END`. This should mean "of the omer" in the language of the text.
    - `PAUSE` - The text separating the total count from the weeks and days. Optional, defaults to `","`.
    - `END` - The text at the end of each text. Optional, defaults to `":"`.

    Args:
        day: The day of the Omer count.
        laomer_at_end: Whether to put the `LAOMER` before the `END` always. Defaults to False.
    """

    TEXTS: Sequence[str]
    LAOMER: str
    PAUSE: str = ","
    END: str = ":"

    __slots__ = ("day", "_laomer_at_end")

    def __init__(self, day: SupportsInt, laomer_at_end: bool = False):
        self.day = int(day)
        self._laomer_at_end = laomer_at_end
        assert self.TEXTS is not None, "TEXTS must be defined in the subclass."
        assert self.LAOMER is not None, "LAOMER must be defined in the subclass."

    def __str__(self):
        return self.text()

    def text(self) -> str:
        """Get the text of the Omer count for this day in Hebrew."""
        text = self.TEXTS[self.day - 1]
        char = self.END if self._laomer_at_end or self.PAUSE not in text else self.PAUSE
        return text.replace(char, f" {self.LAOMER}{char}")
