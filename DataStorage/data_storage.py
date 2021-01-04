#!/usr/bin/env python

"""data_storage.py: Program data stored here."""
from sortedcontainers import SortedDict, SortedList
from datetime import date


# These are for debugging if a company successfully gets added and removed
# from Components.company import Company
# from Components.application import Application


# TODO: test adding/removing application and communication

class Data:
    def __init__(self):
        # TODO: change to 3 x DB
        self._companies = SortedDict({})
        self._applications = SortedList()
        self._activities = SortedList()

    def __repr__(self):
        return f'<Data object: companies: {len(self._companies)}, applications: {self._applications}, activities:' \
               f'{self._activities}>'

    def __str__(self):
        return f''

    def add_company(self, obj_company):
        self._companies.setdefault(obj_company.get_name().title(), obj_company)

    def remove_company(self, co_obj):
        # TODO: Need to remove associated applications, and their communications as well
        self._companies.pop(co_obj)

    def find_company(self, name: str):
        name = name.title()
        if name in self._companies:
            return self._companies[name]

    def get_companies(self):
        return self._companies

    def add_application(self, app_obj):
        self._applications.add([app_obj.get_date(), app_obj])

    def remove_applications(self, obj_application):
        self._applications.remove([obj_application.get_date(), obj_application])

    def get_applications(self):
        return self._applications

    def add_activity(self, obj_activity):
        self._activities.add([obj_activity.get_date(), obj_activity])

    def remove_activity(self, obj_activity):
        self._activities.remove([obj_activity.get_date(), obj_activity])

    def get_activities(self):
        return self._activities

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
            print('No applications logged... yet!')

    def display_activities(self):
        if len(self._activities):
            for idx, app in enumerate(self._activities, start=1):
                print(idx, app)
        else:
            print('No activities added... yet!')

# if __name__ == '__main__':
#     data = Data()
#
#     company_obj = Company('Apple')
#     data.add_co(company_obj)
#     application_obj = Application((2020, 12, 25), company_obj, 'SWE')
#     data.add_app(application_obj)
#
#     company_obj2 = Company('Google')
#     data.add_co(company_obj2)
#     application_obj2 = Application((2020, 12, 24), company_obj2, 'SWE')
#     data.add_app(application_obj2)
#
#     data.display_companies()
#     data.display_applications()
