#!/usr/bin/env python

"""company.py: Creates a company profile."""
from sortedcontainers import SortedList
import data_storage
from application import Application


class Company:
    """Creates a Company object representing the company receiving a job application."""

    def __init__(self, name, description='', priority=''):
        """Initializes a Company object."""
        self._name = name
        self._description = description
        self._priority = priority
        self._applications = SortedList([])

    def __repr__(self):
        return f'<Company object: {self._name}>'

    def __str__(self):
        lines = []
        for i in range(0, len(self._description), 60):
            lines.append(self._description[i:i + 60])
        return f'Company:\n"{self._name}"\n\nDescription:\n' + "\n".join(lines)

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

    # def new_application(self, yr, mo, day, job, desc):
    #     app = Application(yr, mo, day, job, desc)
    #     data_storage.applications[self._name] = self
    #     self._applications = data_storage.applications[self._name]

    def get_applications(self):
        return self._applications


# if __name__ == '__main__':
    # company = 'SalesForce'
    # data_storage.companies[company] = Company(company)
    # print(data_storage.companies)
    # company = 'Apple'
    # data_storage.companies[company] = Company(company)
    # print(data_storage.companies[company])
