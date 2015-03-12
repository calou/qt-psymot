from app.db.DatabaseConnector import DatabaseConnector
from app.model.stimuli import StimulusValue, StimuliTestingConfiguration


class StimuliTestingConfigurationRepository():
    def __init__(self):
        self.database_connector = DatabaseConnector()

    def select_many(self, query):
        cursor = self.database_connector.execute(query)
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

        query = "SELECT id, string_value, authorized from stimuli_values where configuration_id = %d" % config.id
        cursor = self.database_connector.execute(query)
        for row in cursor.fetchall():
            sv = StimulusValue()
            sv.id, sv.value, authorized = row
            sv.name = sv.value
            config.stimuli_values.append(sv)
            if authorized:
                config.valid_stimuli_values.append(sv)