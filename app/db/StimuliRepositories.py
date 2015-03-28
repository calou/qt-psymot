from db.Repository import *
from model.stimuli import StimulusValue, StimuliConfiguration, StimuliTestingSession, Stimulus
from model.base_model import Person
import datetime

SELECT_CONFIGURATION_QUERY = 'SELECT id, name, consigne, number_of_stimuli, average_interval_time, random_interval_time_delta, display_duration from stimuli_configurations'

SELECT_SESSION_QUERY = "SELECT s.id, s.configuration_name, s.started_at, p.first_name, p.last_name FROM stimuli_testing_sessions s LEFT JOIN people p on s.person_id = p.id"
SELECT_SESSION_QUERY_ORDER = " ORDER BY s.started_at DESC"


class ConfigurationRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def select_many(self, query, attrs=()):
        cursor = self.execute(query, attrs)
        testing_configurations = []
        for row in cursor.fetchall():
            configuration = StimuliConfiguration()
            configuration.id, configuration.name, configuration.consigne, configuration.number_of_stimuli, configuration.average_interval_time, configuration.random_interval_time_delta, configuration.display_duration = row
            testing_configurations.append(configuration)
        return testing_configurations

    def list(self):
        query = SELECT_CONFIGURATION_QUERY
        return self.select_many(query)

    def list(self):
        query = SELECT_CONFIGURATION_QUERY
        return self.select_many(query)

    def search(self, q):
        query = SELECT_CONFIGURATION_QUERY + " WHERE name like ?"
        return self.select_many(query, (("%%%s%%" % q),))


    def fetch_stimuli_values(self, config):
        config.stimuli_values = []
        config.valid_stimuli_values = []

        query = "SELECT id, string_value, authorized FROM stimuli_values where configuration_id = %d ORDER BY string_value ASC" % config.id
        cursor = self.execute(query)
        for row in cursor.fetchall():
            sv = StimulusValue()
            sv.id, sv.value, authorized = row
            sv.name = sv.value
            config.stimuli_values.append(sv)
            if authorized:
                config.valid_stimuli_values.append(sv)

    def save(self, configuration):
        if configuration.id:
            query = "UPDATE stimuli_configurations SET  name=?, consigne=?, number_of_stimuli=?, average_interval_time=?, random_interval_time_delta=?, display_duration=? WHERE id=?"
            attrs = (configuration.name, configuration.consigne, configuration.number_of_stimuli,
                     configuration.average_interval_time, configuration.random_interval_time_delta,
                     configuration.display_duration, configuration.id)
            self.execute(query, attrs)
        else:
            query = "INSERT INTO stimuli_configurations (name, consigne, number_of_stimuli, average_interval_time, random_interval_time_delta, display_duration) VALUES (?,?,?,?,?,?)"
            attrs = (configuration.name, configuration.consigne, configuration.number_of_stimuli,
                     configuration.average_interval_time, configuration.random_interval_time_delta,
                     configuration.display_duration)
        print(attrs)
        self.execute(query, attrs)


class SessionRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def save(self, session):
        s_query = "INSERT INTO stimuli_testing_sessions (person_id, configuration_name, started_at) VALUES (?, ?, ?)"
        cursor = self.execute(s_query, (session.person.id, session.configuration_name, session.start_date))
        sid = cursor.lastrowid
        session.id = sid

        query = "INSERT INTO stimuli (session_id, string_value, valid, correct, display_time, action_time, action_count) " \
                "VALUES (?, ?, ?, ?, ?, ?, ? )"
        attrs = []
        for s in session.stimuli:
            str_value = s.stimulus_value.value
            action_time = None
            if s.stimulus_responses:
                action_time = s.stimulus_responses[0].time
            attrs.append(
                (sid, str_value, s.valid, s.is_correct(), s.effective_time, action_time, len(s.stimulus_responses)))

        self.executeMany(query, attrs)


    def select_many(self, query, attrs=()):
        cursor = self.execute(query, attrs)
        sessions = []
        for row in cursor.fetchall():
            session = StimuliTestingSession()
            session.person = Person()
            session.id, session.configuration_name, session.start_date, session.person.first_name, session.person.last_name = row
            sessions.append(session)
        return sessions

    def list(self):
        query = SELECT_SESSION_QUERY + SELECT_SESSION_QUERY_ORDER
        return self.select_many(query)

    def search_by_person(self, q):
        search_value = "%" + q + "%"
        query = SELECT_SESSION_QUERY + " WHERE p.first_name like ? or last_name like ?" + SELECT_SESSION_QUERY_ORDER
        return self.select_many(query, (search_value, search_value))


class StimuliRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def select_many(self, query, attrs):
        cursor = self.execute(query, attrs)
        stimuli = []
        for row in cursor.fetchall():
            s = Stimulus()
            s.effective_time, s.action_time, s.string_value, s.action_count, s.valid, s.correct = row
            stimuli.append(s)
        return stimuli

    def get_by_session_id(self, session_id):
        query = "SELECT display_time, action_time, string_value, action_count, valid, correct FROM stimuli WHERE session_id=? ORDER BY display_time"
        return self.select_many(query, (session_id,))