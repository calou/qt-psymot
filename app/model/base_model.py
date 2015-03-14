# -*- coding: utf8 -*-
from datetime import datetime

class Person():
    def __init__(self):
        self.id = -1
        self.first_name = ""
        self.last_name = ""
        self.birth_date = datetime(1990, 1, 1)

    def fullname(self):
        return self.last_name.upper() + ", " +self.first_name

    def full_name(self):
        return self.fullname()