from app.db.Repository import *
from app.model.base_model import Person
import datetime


class PersonRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def select_many(self, query):
        cursor = self.execute(query)
        people = []
        for row in cursor.fetchall():
            person = Person()
            person.id, person.first_name, person.last_name, birth_date = row
            person.birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            people.append(person)
        return people

    def list(self):
        query = 'SELECT id, first_name, last_name, birth_date from people'
        return self.select_many(query)

    def search(self, search_value):
        value = "'%" + search_value + "%'"
        query = "SELECT id, first_name, last_name, birth_date from people WHERE first_name LIKE " + value + " OR last_name LIKE " + value
        return self.select_many(query)


    def save(self, person):
        query = "INSERT INTO people (first_name, last_name, birth_date) VALUES (?, ?, ?)"
        cursor = self.execute(query, (person.first_name, person.last_name, person.birth_date))
        person.id = cursor.lastrowid

    def update(self, person):
        query = "UPDATE people set first_name=?, last_name=?, birth_date=? WHERE id=? "
        self.execute(query, (person.first_name, person.last_name, person.birth_date, person.id))

    def delete(self, person):
        query = "DELETE FROM people WHERE id=?"
        self.execute(query, (person.id,))
