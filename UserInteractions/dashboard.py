#!/usr/bin/env python

"""dashboard.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import MasterData
from Classes.company import Company
from Classes.application import Application
from Classes.communication import Communication

if __name__ == '__main__':
    data = MasterData()

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

    print(data.display_companies())

    print(''.center(60, '*'))
    print()
    print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(60))
    print()
    print('     Most recent applications:'.ljust(60))
    print(f'       1. {data.get_application_by_index(-1)[1]}')
    print(f'       2. {data.get_application_by_index(-2)[1]}')
    print(f'       2. {data.get_application_by_index(-3)[1]}')

    # Need to solve the "only one application per date" problem
    print()
    print('     Most recent activities:'.ljust(60))
    # print('       1. Apple SWE intern -- 12/20/2020, Received rejection letter - that was fast')
    # print('       2. Blizzard Software Intern -- 12/21/2020, Invited to Online Assessment')
    print()
    print('     Select an option:'.ljust(60))
    print('       1) New application\n       2) Find existing application'.ljust(60))
    selection = input()
    print(f'You chose {selection}')