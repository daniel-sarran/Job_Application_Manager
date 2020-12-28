#!/usr/bin/env python

"""dashboard.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import Data
from Components.company import Company
from Components.application import Application
from Components.communication import Communication

# TODO: make a class that has functions for each menu
# def view_activities(data, n):
#     dashes = '*' * 40
#     print('   ', dashes)
#     for key, val in data.items():
#         print('   ', '{:<10s}{:<30s}'.format(str(key), str(val)))
PADDING = '    '
INNER = '      '
WIDTH = 90


def print_border(fill='*'):
    fill = fill
    border = fill * WIDTH
    print(border)


def greeting():
    print()
    print()
    print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(WIDTH))
    print()
    print()


def recent_applications(data_obj):
    print(PADDING + 'Most recent applications:')
    print(INNER,
          f'{"APPLIED ON":<15s}{"POSITION":<15s}     {"COMPANY":<15s}{"APPLICATION STAGE":<25s}')
    # print(INNER + str(data.get_communications()[-1]))
    apps_list = data_obj.get_applications()
    ending_idx = -4

    # TODO: make print output pretty
    if len(apps_list) < abs(ending_idx):
        for app in reversed(apps_list):
            print(INNER, app[1])
    else:
        for idx in range(-1, ending_idx, -1):
            print(INNER, apps_list[idx][1])
    print()


def upcoming_activities(data_obj):
    print(PADDING + 'Upcoming activities:')
    # print(INNER + str(data.get_communications()[-1]))
    comm_list = data_obj.get_communications()
    ending_idx = -3

    # TODO: make print output pretty
    if len(comm_list) < abs(ending_idx):
        for app in reversed(comm_list):
            print(INNER, app)
    else:
        for idx in range(-1, ending_idx, -1):
            print(INNER, comm_list[idx])
    print()


def recent_completed_activities(data_obj):
    print(PADDING + 'Recently completed activities:')
    # print(INNER + str(data.get_communications()[-1]))
    comm_list = data_obj.get_communications()
    ending_idx = -3

    # TODO: make print output pretty
    if len(comm_list) < abs(ending_idx):
        for app in reversed(comm_list):
            print(INNER, app)
    else:
        for idx in range(-1, ending_idx, -1):
            print(INNER, comm_list[idx])
    print()


def prompt_for_selection():
    add_new = '(1) Add new...' + PADDING
    find = '(2) Find...' + PADDING
    view_all = '(3) View all...' + PADDING

    print(PADDING + 'Select an option:')
    print(INNER, add_new)
    print(INNER, find)
    print(INNER, view_all)


if __name__ == '__main__':
    data = Data()

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

    print_border()
    greeting()
    recent_applications(data)
    upcoming_activities(data)
    recent_completed_activities(data)
    print_border()
    prompt_for_selection()
    print(PADDING, '{:<10s}{:<10s}{:<20s}{:<10s}'.format(application1.get_clean_date(), str(application1.get_company()),
                                                         application1.get_job(), application1.get_stage()))
    # print(''.center(60, '*'))
    # print()
    # print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(60))
    # print()
    # print('     Most recent applications:'.ljust(60))
    # print(f'       {data.get_applications()[-1][1]}')
    # print(f'       {data.get_applications()[-2][1]}')
    # print(f'       {data.get_applications()[-3][1]}')
    #
    # # Need to solve the "only one application per date" problem
    # print()
    # print('     Newest activities:'.ljust(60))
    # print(f'       {data.get_communications()[-1][1]}')
    # print(f'       {data.get_communications()[-2][1]}')
    # print()
    # print('     Select an option:'.ljust(60))
    # print('       1) Add new...\n       2) Find existing...\n       3) View more...'.ljust(60))
    # selection = input()
    # print(f'You chose {selection}')
