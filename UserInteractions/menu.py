#!/usr/bin/env python

"""menu.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import Data
from Components.activity import Activity
from Components.company import Company
from Components.application import Application


# TODO: move into class
def _take_input():
    print()
    answer = input().lower()
    return answer


class Menu:
    def __init__(self, data):
        self.data = data
        self.width = 90
        self.padding_size = 3
        self.padding = ' ' * self.padding_size
        self.two_padding = self.padding * 2
        self.three_padding = self.padding * 3

    def _print_border(self, fill='*'):
        fill = fill
        border = fill * self.width
        print(border)

    def _pad(self, text):
        print(self.padding, text)

    def _two_pad(self, text):
        print(self.two_padding, text)

    def _three_pad(self, text):
        print(self.three_padding, text)

    def _greeting(self):
        print()
        if Application.count > 1:
            print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(self.width))
        elif Application.count == 1:
            print(f'You applied to your first job - keep it up!'.center(self.width))
        else:
            print(f'Let\'s get started!'.center(self.width))
        print()

    def _recent_applications(self):
        apps_list = self.data.get_applications()
        ending_idx = -4
        if not apps_list:
            return
        self._pad('Most recent applications:')
        self._two_pad(f'{"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
        if len(apps_list) < abs(ending_idx):
            for app in reversed(apps_list):
                self._two_pad(app[1])
        else:
            for idx in range(-1, ending_idx, -1):
                self._two_pad(apps_list[idx][1])
        print()

    def _upcoming_activities(self):
        sched_list = [app[1] for app in self.data.get_activities() if app[1].get_status() == 'Scheduled']
        ending_idx = -3
        if not sched_list:
            return
        self._pad('Upcoming activities:')
        self._two_pad(f'{"DATE":<15s}{"STATUS":<13s}{"TYPE":<10s}{"NOTE":<40s}')
        if len(sched_list) < abs(ending_idx):
            for app in reversed(sched_list):
                self._two_pad(app)
        else:
            for idx in range(-1, ending_idx, -1):
                self._two_pad(sched_list[idx])
        print()

    def _recent_completed_activities(self):
        done_list = [app[1] for app in self.data.get_activities() if app[1].get_status() == 'Done']
        ending_idx = -3
        if not done_list:
            return
        self._pad('Recently completed activities:')
        self._two_pad(f'{"DATE":<15s}{"STATUS":<13s}{"TYPE":<10s}{"NOTE":<40s}')
        if len(done_list) < abs(ending_idx):
            for app in reversed(done_list):
                self._two_pad(app)
        else:
            for idx in range(-1, ending_idx, -1):
                self._two_pad(done_list[idx])
        print()

    def home_menu(self):
        add_new = '[N] New company'
        find = '[S] Search...'
        view_all = '[V] View All...'
        tutorial = '[H] Help'
        quick_reject = '[R] Quick Reject'
        quick_advance = '[A] Quick Advance'

        self._pad('Menu:')
        print()
        if Application.count < 1:
            self._two_pad(add_new)
            return

        col_1 = max(len(add_new), len(find)) + 3 * self.padding_size
        col_2 = max(len(quick_reject), len(quick_advance)) + 3 * self.padding_size
        col_3 = max(len(view_all), len(tutorial)) + 3 * self.padding_size

        self._two_pad(f'{add_new:<{col_1}}{quick_reject:<{col_2}}{view_all:<{col_3}}')
        self._two_pad(f'{find:<{col_1}}{quick_advance:<{col_2}}{tutorial:<{col_3}}')

    def view_company_menu(self, company):
        edit = '[E] Edit details'
        view_app = '[#] Select application'
        new_app = '[N] New application'
        home = '[H] Home'

        company_apps = company.get_applications()
        self._pad('Menu:')
        print()
        if len(company_apps) < 1:
            self._two_pad(f'{new_app}')
        else:
            self._two_pad(f'{new_app}{self.two_padding}{view_app}{self.two_padding}{edit}')
            self._two_pad(f'{home}')

        while True:
            choice = _take_input()
            if choice == 'e':
                self.edit_company_details(company)
                break
            elif choice in list(map(str, range(0, len(company_apps)))):
                index = int(choice) - 1
                self.view_application(company_apps[index])
                break
            elif choice == 'n':
                self.build_application()
                break
            elif choice == 'h':
                self.main_menu()
                break
            else:
                print('Invalid selection, try again.')

    def quick_reject_menu(self, company: Company):
        select_app = '(#) Select application'
        home = '[H] Home'
        self._pad('Menu:')
        if len(company.get_applications()) < 1:
            self._two_pad(f'No applications on file for {company} (press any key to continue).')
            _take_input()
            self.main_menu()
        else:
            self._two_pad(f'{select_app}{self.two_padding}{home}')
        company_apps = company.get_applications()
        while True:
            choice = _take_input()
            if choice in list(map(str, range(0, len(company_apps) + 1))):
                index = int(choice) - 1
                company_apps[index].set_stage(4)
                self.reject_confirmation(company_apps[index])
                self.main_menu()
                break
            elif choice == 'h':
                self.main_menu()
                break
            else:
                print('Invalid selection, try again.')
        pass

    # TODO: incomplete
    def quick_advance_menu(self, company: Company):
        pass

    # TODO: incomplete
    def edit_company_details_menu(self, company: Company):
        pass

    # TODO: incomplete
    def edit_application_details_menu(self, application: Application):
        pass

    # TODO: incomplete
    def edit_activity_details_menu(self, activity: Activity):
        pass

    def view_company(self, company: Company, fork='view'):
        self._print_border()
        print()
        self._pad('>> View Company Details <<')
        print()
        self._two_pad(f'Company:         {company.get_name()}')
        self._two_pad(f'Description:     {company.get_description()}')
        if len(company.get_applications()) > 0:
            print()
            self._three_pad(f'#  {"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
            for idx, app in enumerate(reversed(company.get_applications()), start=1):
                self._three_pad(f'{idx}  {app}')
        print()
        self._print_border()
        print()
        if fork == 'view':
            self.view_company_menu(company)
        elif fork == 'quick reject':
            self.quick_reject_menu(company)
        elif fork == 'quick advance':
            self.quick_advance_menu(company)

    def view_application(self, application: Application, fork='view'):
        self._print_border()
        print()
        self._pad('Application Details:')
        print()
        self._two_pad(f'Company:         {application.get_company().get_name()}')
        self._two_pad(f'Position:        {application.get_job()}')
        self._two_pad(f'Applied on:      {application.get_clean_date()}')
        self._two_pad(f'Description:     {application.get_job_description()}')
        print()
        self._print_border()
        if fork == 'view':
            pass
        elif fork == 'quick reject':
            pass
        else:  # fork == 'quick advance'
            pass

    # TODO: incomplete
    def view_activity(self, activity: Activity):
        pass

    # TODO: incomplete
    def build_company(self, company_name: str):
        pass

    # TODO: incomplete
    def build_application(self, company: str):
        pass

    # TODO: incomplete
    def build_activity_(self, application: Application):
        pass

    def new_company(self):
        print()
        self._pad('>> New Company <<')
        print()
        company_name = self._prompt_company_name()
        found = self.data.find_company(company_name)
        if found:  # company is already on file
            print()
            self._two_pad(f'It looks like {found} is already on file (press any key to continue).')
            _take_input()
            self.view_company(found, 'view')
        else:  # company is not on file
            self.build_company(company_name)

    def search_not_found(self, company_name):
        print()
        self._two_pad(f'"{company_name}" not found.')
        print()
        self._pad('Menu:')
        new = '[N] New search'
        home = '[H] Home'
        self._two_pad(f'{new}')
        self._two_pad(f'{home}')
        while True:
            choice = _take_input()
            if choice == 'n':
                self.search_company()
                break
            elif choice == 'm':
                self.main_menu()
                break
            else:
                self._pad('Invalid selection, try again.')

    def _prompt_company_name(self):
        self._two_pad('Enter the company name.')
        return _take_input().title()

    def search_company(self, fork='view'):
        print()
        self._pad('>> Search existing company <<')
        print()
        company_name = self._prompt_company_name()
        found = self.data.find_company(company_name)
        if not found:  # company is already on file
            self.search_not_found(company_name)
        elif found and fork == 'quick reject':
            self.view_company(found, 'quick reject')
        else:
            self.view_company(found, 'view')

    # TODO: incomplete
    def view_all(self):
        pass

    # TODO: incomplete
    def help_page(self):
        pass

    def main_menu(self):
        self._print_border()
        self._greeting()
        self._recent_applications()
        self._upcoming_activities()
        self._recent_completed_activities()
        self._print_border()
        print()
        self.home_menu()

        prompts = {
            'new company': 'n',
            'search existing': 's',
            'quick reject': 'r',
            'quick advance': 'a',
            'view all': 'l',
            'help': 'h'
        }

        while True:
            choice = _take_input()
            if choice == prompts['new company']:
                self.new_company()
                break
            elif choice == prompts['search existing']:
                self.search_company()
                break
            elif choice == prompts['quick reject']:
                self.search_company('quick reject')
                break
            elif choice == prompts['quick advance']:
                self.search_company('quick advance')
                break
            elif choice == prompts['view all']:
                self.view_all()
                break
            elif choice == prompts['help']:
                self.view_help()
                break
            else:
                self._pad('Invalid selection, try again.')

    def new_company_review_and_submit(self, company, description):
        self._print_border()
        print()
        self._pad('Review & submit:')
        print()
        self._pad(f'>> New company <<')
        self._two_pad(f'Company:      {company}')
        self._two_pad(f'Description:  {description}')
        print()
        self._two_pad('(1) Submit')
        self._two_pad('(2) Cancel')

    def edit_company_details(self, company: Company):
        self._print_border()
        print()
        self._pad('>> Edit Company Details <<')
        print()
        self._two_pad(f'Company:     [1] {company.get_name()}')
        self._two_pad(f'Description: [2] {company.get_description()}')
        if len(company.get_applications()) > 0:
            print()
            self._three_pad(f'#  {"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
            for idx, app in enumerate(reversed(company.get_applications()), start=1):
                self._three_pad(f'{idx}  {app}')
        print()
        self._print_border()
        print()
        self.edit_company_details_menu(company)

    # TODO: incomplete
    def edit_application_details(self, application: Application):
        pass

    # TODO: incomplete
    def edit_activity_details(self, activity: Activity):
        pass

    def reject_confirmation(self, application: Application):
        self._print_border()
        print()
        self._pad('Application Updated:')
        print()
        self._two_pad(f'{"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
        self._two_pad(f'{application}')
        print()
        self._three_pad('Every "no" gets you one step closer to a "YES"!')
        print()
        self._two_pad('Press any key to continue.')
        _take_input()

    def advance_confirmation(self, application: Application):
        self._print_border()
        print()
        self._pad('Application Updated:')
        print()
        self._two_pad(f'{"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
        self._two_pad(f'{application}')
        print()
        self._three_pad('High five!!!')
        print()
        self._two_pad('Press any key to continue.')
        _take_input()


if __name__ == '__main__':
    data1 = Data()

    company1 = Company('Apple')
    company2 = Company('Facebook')
    company3 = Company('Google')

    data1.add_co(company1)
    data1.add_co(company2)
    data1.add_co(company3)

    application1 = Application((2020, 12, 1), company1, 'SWE Intern')
    data1.add_app(application1)
    company1.add_application(application1)

    application2 = Application((2020, 12, 21), company2, 'Embedded Intern')
    data1.add_app(application2)
    application2.set_stage(2)
    company2.add_application(application2)

    application3 = Application((2020, 12, 22), company3, 'Web Dev Intern')
    data1.add_app(application3)

    communication1 = Activity((2021, 1, 1), 0, 0, 'Send thank you letter to Yasmine & Habib')
    application1.add_act(communication1)
    data1.add_act(communication1)

    communication2 = Activity((2020, 12, 22), 0, 1, 'Rejection')
    application2.add_act(communication2)
    data1.add_act(communication2)

    communication3 = Activity((2021, 1, 6), 0, 0, 'Follow up w/ Recruiter - said reach out in 2 weeks')
    application1.add_act(communication3)
    data1.add_act(communication3)

    communication4 = Activity((2020, 12, 26), 1, 1, 'Sent follow up email')
    application3.add_act(communication4)
    data1.add_act(communication4)

    communication5 = Activity((2020, 12, 26), 1, 1,
                              'Sent another email, can\'t believe they didn\'t get back to me')
    application3.add_act(communication5)
    data1.add_act(communication5)

    communication6 = Activity((2020, 12, 27), 1, 1, 'Rcvd rejection email')
    application3.add_act(communication6)
    data1.add_act(communication6)

    # ************************Start dashboard menu

    run = Menu(data1)
    run.main_menu()
