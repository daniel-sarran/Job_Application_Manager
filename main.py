#!/usr/bin/env python

"""main.py: Main program loop."""

import UI
import data_storage

def new_company(co_name, co_object):
    data_storage.companies[co_name] = co_object

if __name__ == '__main__':
    UI.greeting()

