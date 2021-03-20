#!/usr/bin/env python

"""communication.py: Creates a single communication (email, call, etc)."""

import textwrap
from Components.date import Date


class Activity(Date):
    """Creates log of a single communication to/from an employer."""

    def __init__(self, yr_mo_day_tuple, interaction_type, status, notes=''):
        super().__init__(*yr_mo_day_tuple)
        self._interaction_types = {
            0: 'Call',
            1: 'Email',
            2: 'Meeting'
        }
        self._interaction_type = self._interaction_types[interaction_type]
        self._notes = notes
        self._statuses = {
            0: 'Scheduled',
            1: 'Done'
        }
        self._status = self._statuses[status]

    def __repr__(self):
        return f'<Communication object: "{self._interaction_type} on {self._date.strftime("%x")} -- {self._notes}>"'

    def __str__(self):
        note = self._notes
        if len(self._notes) > 40:
            note = note[:37] + '...'
        return f'{self.get_clean_date():<15s}{self.get_status():<13s}{self.get_interaction_type():<10s}' \
               f'{note:<40s}'

    def _get_date(self):
        return self._date

    def set_interaction_type(self, interaction):
        """Sets interaction to 'Call', 'Email', or 'Meeting'."""
        self._interaction_type = interaction

    def get_interaction_type(self):
        return self._interaction_type

    def set_notes(self, notes):
        """Set notes from communication."""
        self._notes = notes

    def get_notes(self):
        """Returns notes from communication."""
        note_lines = textwrap.wrap(self._notes)
        return note_lines

    def set_status(self, status):
        """Set status to 'Done', 'In Progress', 'Cancelled' or 'Failed'."""
        self._status = status

    def get_status(self):
        return self._status


if __name__ == '__main__':
    comm = Activity((2020, 12, 20), 0, 0, 'You are invited to Online Assessment!')
    print(comm)
    comm2 = Activity((2020, 12, 21), 0, 0, 'Recruiter: focus on problem solving process over working code')
    print(comm2)
    print(comm < comm2)
