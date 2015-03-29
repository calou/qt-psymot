# -*- coding: utf8 -*-
import codecs
import os
import sqlite3
from PyQt4 import QtCore
from filesystem.FileSystemManager import FileSystemManager

class DatabaseManager():
    def __init__(self):
        self.db_filename = FileSystemManager.get_application_data_directory() + 'psychomotriciel.db'
        self.schema_filename = 'db/schema.sql'

    def get_connection(self):
        return sqlite3.connect(self.db_filename, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def migrate(self):
        db_is_new = not os.path.exists(self.db_filename)
        with sqlite3.connect(self.db_filename) as conn:
            if db_is_new:
                QtCore.qDebug("Creating schema")
                with codecs.open(self.schema_filename, encoding='utf8') as f:
                    schema = f.read()
                conn.executescript(schema)
            else:
                QtCore.qDebug("Database exists, assume schema does, too.")


class Repository():
    def __init__(self):
        self.database_manager = DatabaseManager()

    def executeMany(self, script, attrs):
        with self.database_manager.get_connection() as conn:
            QtCore.qDebug("DB : %s" % script)
            conn.executemany(script, attrs)

    def execute(self, script, attrs=()):
        with self.database_manager.get_connection() as conn:
            QtCore.qDebug("DB : %s" % script)
            cursor = conn.cursor()
            cursor.execute(script, attrs)
            return cursor

