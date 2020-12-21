#!/usr/bin/env python

"""contact.py: Creates a single communication (email, call, etc)."""


class Communication:
    """Creates a Communication object representing a single contact history to or from a Company."""

    def __init__(self, date, type, note, status):
        # contacts = heap - with dates, type, and notes
        self._contact_type = ('Phone Call Out', 'Phone call in', 'Email sent', 'Email received', 'Face-to-face')
        self._status_type = ('In Progress', 'Cancelled', 'Failed', 'Done')
        self._date = date
        self._type = type
        self._note = note
        self._status = status

    def __repr__(self):
        pass

    def set_date(self, date):
        pass

    def get_communication(self, date, time):
        pass

    def set_communication(self, date, type, message):
        pass

