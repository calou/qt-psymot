# -*- coding: utf8 -*-
import os

from appdirs import *


class FileSystemManager():

    @staticmethod
    def get_application_data_directory():
        data_dir = user_data_dir('Psychomotriciel', 'Psymot')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return data_dir + "/"