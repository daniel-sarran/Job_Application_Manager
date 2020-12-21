#!/usr/bin/env python

"""company.py: Creates a user and a profile of their basic information."""


class Company:
    """Creates a Company object representing the employer receiving the application."""

    def __init__(self, name, industry='', description=''):
        """Initializes a Company object."""
        self._name = name
        self._industry = industry
        self._description = description

    def __repr__(self):
        pass

    def set_name(self, name):
        """Sets user first, last, (optional) middle name."""
        self._name = name

    def get_name(self):
        """Returns first, last, middle name as a tuple"""
        return self.name

    def set_industry(self, industry):
        """Sets user address."""
        self._industry = industry

    def get_industry(self, industry):
        """Returns a company's industry."""
        return self._industry

    def set_description(self, description):
        """Change Company description"""
        self._description = description

    def get_description(self):
        """Returns Company description."""
        return self._description
