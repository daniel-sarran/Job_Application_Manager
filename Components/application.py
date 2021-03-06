#!/usr/bin/env python

"""application.py: Represents one application opportunity, and its basic information."""

from sortedcontainers import SortedList
from Components.activity import Activity
from Components.date import Date


# TODO: stage change should monitor date of stage change

class Application(Date):
    """Creates an application object representing a single job application to an employer."""
    # Keeps count of all applications created
    count = 0

    def __init__(self, yr_mo_day_tuple, obj_company, job_title, job_description=''):
        """Initializes an Opportunity class"""
        super().__init__(*yr_mo_day_tuple)
        self._obj_company = obj_company
        self._job = job_title
        self._job_description = job_description
        self._stages = {
            0: 'Applied - awaiting response',
            1: 'Online Assessment - Scheduled',
            2: 'Phone Screen - Scheduled',
            3: 'Interview - Scheduled',
            4: 'Rejection',
            5: 'Offer'
        }
        self._stage = self._stages[0]
        # TODO: change activities to save into DB
        self._activities = SortedList()
        Application.count += 1

    def __repr__(self):
        return f'<Application object: {self._job} @ {self._obj_company} on {self.get_clean_date()}>'

    def __str__(self):
        return f'{self.get_clean_date():<15s}{self.get_job():<20s}{str(self.get_company()):<15s}{self.get_stage():<25s}'

    def get_job(self):
        return self._job

    def set_job(self, job):
        self._job = job

    def get_job_description(self):
        return self._job_description

    def set_job_description(self, description):
        self._job_description = description

    def get_company(self):
        return self._obj_company

    def set_stage(self, stage):
        if stage in self._stages:
            self._stage = self._stages[stage]
        else:
            raise ValueError(f'Stages are: {self._stages}')

    def advance_stage(self):
        if self._stage in [0, 1, 2]:
            self._stage += 1
        elif self._stage == 3:
            self._stage = 5
        else:
            return

    def get_stage(self):
        return self._stage

    def add_activity(self, comm):
        self._activities.add(comm)

    def remove_activity(self, comm):
        self._activities.remove(comm)

    def get_activities(self):
        return self._activities


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
    comm1 = Activity((2020, 12, 20), 'Email', 'Invited to Online Assessment', 'Done')
    app1.add_activity(comm1)
    comm2 = Activity((2020, 12, 25), 'Meeting', 'Passed OA, awaiting interview per recruiter', 'Done')
    app1.add_activity(comm2)
    print(app1)
    app1.set_stage(0)
