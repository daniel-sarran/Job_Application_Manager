#!/usr/bin/env python

"""communication.py: Creates a single communication (email, call, etc)."""

import datetime


class Communication:
    """Creates a log of a single communication to/from a Company."""

    def __init__(self, year, month, day, msg_type, note, status):
        # contacts = heap - with dates, type, and notes
        # self._application = obj_application
        self._contact_type = ('Phone Call Out', 'Phone call in', 'Email sent', 'Email received', 'Face-to-face')
        self._status_type = ('In Progress', 'Cancelled', 'Failed', 'Done')

        self._date = datetime.datetime(year, month, day)
        self._type = msg_type
        self._note = note
        self._status = status

    def __repr__(self):
        return f'Communication object: "{self._date.strftime("%x"), self._type, self._note}"'

    def __str__(self):
        return f'{self._date.strftime("%x")}  {self._type}  {self._status}  --  {self._note}'

    def set_date(self, year, month, day):
        self._date = datetime.datetime(year, month, day)

    def get_date(self):
        return self._date.strftime('%x')

    # Set & Get
    # contact type
    # status
    # etc


if __name__ == '__main__':
    comm = Communication(2020, 12, 20, 'Email received', 'Invited to Online Assessment!', 'In Progress')
    print(comm)
