#!/usr/bin/env python

"""contacts.py: Creates and stores log of communications and attempts."""

class ContactHistory:
    """Creates a contact history for a user."""

    def __init__(self):
        # contacts = heap - with dates, type, and notes
        contact_type = ('Phone Call Out', 'Phone call in', 'Email sent', 'Email received', 'Face-to-face')

    def __repr__(self):
        pass

    def add_new_contact(self, date, type, message):
        pass

    def get_contact(self, date, time):
        pass

    def edit_contact(self, date, type, message):
        pass