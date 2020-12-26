#!/usr/bin/env python

"""data_storage.py: Program data stored here."""
from sortedcontainers import SortedDict

# These are for debugging if a company successfully gets added and removed
import Classes.company as company


# TODO: test adding/removing application and communication

class MasterData:
    def __init__(self):
        self._companies = SortedDict({})
        self._applications = SortedDict({})
        self._communications = SortedDict({})

    def add_co(self, co, obj):
        self._companies[co] = obj

    def remove_co(self, co):
        self._companies.pop(co)

    def add_app(self, date, obj):
        self._applications[date] = obj

    def remove_app(self, date):
        self._applications.pop(date)

    def add_comm(self, date, obj):
        self._communications[date] = obj

    def remove_comm(self, date):
        self._communications.pop(date)

    def save_data(self):
        # TODO: save state
        pass

    def load_data(self):
        # TODO: load state
        pass

    def display_companies(self):
        if len(self._companies):
            for idx, co in enumerate(self._companies, start=1):
                print(idx, co)
        else:
            print('No companies added... yet!')


if __name__ == '__main__':
    data = MasterData()
    company_obj = company.Company('Apple')
    data.add_co('Apple', company_obj)
    data.display_companies()
    data.remove_co('Apple')
    data.display_companies()
