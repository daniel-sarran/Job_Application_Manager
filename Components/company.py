#!/usr/bin/env python

"""company.py: Creates a company profile."""
from sortedcontainers import SortedList

# for debugging only:
# from DataStorage.data_storage import Data


class Company:
    """Creates a Company object representing the company receiving a job application."""

    def __init__(self, name, sector='', description=''):
        """Initializes a Company object."""
        self._name = name
        self._description = description
        self._sector = sector
        self._applications = SortedList([])

    def __repr__(self):
        return f'<Company object: {self._name}>'

    def __str__(self):
        return f'{self._name}'

    def set_name(self, name):
        """Sets company name."""
        self._name = name

    def get_name(self):
        """Returns company name"""
        return self._name

    def set_sector(self, sector):
        """Sets user industry."""
        self._sector = sector

    def get_sector(self, sector):
        """Returns company industry."""
        return self._sector

    def set_description(self, description):
        """Change company description."""
        self._description = description

    def get_description(self):
        """Returns company description."""
        return self._description

    def get_applications(self):
        return self._applications

    def add_application(self, application: object):
        self._applications.add(application)

    # TODO: remove application from company, from database, decrement application count
    def remove_application(self, application: object):
        pass


# if __name__ == '__main__':
#     data = Data()
#     company = 'SalesForce'
#     data.add_co(Company(company, 'Really sweet CRMs, ticker CRM'))
#     data.display_companies()
