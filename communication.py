#!/usr/bin/env python

"""communication.py: Creates a single communication (email, call, etc)."""

import datetime


class Communication:
    """Creates log of a single communication to/from a Company."""

    def __init__(self, yr_mo_day_tuple, interaction, notes, status):
        """
        //TODO: Docstring
        :param yr_mo_day_tuple: 
        :type yr_mo_day_tuple: 
        :param interaction: "Call", "Email", or "Meeting"
        :type interaction: 
        :param notes: 
        :type notes: 
        :param status: "Done", "In Progress", "Cancelled", or "Failed"
        :type status: 
        """
        self._date = datetime.datetime(*yr_mo_day_tuple)
        self._interaction = interaction
        self._notes = notes
        self._status = status

    def __repr__(self):
        return f'Communication object: "{self._date.strftime("%x"), self._interaction, self._notes}"'

    def __str__(self):
        return f'{self._date.strftime("%x")}  {self._interaction}  {self._status}  --  "{self._notes}"'

    def set_date(self, yr_mo_day_tuple):
        self._date = datetime.datetime(*yr_mo_day_tuple)

    def get_date(self):
        return self._date.strftime('%x')

    # Set & Get
    def set_interaction(self, interaction):
        """Sets interaction to 'Call', 'Email', or 'Meeting'."""
        self._interaction = interaction

    def get_interaction(self):
        return self._interaction

    def set_notes(self, notes):
        """Set notes from communication."""
        self._notes = notes

    def get_notes(self):
        """Returns notes from communication."""
        return self._notes

    def set_status(self, status):
        """Set status to 'Done', 'In Progress', 'Cancelled' or 'Failed'."""
        self._status = status

    def get_status(self):
        return self._status


if __name__ == '__main__':
    comm = Communication((2020, 12, 20), 0, 'You are invited to Online Assessment!', 0)
    print(comm)
