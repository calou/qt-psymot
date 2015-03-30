# -*- coding: utf8 -*-
import codecs
import os
import sqlite3
from PyQt4 import QtCore
from filesystem.FileSystemManager import FileSystemManager
from sqlturk.migration import MigrationTool


class DatabaseManager():
    def __init__(self):
        self.db_filename = FileSystemManager.get_application_data_directory() + 'psychomotriciel.db'
        self.migration_tool = MigrationTool("sqlite:///" + self.db_filename, "db/migrations")
        self.migration_tool.install()

    def get_connection(self):
        return sqlite3.connect(self.db_filename, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def migrate(self):
        self.migration_tool.find_migrations()
        self.migration_tool.run_migrations()


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

