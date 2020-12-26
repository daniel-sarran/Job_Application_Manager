#!/usr/bin/env python

"""application.py: Represents one application opportunity, and its basic information."""

import datetime
import data_storage


class Application:
    """Creates an application object representing a single job application to an employer."""
    count = 0

    def __init__(self, company, year, month, day, job_title, job_description=''):
        """Initializes an Opportunity class"""
        self._company = company
        self._date = datetime.datetime(year, month, day)
        # self._company = obj_company
        self._job = job_title
        self._job_description = job_description
        self._stages = {
            1: 'Applied',
            2: 'Online Assessment Scheduled',
            3: 'Phone Interview Scheduled',
            4: 'Behavioral/Technical Interview Scheduled',
            5: 'Close Application -- Rejection',
            6: 'Close Application -- Duplicate',
            7: 'Offer'
        }
        self._stage = self._stages[1]
        Application.count += 1
        self._communications = []

    def __repr__(self):
        pass

    def __str__(self):
        return f'{self._date.strftime("%x")} -- {self._job}  {self._job_description}'

    def set_application_date(self, year, month, day):
        self._date = datetime.datetime(year, month, day)

    def get_application_date(self):
        return self._date

    def get_company(self):
        return self._company

    def set_stage(self, stage):
        self._stage = stage

    def get_stage(self):
        return self._stage


def display_total_applications():
    print(f'Total Applications: {Application.count}')


if __name__ == '__main__':

    app = Application('Apple', 2020, 12, 20, 'SWE', 'Entry level -- required: 15+ yrs C++ and PhD in Computer Science')
    print(app)

    display_total_applications()
