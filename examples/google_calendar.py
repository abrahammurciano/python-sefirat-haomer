import csv
from typing import Any, Iterable, NamedTuple

from pyluach.dates import HebrewDate

from sefirat_haomer import OmerCalendar
from sefirat_haomer.texts import HebrewText


class Row(NamedTuple):
    subject: str
    description: Any
    start_date: str
    all_day_event: bool = True
    private: bool = False


def rows() -> Iterable[Iterable[Any]]:
    for year in range(HebrewDate.today().year, 6001):
        for day in OmerCalendar(hebrew_year=year):
            subject = f"Omer {day.day}"
            if day.weeks:
                subject += f" ({day.weeks} weeks{f' and {day.days} days' if day.days else ''})".replace(
                    "1 weeks", "1 week"
                ).replace(
                    "1 days", "1 day"
                )
            yield Row(subject, HebrewText(day), day.gregorian.isoformat())


if __name__ == "__main__":
    with open("sefirat_haomer.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(f.replace("_", " ").title() for f in Row._fields)
        writer.writerows(rows())
