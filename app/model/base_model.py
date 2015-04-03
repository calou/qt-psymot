# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)

    def fullname(self):
        return self.last_name.upper() + ", " + self.first_name

    def full_name(self):
        return self.fullname()