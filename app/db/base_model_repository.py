from sqlalchemy import or_
from db.repository import *
from model.base_model import Person

class PersonRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def list(self):
        session = self.get_session()
        return session.query(Person).order_by(Person.id)


    def search(self, search_value):
        value = "%" + search_value + "%"
        session = self.get_session()
        return session.query(Person).filter(or_(Person.first_name.like(value), Person.last_name.like(value))).order_by(
            Person.id)
