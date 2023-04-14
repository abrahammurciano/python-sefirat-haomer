"""
.. include:: ../README.md
"""


import importlib.metadata as metadata

__version__ = metadata.version(__package__ or __name__)

from .omer_calendar import OmerCalendar
from .omer_date import OmerDate
from .omer_day import OmerDay

__all__ = ("OmerCalendar", "OmerDate", "OmerDay")
