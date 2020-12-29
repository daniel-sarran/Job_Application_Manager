#!/usr/bin/env python

"""dashboard.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import Data
from Components.company import Company
from Components.application import Application
from Components.activity import Activity

WIDTH = 90
PADDING_SIZE = 4
INNER_PADDING_SIZE = 6

padding = ' ' * PADDING_SIZE
inner_padding = ' ' * INNER_PADDING_SIZE


def print_border(fill='*'):
    fill = fill
    border = fill * WIDTH
    print(border)


def greeting():
    print()
    print()
    if Application.count > 1:
        print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(WIDTH))
    elif Application.count == 1:
        print(f'You applied to your first job - keep it up!'.center(WIDTH))
    else:
        print(f'Let\'s get started!'.center(WIDTH))
    print()
    print()


def recent_applications(data_obj):
    apps_list = data_obj.get_applications()
    ending_idx = -4
    if not apps_list:
        return
    print(padding + 'Most recent applications:')
    print(
        inner_padding,
        f'{"APPLIED":<15s}{"POSITION":<15s}     {"COMPANY":<15s}{"APPLICATION STAGE":<30s}'
    )
    if len(apps_list) < abs(ending_idx):
        for app in reversed(apps_list):
            print(inner_padding, app[1])
    else:
        for idx in range(-1, ending_idx, -1):
            print(inner_padding, apps_list[idx][1])
    print()


def upcoming_activities(data_obj):
    sched_list = [app[1] for app in data_obj.get_activities() if app[1].get_status() == 'Scheduled']
    ending_idx = -3
    if not sched_list:
        return
    print(padding + 'Upcoming activities:')
    print(
        inner_padding,
        f'{"DATE":<15s}{"STATUS":<13s}{"TYPE":<10s}{"NOTE":<40s}'
    )
    if len(sched_list) < abs(ending_idx):
        for app in reversed(sched_list):
            print(inner_padding, app)
    else:
        for idx in range(-1, ending_idx, -1):
            print(inner_padding, sched_list[idx])
    print()


def recent_completed_activities(data_obj):
    done_list = [app[1] for app in data_obj.get_activities() if app[1].get_status() == 'Done']
    ending_idx = -3
    if not done_list:
        return
    print(padding + 'Recently completed activities:')
    print(
        inner_padding,
        f'{"DATE":<15s}{"STATUS":<13s}{"TYPE":<10s}{"NOTE":<40s}'
    )

    if len(done_list) < abs(ending_idx):
        for app in reversed(done_list):
            print(inner_padding, app)
    else:
        for idx in range(-1, ending_idx, -1):
            print(inner_padding, done_list[idx])
    print()


def prompt_for_selection():
    print()
    add_new = '(1) Add new...' + padding
    find = '(2) View/Edit/Search...' + padding
    view_all = '(3) List all...' + padding

    print(padding + 'Select an option:')
    print(inner_padding, add_new)
    if Application.count < 1:
        return
    print(inner_padding, find)
    print(inner_padding, view_all)


def display():
    print_border()
    greeting()
    recent_applications(data)
    upcoming_activities(data)
    recent_completed_activities(data)
    print_border()
    prompt_for_selection()
    print()

if __name__ == '__main__':
    data = Data()

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

    communication1 = Activity((2021, 1, 1), 0, 0, 'Send thank you letter to Yasmine & Habib')
    application1.add_act(communication1)
    data.add_act(communication1)

    communication2 = Activity((2020, 12, 22), 0, 1, 'Rejection')
    application2.add_act(communication2)
    data.add_act(communication2)

    communication3 = Activity((2021, 1, 6), 0, 0, 'Follow up w/ Recruiter - said reach out in 2 weeks')
    application1.add_act(communication3)
    data.add_act(communication3)

    communication4 = Activity((2020, 12, 26), 1, 1, 'Sent follow up email')
    application3.add_act(communication4)
    data.add_act(communication4)

    communication5 = Activity((2020, 12, 26), 1, 1, 'Sent another email')
    application3.add_act(communication5)
    data.add_act(communication5)

    communication6 = Activity((2020, 12, 27), 1, 1, 'Rcvd rejection email')
    application3.add_act(communication6)
    data.add_act(communication6)

    display()


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
