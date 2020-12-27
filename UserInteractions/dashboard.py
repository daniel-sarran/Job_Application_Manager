#!/usr/bin/env python

"""dashboard.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

import DataStorage.data_storage as ds
import Classes.company as co
import Classes.application as app

if __name__ == '__main__':
    data = ds.MasterData()

    company1 = co.Company('Apple')
    data.add_co(company1)

    company2 = co.Company('Facebook')
    data.add_co(company2)

    company3 = co.Company('Google')
    data.add_co(company3)

    application1 = app.Application(company1, 2020, 12, 20, 'SWE Intern')
    data.add_app(application1)

    application2 = app.Application(company2, 2020, 12, 21, 'Embedded Intern')
    data.add_app(application2)

    application3 = app.Application(company3, 2020, 12, 22, 'Web Dev Intern')
    data.add_app(application3)

    print(data.display_companies())

    print(''.center(60))
    print()
    print('Welcome!'.center(60))
    print('You have applied to 67 jobs - nice work!'.center(60))
    # print()
    # print('     Most recent applications:'.ljust(60))
    # print(f'       1. {data.get_application_by_index(-1)}')
    # print(f'       2. {data.get_application_by_index(-2)}')
    # print(f'       3. {data.get_application_by_index(-3)}')
    # print()
    # print('     Most recent activities:'.ljust(60))
    # print('       1. Apple SWE intern -- 12/20/2020, Received rejection letter - that was fast')
    # print('       2. Blizzard Software Intern -- 12/21/2020, Invited to Online Assessment')
