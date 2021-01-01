#!/usr/bin/env python

"""menu.py: The main "jump-off" point for the program."""

# Sample dashboard - run to view in console - this whole script is playground at this point

from DataStorage.data_storage import Data
from Components.activity import Activity
from Components.company import Company
from Components.application import Application


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

    def greeting(self):
        print()
        if Application.count > 1:
            print(f'You\'ve already applied to {Application.count} jobs - nice work!'.center(self.width))
        elif Application.count == 1:
            print(f'You applied to your first job - keep it up!'.center(self.width))
        else:
            print(f'Let\'s get started!'.center(self.width))
        print()

    def recent_applications(self):
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

    def upcoming_activities(self):
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

    def recent_completed_activities(self):
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

    def dashboard_selections(self):
        add_new = '(N)ew company'
        find = '(S)earch existing'
        view_all = '(L)ist All...'
        tutorial = '(H)elp'
        quick_reject = 'Quick (R)eject'
        quick_advance = 'Quick (A)dvance'

        self._pad('Menu:')
        if Application.count < 1:
            self._two_pad(add_new)
            return
        self._two_pad(f'{add_new:<25}{quick_reject:<25}{view_all:<25}')
        self._two_pad(f'{find:<25}{quick_advance:<25}{tutorial:<25}')

    def view_company(self, company: Company):
        self._print_border()
        print()
        self._pad('Company profile:')
        print()
        self._two_pad(f'Company:      {company.get_name()}')
        self._two_pad(f'Description:  {company.get_description()}')
        if len(company.get_applications()) > 0:
            self._two_pad(f'Applications:')
            print()
            self._three_pad(f'{"APPLIED":<15s}{"POSITION":<20s}{"COMPANY":<15s}{"APPLICATION STAGE":<30s}')
            for app in reversed(company.get_applications()):
                self._three_pad(app)
        print()
        self._print_border()
        print()

        # view company selections
        edit = '(E)dit details'
        view_app = '(S)elect application'
        new_app = '(N)ew application'

        self._pad('Menu:')
        if len(company.get_applications()) < 1:
            self._two_pad(f'{new_app:<25}{edit:<25}')
        else:
            self._two_pad(f'{new_app:<25}{view_app:<25}{edit:<25}')
        _take_input()

    def view_application(self, application: Application):
        pass

    def view_activity(self, activity: Activity):
        pass

    def build_company(self, company_name: str):
        pass

    def build_application(self, company: str):
        pass

    def build_activity_(self, application: Application):
        pass

    def new_company(self):
        print()
        self._pad('>>New Company<<')
        print()
        company_name = self._prompt_company_name()
        found = data1.find_company(company_name)
        if found:  # company is already on file
            print()
            self._two_pad(f'It looks like {found} is already on file (press Enter to continue).')
            _take_input()
            self.view_company(found)
        else:  # company is not on file
            self.build_company(company_name)

    def search_not_found(self, company_name):
        print()
        self._two_pad(f'"{company_name}" not found.')
        print()
        self._pad('Menu:')
        new = '(N)ew search'
        main = '(M)ain Menu'
        self._two_pad(f'{new:<25}{main:<25}')
        while True:
            choice = _take_input()
            if choice == 'n':
                self.search_existing()
                break
            elif choice == 'm':
                self.main_menu()
                break
            else:
                self._pad('Invalid selection, try again.')

    def search_existing(self):
        print()
        self._pad('>>Search existing company<<')
        print()
        company_name = self._prompt_company_name()
        found = data1.find_company(company_name)
        if not found:  # company is already on file
            self.search_not_found(company_name)
        else:
            self.view_company(found)

    def quick_reject(self):
        pass

    def quick_advance(self):
        pass

    def view_all(self):
        pass

    def view_help(self):
        pass

    def main_menu(self):
        self._print_border()
        self.greeting()
        self.recent_applications()
        self.upcoming_activities()
        self.recent_completed_activities()
        self._print_border()
        print()
        self.dashboard_selections()

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
                self.search_existing()
                break
            elif choice == prompts['quick reject']:
                self.quick_reject()
                break
            elif choice == prompts['quick advance']:
                self.quick_advance()
                break
            elif choice == prompts['view all']:
                self.view_all()
                break
            elif choice == prompts['help']:
                self.view_help()
                break
            else:
                self.pad('Invalid selection, try again.')

    def _prompt_company_name(self):
        self._two_pad('Enter the company name.')
        return _take_input().title()

    def company_review_and_submit(self, company, description):
        self._print_border()
        print()
        self._pad('Review & submit:')
        print()
        self._pad(f'-New company...')
        self._two_pad(f'Company:      {company}')
        self._two_pad(f'Description:  {description}')
        print()
        self._two_pad('(1) Submit')
        self._two_pad('(2) Cancel')

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
    company2.add_application(application1)

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

