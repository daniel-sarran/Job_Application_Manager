#!/usr/bin/env python

"""main.py: Main program loop, driver code."""

from UserInteractions.menu import Menu
from DataStorage.data_storage import Data

if __name__ == '__main__':
    data1 = Data()
    run = Menu(data1)
    run.main_menu()
