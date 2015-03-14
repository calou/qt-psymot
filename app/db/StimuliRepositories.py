from app.db.Repository import *
from app.model.stimuli import StimulusValue, StimuliTestingConfiguration


class ConfigurationRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def select_many(self, query):
        cursor = self.execute(query)
        testing_configurations = []
        for row in cursor.fetchall():
            testing_configuration = StimuliTestingConfiguration()
            testing_configuration.id, testing_configuration.name, testing_configuration.consigne, testing_configuration.number_of_stimuli, testing_configuration.average_interval_time, testing_configuration.random_interval_time_delta, testing_configuration.display_duration = row
            testing_configurations.append(testing_configuration)
        return testing_configurations

    def list(self):
        query = 'SELECT id, name, consigne, number_of_stimuli, average_interval_time, random_interval_time_delta, display_duration from stimuli_testing_configurations'
        return self.select_many(query)

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


class SessionRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def save(self, session):
        s_query = "INSERT INTO stimuli_testing_sessions (person_id, configuration_name, started_at) VALUES (?, ?, ?)"
        cursor = self.execute(s_query, (session.person.id, session.configuration_name, session.start_date))
        sid = cursor.lastrowid
        session.id = sid

        query = "INSERT INTO stimuli (session_id, string_value, valid, display_time, action_time, action_count) " \
                "VALUES (?, ?, ?, ?, ?,? )"
        attrs = []
        for s in session.stimuli:
            str_value = s.stimulus_value.value
            attrs.append((sid, str_value, s.valid, s.effective_time, s.effective_time, len(s.stimulus_responses)))

        self.executeMany(query, attrs)

