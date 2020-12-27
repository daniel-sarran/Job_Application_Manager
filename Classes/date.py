#!/usr/bin/env python

"""date.py: Simple date class where dates can be compared."""
import datetime


class Date:
    """Represents a date."""

    def __init__(self, yr, mo, day):
        self._date = datetime.date(yr, mo, day)

    def __lt__(self, other):
        return self._date < other._date

    def __le__(self, other):
        return self._date <= other._date

    def __gt__(self, other):
        return self._date > other._date

    def __ge__(self, other):
        return self._date >= other._date

    def __eq__(self, other):
        return self._date == other._date

    def __ne__(self, other):
        return self._date != other._date

    def set_date(self, yr_mo_day_tuple):
        self._date = datetime.date(*yr_mo_day_tuple)

    def get_date(self):
        return self._date


if __name__ == '__main__':
    new_date = Date(2020, 12, 20)
    print(new_date)
    new_date2 = Date(2020, 12, 21)
    print(new_date2)
    print('newdate < newdate2: ', {new_date < new_date2})
