# -*- coding: utf8 -*-
import codecs
import os
import sqlite3
from PyQt4 import QtCore
from filesystem.FileSystemManager import FileSystemManager
from sqlturk.migration import MigrationTool
from sqlalchemy.orm import sessionmaker

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

    def create_session(self):
        engine = self.migration_tool.engine
        Session = sessionmaker(bind=engine)
        return Session()

class Repository():
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.current_session = None

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

    def create_session(self):
        return self.database_manager.create_session()

    #TODO : améliorer la gestion de la session
    def get_session(self):
        if not self.current_session:
            self.current_session = self.create_session()
        return self.current_session

    def save(self, model):
        session = self.get_session()
        session.add(model)
        session.commit()

    def update(self, model):
        session = self.get_session()
        session.update(model)
        session.commit()

    def save_or_update(self, model):
        if model.id:
            self.update(model)
        else:
            self.save(model)

    def delete(self, model):
        session = self.get_session()
        session.delete(model)
        session.commit()