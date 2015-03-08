import os
import sqlite3

from app.model.Person import *


class DatabaseConnector():
    def __init__(self):
        self.db_filename = 'app/db/database.db'
        schema_filename = 'app/db/schema.sql'

        db_is_new = not os.path.exists(self.db_filename)

        with sqlite3.connect(self.db_filename) as conn:
            if db_is_new:
                print 'Creating schema'
                with open(schema_filename, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)
            else:
                print 'Database exists, assume schema does, too.'

    def executeUpdate(self, script):
        with sqlite3.connect(self.db_filename) as conn:
            print("DB : %s" % script)
            conn.executescript(script)

    def execute(self, script):
        with sqlite3.connect(self.db_filename) as conn:
            print("DB : %s" % script)
            cursor = conn.cursor()
            cursor.execute(script)
            return cursor

class PersonRepository():
    def __init__(self):
        self.database_connector = DatabaseConnector()

    def list(self):
        cursor = self.database_connector.execute("SELECT id, first_name, last_name, birth_date from people")

        people = []
        for row in cursor.fetchall():
            person = Person()
            person.id, person.first_name, person.last_name, person.birth_date = row
            people.append(person)
        return people

    def save(self, person):
        query = "INSERT INTO people (first_name, last_name, birth_date) VALUES ('%s', '%s', '%s')" % (person.first_name, person.last_name, person.birth_date)
        self.database_connector.executeUpdate(query)

    def update(self, person):
        query = "UPDATE people set first_name='%s', last_name='%s', birth_date='%s' WHERE id=%s " % (person.first_name, person.last_name, person.birth_date, person.id)
        self.database_connector.executeUpdate(query)