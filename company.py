#!/usr/bin/env python

"""company.py: Creates a company profile."""


class Company:
    """Creates a Company object representing the company receiving a job application."""

    def __init__(self, name, description='', priority=''):
        """Initializes a Company object."""
        self._name = name
        self._description = description
        self._priority = priority

    def __repr__(self):
        return f'Company object: "{self._name}'

    def __str__(self):
        return f'{self._name}'

    def set_name(self, name):
        """Sets user first, last, (optional) middle name."""
        self._name = name

    def get_name(self):
        """Returns first, last, middle name as a tuple"""
        return self._name

    def set_industry(self, industry):
        """Sets user address."""
        self._description = industry

    def get_industry(self, industry):
        """Returns a company's industry."""
        return self._description

    def set_description(self, description):
        """Change Company description"""
        self._description = description

    def get_description(self):
        """Returns Company description."""
        return self._description

