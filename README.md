# sefirat-haomer
A library for calculating the days of Sefirat HaOmer.

## Installation

You can install this package with pip or conda.
```sh
$ pip install sefirat-haomer
```
```sh
$ conda install -c abrahammurciano sefirat-haomer
```

## Links

[![Documentation](https://img.shields.io/badge/Documentation-C61C3E?style=for-the-badge&logo=Read+the+Docs&logoColor=%23FFFFFF)](https://abrahammurciano.github.io/python-sefirat-haomer/sefirat-haomer)

[![Source Code - GitHub](https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=%23FFFFFF)](https://github.com/abrahammurciano/python-sefirat-haomer.git)

[![PyPI - sefirat-haomer](https://img.shields.io/badge/PyPI-sefirat-haomer-006DAD?style=for-the-badge&logo=PyPI&logoColor=%23FFD242)](https://pypi.org/project/sefirat-haomer/)

[![Anaconda - sefirat-haomer](https://img.shields.io/badge/Anaconda-sefirat-haomer-44A833?style=for-the-badge&logo=Anaconda&logoColor=%23FFFFFF)](https://anaconda.org/abrahammurciano/sefirat-haomer)

## Usage

This library provides three main classes. `OmerDay` which represents a single day (1 to 49) of Sefirat HaOmer (not bound to any particular year), `OmerDate` which represents a day of Sefirat HaOmer in a particular year, and `OmerCalendar` which is a collection of `OmerDate` objects for a particular year.

For an actual example of how this library was used to generate Google Calendar events for the next 100 years, see [this example](expamples/google_calendar.py). (Interestingly, this is why I wrote this library in the first place.)

### `OmerDay`

Here are some examples of how to use the `OmerDay` class.

```python
>>> from sefirat_haomer import OmerDay
>>> day = OmerDay(33)
```

`OmerDay` objects have the following attributes:
```python
>>> day.day
33
>>> day.weeks
4
>>> day.days
5
```

You can also get the day of the week for a given `OmerDay` by unpacking it:
```python
>>> weeks, days = day
>>> weeks
4
>>> days
5
```

`OmerDay` objects can be converted to integers:
```python
>>> int(day)
33
```

`OmerDay` objects can also be compared to other `OmerDay` objects:
```python
>>> day == OmerDay(33)
True
>>> day != OmerDay(33)
False
>>> day < OmerDay(45)
True
>>> day > OmerDay(45)
False
>>> day <= OmerDay(20)
False
>>> day >= OmerDay(20)
True
```

### `OmerDate`

Here are some examples of how to use the `OmerDate` class.

`OmerDate` objects can be created in any of the following ways. (All the following examples are equivalent.)
```python
>>> from sefirat_haomer import OmerDate
>>> from pyluach.dates import HebrewDate
>>> from datetime import date
>>> date = OmerDate(8, hebrew_year=5783)
>>> date = OmerDate(8, gregorian_year=2023)
>>> date = OmerDate.from_hebrew(HebrewDate(5783, 1, 23))
>>> date = OmerDate.from_gregorian(date(2023, 4, 14))
```

`OmerDate` objects have the following attributes (in addition to those inherited from `OmerDay`):
```python
>>> date.hebrew
HebrewDate(5783, 1, 23)
>>> date.gregorian
datetime.date(2023, 4, 14)
```

`OmerDate` objects can be compared to other `OmerDate` objects:
```python
>>> date == OmerDate(8, hebrew_year=5783)
True
>>> date != OmerDate(8, hebrew_year=5784)
True
>>> date != OmerDate(33, gregorian_year=5783)
True
>>> date < OmerDate(33, gregorian_year=5782)
True
>>> date > OmerDate(33, gregorian_year=5784)
True
>>> date <= OmerDate(33, gregorian_year=5782)
False
>>> date >= OmerDate(33, gregorian_year=5784)
False
```

### `OmerCalendar`

Here are some examples of how to use the `OmerCalendar` class.

`OmerCalendar` objects can be created in any of the following ways. (All the following examples are equivalent.)

```python
>>> from sefirat_haomer import OmerCalendar
>>> calendar = OmerCalendar(hebrew_year=5783)
>>> calendar = OmerCalendar(gregorian_year=2023)
```

`OmerCalendar` objects have the following attributes:
```python
>>> calendar.hebrew_year
5783
>>> calendar.gregorian_year
2023
```

`OmerCalendar` objects can be indexed just like a list:
```python
>>> calendar[0]
OmerDate(1, hebrew_year=5783)
>>> calendar[48]
OmerDate(49, hebrew_year=5783)
>>> calendar[-1]
OmerDate(49, hebrew_year=5783)
>>> calendar[:2]
[OmerDate(1, hebrew_year=5783), OmerDate(2, hebrew_year=5783)]
>>> calendar[2:5]
[OmerDate(3, hebrew_year=5783), OmerDate(4, hebrew_year=5783), OmerDate(5, hebrew_year=5783)]
>>> calendar[46:]
[OmerDate(47, hebrew_year=5783), OmerDate(48, hebrew_year=5783), OmerDate(49, hebrew_year=5783)]
>>> calendar[5:10:2]
[OmerDate(6, hebrew_year=5783), OmerDate(8, hebrew_year=5783), OmerDate(10, hebrew_year=5783)]
```

`OmerCalendar` objects can be iterated over:
```python
>>> for day in calendar:
...     print(day)
```

`OmerCalendar` objects can also tell you if a given `OmerDate` is in the calendar:
```python
>>> OmerDate(1, hebrew_year=5783) in calendar
True
>>> OmerDate(1, hebrew_year=5784) in calendar
False
```
