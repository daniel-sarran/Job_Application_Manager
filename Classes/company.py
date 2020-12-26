#!/usr/bin/env python

"""company.py: Creates a company profile."""
from sortedcontainers import SortedList


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
        """Sets company name."""
        self._name = name

    def get_name(self):
        """Returns company name"""
        return self._name

    def set_industry(self, industry):
        """Sets user industry."""
        self._description = industry

    def get_industry(self, industry):
        """Returns company industry."""
        return self._description

    def set_description(self, description):
        """Change company description."""
        self._description = description

    def get_description(self):
        """Returns company description."""
        return self._description

    def get_applications(self):
        return self._applications

# if __name__ == '__main__':
    # company = 'SalesForce'
    # data_storage.companies[company] = Company(company)
    # print(data_storage.companies)
    # company = 'Apple'
    # data_storage.companies[company] = Company(company)
    # print(data_storage.companies[company])
