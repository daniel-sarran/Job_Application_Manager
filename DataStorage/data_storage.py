#!/usr/bin/env python

"""data_storage.py: Program data stored here."""
from sortedcontainers import SortedDict, SortedList

# These are for debugging if a company successfully gets added and removed
# from Components.company import Company
# from Components.application import Application


# TODO: test adding/removing application and communication

class Data:
    def __init__(self):
        self._companies = SortedDict({})
        self._applications = SortedList()
        self._communications = SortedList()

    def __repr__(self):
        pass

    def __str__(self):
        return f''

    def add_co(self, obj_company):
        self._companies.setdefault(obj_company.get_name(), obj_company)

    def remove_co(self, co):
        self._companies.pop(co)

    def get_company_by_index(self, index):
        return self._companies.peekitem(index)

    def add_app(self, obj_application):
        # TODO: as it stands now, can only add one application per date
        self._applications.add([obj_application.get_date(), obj_application])

    def remove_app(self, date):
        self._applications.pop(date)

    def get_applications(self):
        return self._applications

    def add_comm(self, obj_communication):
        self._communications.add([obj_communication.get_date(), obj_communication])

    def remove_comm(self, date):
        self._communications.pop(date)

    def get_communications(self):
        return self._communications

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

    def display_applications(self):
        if len(self._applications):
            for idx, app in enumerate(self._applications, start=1):
                print(idx, app)
        else:
            print('No companies added... yet!')


if __name__ == '__main__':
    data = Data()

    company_obj = Company('Apple')
    data.add_co(company_obj)
    application_obj = Application((2020, 12, 25), company_obj, 'SWE')
    data.add_app(application_obj)

    company_obj2 = Company('Google')
    data.add_co(company_obj2)
    application_obj2 = Application((2020, 12, 24), company_obj2, 'SWE')
    data.add_app(application_obj2)

    data.display_companies()
    data.display_applications()