import os
import sqlite3
from PyQt5 import QtCore

class Repository():
    def __init__(self):
        self.db_filename = 'app/db/database.db'
        schema_filename = 'app/db/schema.sql'

        db_is_new = not os.path.exists(self.db_filename)

        with sqlite3.connect(self.db_filename) as conn:
            if db_is_new:
                QtCore.qDebug("Creating schema")
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)
            else:
                QtCore.qDebug("Database exists, assume schema does, too.")

    def executeMany(self, script, attrs):
        with sqlite3.connect(self.db_filename, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as conn:
            QtCore.qDebug("DB : %s" % script)
            conn.executemany(script, attrs)

    def execute(self, script, attrs=()):
        with sqlite3.connect(self.db_filename, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as conn:
            QtCore.qDebug("DB : %s" % script)
            cursor = conn.cursor()
            cursor.execute(script, attrs)
            return cursor

