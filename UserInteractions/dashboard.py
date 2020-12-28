#!/usr/bin/env python

"""dashboard.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import MasterData
from Classes.company import Company
from Classes.application import Application
from Classes.communication import Communication

# TODO: make a class that has functions for each menu
"""
def view_activities(data, n):

    dashes = '*' * 40
    print('   ', dashes)
    for key, val in data.items():
        print('   ', '{:<10s}{:<30s}'.format(str(key), str(val)))
class Dashboard:
    def __init__(self, width=40, ):
        # self._width =
        
    def recent_applications(self):
        pass
        
    def upcoming_activities(self):
        pass
        
    def recent_completed_activities(self):
        
"""


if __name__ == '__main__':
    data = MasterData()

    print(data.display_applications())
    print(data.display_companies())

    company1 = Company('Apple')
    company2 = Company('Facebook')
    company3 = Company('Google')

    data.add_co(company1)
    data.add_co(company2)
    data.add_co(company3)

    application1 = Application((2020, 12, 1), company1, 'SWE Intern')
    data.add_app(application1)

    application2 = Application((2020, 12, 21), company2, 'Embedded Intern')
    data.add_app(application2)
    application2.set_stage(2)

    application3 = Application((2020, 12, 22), company3, 'Web Dev Intern')
    data.add_app(application3)

    communication1 = Communication((2020, 12, 24), 'Call', 'Follow up w/ Recruiter - said 2 weeks', 'Upcoming')
    application1.add_comm(communication1)
    data.add_comm(communication1)

    communication2 = Communication((2020, 12, 22), 'Email', 'Rejection', 'Done')
    application2.add_comm(communication2)
    data.add_comm(communication2)

    print(''.center(60, '*'))
    print()
    print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(60))
    print()
    print('     Most recent applications:'.ljust(60))
    print(f'       {data.get_applications()[-1][1]}')
    print(f'       {data.get_applications()[-2][1]}')
    print(f'       {data.get_applications()[-3][1]}')

    # Need to solve the "only one application per date" problem
    print()
    print('     Newest activities:'.ljust(60))
    print(f'       {data.get_communications()[-1][1]}')
    print(f'       {data.get_communications()[-2][1]}')
    print()
    print('     Select an option:'.ljust(60))
    print('       1) Add new...\n       2) Find existing...\n       3) View more...'.ljust(60))
    selection = input()
    print(f'You chose {selection}')
