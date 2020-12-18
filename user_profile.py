#!/usr/bin/env python

"""user_profile.py: Creates a user and a profile of their basic information."""

class User:
    """Creates a user object and its basic information."""
    _counter = 0

    def __init__(self, first_name, last_name, phone_number):
        """Initializes a User object."""
        self._first_name = first_name
        self._last_name = last_name
        self._middle_initial = ''
        self._address = ''
        self._phone = phone_number
        self._dob_mdy = None
        self._ssn = None
        self._id = User._counter
        User._counter += 1

    def __repr__(self):
        pass

    def set_name(self, first_name, last_name, middle_initial=''):
        """Sets user first, last, (optional) middle name."""
        self.first_name, self.last_name, self.middle_initial =  first_name, last_name, middle_initial

    def get_name(self):
        """Returns first, last, middle name as a tuple"""
        return self.first_name, self.last_name, self.middle_initial

    def set_address(self, address, city, state, zip):
        """Sets user address."""

    def get_address(self):
        pass

    def set_phone(self, phone):
        pass

    def get_phone(self):
        pass

    def set_dob(self, dob):
        pass

    def get_dob(self):
        pass

    def set_ssn(self, ssn):
        pass

    def get_ssn(self):
        pass

    def get_id(self):
        pass
