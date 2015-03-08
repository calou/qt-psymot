# -*- coding: utf8 -*-
from datetime import datetime

class Person():
    def __init__(self):
        self.id = 0
        self.firstName = ""
        self.lastName = ""
        self.birthDate = datetime(1990, 1, 1)

    def fullname(self):
        return self.firstName + " " + self.lastName