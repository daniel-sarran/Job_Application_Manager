#!/usr/bin/env python

"""data_storage.py: Program data stored here."""
from sortedcontainers import SortedDict, SortedList

# These are for debugging if a company successfully gets added and removed
# from Components.company import Company
# from Components.application import Application

# import sqlite3
# from Components.company import Company
#
# conn = sqlite3.connect(':memory:')
#
# c = conn.cursor()
#
# c.execute("""CREATE TABLE companies (
#             name text,
#             description text
#             )""")
#
#
# def insert_co(co):
#     with conn:
#         c.execute("INSERT INTO companies VALUES (:name, :description)",
#                   {'name': co_1.get_name(), 'description': co_1.get_description()})
#
#
# def get_co_by_name(co):
#     with conn:
#         c.execute("SELECT * FROM companies WHERE name=:name",
#                   {'name': co_1.get_name()})
#         return c.fetchone()  # return ALL companies with a certain date
#
#
# co_1 = Company('Facebook', 'Social media & advertising company')
# co_2 = Company('Google', 'It\'s Google!')
#
# insert_co(co_1)
# insert_co(co_2)
#
# companies = get_co_by_name('Facebook')
# print(companies)
#
# conn.close()

from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(engine)


class CompanyDB(Base):
    __tablename__ = 'company'

    co_name = Column(String(15), primary_key=True)
    description = Column(String(200))


    class ApplicationDB(CompanyDB):
        __tablename__ = 'application'

        date = Column(Date(), primary_key=True)
        co = Column(String(15), ForeignKey('company.co_name'))
        job_title = Column(String(15))
        job_desc = Column(String(200))
        stage = Column(String(15))


    class ActivityDB(ApplicationDB):
        __tablename__ = 'activity'

        act_date = Column(Date(), primary_key=True)
        act_type = Column(String(25))
        note = Column(String(50))
        status = Column(String(10))
        app_date = Column(String(10), ForeignKey('application.date'))
        app_job = Column(String(15), ForeignKey('application.job_title'))
