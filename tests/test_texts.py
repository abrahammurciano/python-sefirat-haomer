import pytest

from sefirat_haomer.texts import EnglishText, HebrewText, PhoneticHebrewText


@pytest.mark.parametrize(
    "subclass, day, kwargs, expected",
    [
        pytest.param(HebrewText, 1, {}, "היום יום אחד לעמר:", id="he_1"),
        pytest.param(PhoneticHebrewText, 1, {}, "HaYom yom echad laomer:", id="ph_1"),
        pytest.param(EnglishText, 1, {}, "Today is one day of the Omer.", id="en_1"),
        pytest.param(
            HebrewText,
            10,
            {},
            "היום עשרה ימים לעמר, שהם שבוע אחד ושלשה ימים:",
            id="he_10",
        ),
        pytest.param(
            PhoneticHebrewText,
            10,
            {},
            "HaYom asara yamim laomer, shehem shavua echad ushlosha yamim:",
            id="ph_10",
        ),
        pytest.param(
            HebrewText,
            33,
            {"vowels": True},
            "הַיּוֹם שְׁלֹשָׁה וּשְׁלֹשִׁים יוֹם לָעֹמֶר, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים:",
            id="he_33_vowels",
        ),
        pytest.param(
            HebrewText,
            33,
            {"laomer_at_end": True},
            "היום שלשה ושלשים יום, שהם ארבעה שבועות וחמשה ימים לעמר:",
            id="he_33_laomer_at_end",
        ),
        pytest.param(
            HebrewText,
            33,
            {"vowels": True, "laomer_at_end": True},
            "הַיּוֹם שְׁלֹשָׁה וּשְׁלֹשִׁים יוֹם, שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וַחֲמִשָּׁה יָמִים לָעֹמֶר:",
            id="he_33_vowels_laomer_at_end",
        ),
    ],
)
def test_text(subclass, day, kwargs, expected):
    """Test that the Hebrew text is returned correctly."""
    assert subclass(day, **kwargs).text() == expected
