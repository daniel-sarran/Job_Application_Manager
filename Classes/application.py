#!/usr/bin/env python

"""application.py: Represents one application opportunity, and its basic information."""

from sortedcontainers import SortedList
from Classes.communication import Communication
from Classes.date import Date


class Application(Date):
    """Creates an application object representing a single job application to an employer."""
    # Keeps count of all applications created
    count = 0

    def __init__(self, yr_mo_day_tuple, company, job_title, job_description=''):
        """Initializes an Opportunity class"""
        super().__init__(*yr_mo_day_tuple)
        self._company = company
        self._job = job_title
        self._job_description = job_description
        self._stages = {
            0: 'Applied',
            1: 'Online Assessment',
            2: 'Phone Screen',
            3: 'Interview',
            4: 'Rejection',
            5: 'Offer'
        }
        self._stage = self._stages[0]
        self._communications = SortedList()
        Application.count += 1

    def __repr__(self):
        pass

    def __str__(self):
        result = f'{self._date.strftime("%x")} -- {self._job}  {self._job_description}\n'
        for obj in self._communications:
            result += f'    {obj}\n'
        return result

    def set_date(self, year, month, day):
        self._date = datetime.datetime(year, month, day)

    def get_date(self):
        return self._date.strftime('%x')

    def get_company(self):
        return self._company

    def set_stage(self, stage):
        self._stage = stage

    def get_stage(self):
        return self._stage

    def add_comm(self, comm):
        self._communications.add(comm)

    def remove_comm(self, comm):
        self._communications.pop(comm)


def display_total_applications():
    print(f'Total Applications: {Application.count}')


if __name__ == '__main__':
    app = Application((2020, 12, 20), 'Apple', 'SWE',
                      'Entry level -- required: 15+ yrs C++ and PhD in Computer Science')
    print(app)
    display_total_applications()
    app1 = Application((2020, 12, 22), 'Google', 'SWE',
                       'Entry level -- required: 15+ yrs C++ and PhD in Computer Science')
    print(app1)
    display_total_applications()
    comm1 = Communication((2020, 12, 20), 'Email', 'Invited to Online Assessment', 'Done')
    app1.add_comm(comm1)
    comm2 = Communication((2020, 12, 25), 'Meeting', 'Passed OA, awaiting interview per recruiter', 'Done')
    app1.add_comm(comm2)
    print(app1)
