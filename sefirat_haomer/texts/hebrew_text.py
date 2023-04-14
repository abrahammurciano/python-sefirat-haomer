import re
from typing import SupportsInt

from .text import Text


class HebrewText(Text):
    """Get the text of the Omer count for this day in Hebrew.

    Args:
        omer_day: The day of the Omer count.
        laomer_at_end: If True, the word "לעמר" will be at the end of the text. Otherwise it will be before the weeks and days.
    """

    TEXTS = (
        "הַיּוֹם יוֹם אֶחָד:",
        "הַיּוֹם שְׁנֵי יָמִים:",
        "הַיּוֹם שְׁלֹשָׁה יָמִים:",
        "הַיּוֹם אַרְבָּעָה יָמִים:",
        "הַיּוֹם חֲמִשָּׁה יָמִים:",
        "הַיּוֹם שִׁשָּׁה יָמִים:",
        "הַיּוֹם שִׁבְעָה יָמִים, שֶׁהֵם שָׁבוּעַ אֶחָד:",
        "הַיּוֹם שְׁמוֹנָה יָמִים, שֶׁהֵם שָׁבוּעַ אֶחָד וְיוֹם אֶחָד:",
        "הַיּוֹם תִּשְׁעָה יָמִים, שֶׁהֵם שָׁבוּעַ אֶחָד וּשְׁנֵי יָמִים:",
        "הַיּוֹם עֲשָׂרָה יָמִים, שֶׁהֵם שָׁבוּעַ אֶחָד וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם אַחַד עָשָׂר יוֹם, שֶׁהֵם שָׁבוּעַ אֶחָד וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם שְׁנֵים עָשָׂר יוֹם, שֶׁהֵם שָׁבוּעַ אֶחָד וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם שְׁלֹשָׁה עָשָׂר יוֹם, שֶׁהֵם שָׁבוּעַ אֶחָד וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם אַרְבָּעָה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת:",
        "הַיּוֹם חֲמִשָּׁה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְיוֹם אֶחָד:",
        "הַיּוֹם שִׁשָּׁה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וּשְׁנֵי יָמִים:",
        "הַיּוֹם שִׁבְעָה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם שְׁמוֹנָה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם תִּשְׁעָה עָשָׂר יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם עֶשְׂרִים יוֹם, שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם אֶחָד וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת:",
        "הַיּוֹם שְׁנַֽיִם וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְיוֹם אֶחָד:",
        "הַיּוֹם שְׁלֹשָׁה וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים:",
        "הַיּוֹם אַרְבָּעָה וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם חֲמִשָּׁה וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם שִׁשָּׁה וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם שִׁבְעָה וְעֶשְׂרִים יוֹם, שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם שְׁמוֹנָה וְעֶשְׂרִים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת:",
        "הַיּוֹם תִּשְׁעָה וְעֶשְׂרִים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְיוֹם אֶחָד:",
        "הַיּוֹם שְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וּשְׁנֵי יָמִים:",
        "הַיּוֹם אֶחָד וּשְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם שְׁנַיִם וּשְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם שְׁלֹשָׁה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם אַרְבָּעָה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם חֲמִשָּׁה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת:",
        "הַיּוֹם שִׁשָּׁה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וְיוֹם אֶחָד:",
        "הַיּוֹם שִׁבְעָה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים:",
        "הַיּוֹם שְׁמוֹנָה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם תִּשְׁעָה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם אַרְבָּעִים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם אֶחָד וְאַרְבָּעִים יוֹם, שֶׁהֵם חֲמִשָּׁה שָׁבוּעוֹת וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם שְׁנַיִם וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת:",
        "הַיּוֹם שְׁלֹשָׁה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וְיוֹם אֶחָד:",
        "הַיּוֹם אַרְבָּעָה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים:",
        "הַיּוֹם חֲמִשָּׁה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים:",
        "הַיּוֹם שִׁשָּׁה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים:",
        "הַיּוֹם שִׁבְעָה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
        "הַיּוֹם שְׁמוֹנָה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁשָּׁה שָׁבוּעוֹת וְשִׁשָּׁה יָמִים:",
        "הַיּוֹם תִּשְׁעָה וְאַרְבָּעִים יוֹם, שֶׁהֵם שִׁבְעָה שָׁבוּעוֹת:",
    )
    LAOMER = "לָעֹמֶר"

    __slots__ = ("_vowels",)

    def __init__(
        self, day: SupportsInt, laomer_at_end: bool = False, vowels: bool = False
    ):
        super().__init__(day, laomer_at_end)
        self._vowels = vowels

    def text(self) -> str:
        text = super().text()
        if not self._vowels:
            text = re.sub(r"[\u0591-\u05BD\u05BF-\u05C2\u05C4-\u05C7]", "", text)
        return text
