from app.db.DatabaseConnector import DatabaseConnector
from app.model.Person import Person

__author__ = 'calou'


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
        cursor = self.database_connector.execute(query)
        person.id = cursor.lastrowid

    def update(self, person):
        query = "UPDATE people set first_name='%s', last_name='%s', birth_date='%s' WHERE id=%s " % (person.first_name, person.last_name, person.birth_date, person.id)
        self.database_connector.executeUpdate(query)