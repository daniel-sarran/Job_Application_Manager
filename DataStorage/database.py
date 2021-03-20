#!/usr/bin/env python

"""database.py: Program data stored here."""
from sortedcontainers import SortedDict, SortedList
import sqlite3
from datetime import date

# These are for debugging if a company successfully gets added and removed
from Components.company import Company
from Components.application import Application


# https://www.youtube.com/watch?v=girsuXz0yA8&ab_channel=Kite
# https://www.youtube.com/watch?v=pd-0G0MigUA&t=148s&ab_channel=CoreySchafer

# TODO: test adding/removing application and communication

def setup():
    # TODO: change to 3 x DB
    # Define connection and cursor
    connection = sqlite3.connect('jobs.db')
    cursor = connection.cursor()

    # Create companies' table
    cursor.execute("""CREATE TABLE IF NOT EXISTS companies (
                    company TEXT PRIMARY KEY, 
                    sector TEXT,
                    co_desc TEXT
                    )""")

    # Note: no applications column, because we will just check applications table instead
    cursor.execute("""CREATE TABLE IF NOT EXISTS applications (
                    app_date TEXT PRIMARY KEY, 
                    company TEXT, 
                    job_title TEXT, 
                    job_desc TEXT,
                    FOREIGN KEY(company) REFERENCES companies(company)
                    )""")

    # Same applies for applications
    cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
                    act_date TEXT PRIMARY KEY, 
                    app_date TEXT, 
                    interaction TEXT, 
                    status TEXT, 
                    notes TEXT,
                    FOREIGN KEY(app_date) REFERENCES applications(app_date)
                    """)


# def add_company(self, obj_company):
#     self._companies.setdefault(obj_company.get_name().title(), obj_company)

# TODO
def add_company(self, co_obj: Company):
    db = sqlite3.connect("job_application_tracker.db")
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO companies VALUES (?, ?, ?)',
                   (co_obj.get_name(), co_obj.get_industry(), co_obj.get_description()))


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


if __name__ == '__main__':
    setup()
    co = Company('Apple', 'Electronics', 'Leading Phone and Computer maker')
