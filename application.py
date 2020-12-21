#!/usr/bin/env python

"""application.py: Represents one application opportunity, and its basic information."""


class Application:
    """Creates an opportunity object representing an application/opportunity with an employer."""
    count = 0
    stages = {
        1: 'Applied',
        2: 'Online Assessment Scheduled',
        3: 'Phone Interview Scheduled',
        4: 'Behavioral/Technical Interview Scheduled',
        5: 'Close Application -- Rejection',
        6: 'Close Application -- Duplicate',
        7: 'Offer'
    }

    def __init__(self, application_date, company, job_description):
        """Initializes an Opportunity class"""
        self._application_date = application_date
        self._company = company
        self._job_description = job_description
        self._stage = Application.stages[1]
        Application.count += 1

    def set_application_date(self, application_date):
        self._application_date = application_date

    def get_application_date(self):
        return self._application_date

    def set_company(self, company):
        self._company = company

    def get_company(self):
        return self._company

    def set_stage(self, stage):
        self._stage = stage

    def get_stage(self):
        return self._stage


def display_total_applications():
    print(f'Total Applications: {Application.count}')
