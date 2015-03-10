import random

class StimulusValue():
    def __init__(self, name="", value="", content=""):
        self.id = -1
        self.name = name
        if not value:
            self.value = name
        else:
            self.value = value
        self.content = content


class Stimulus():
    def __init__(self, stimulus_value, time, duration):
        self.id = -1
        self.stimulus_value = stimulus_value
        self.time = time
        self.duration = duration
        self.effective_time = None


class StimuliTestSession():
    def __init__(self):
        self.id = -1
        self.stimuli = []
        self.patient = None
        self.start_time = None


class StimuliTestConfiguration():
    def __init__(self):
        self.id = -1
        self.number_of_stimuli = 50
        self.average_interval_time = 5.0
        self.random_interval_time_delta = 2.0
        self.display_duration = 0.8

        self.stimuli_values = []
        self.valid_stimuli_values = []

    def min_interval_time(self):
        return self.average_interval_time - self.random_interval_time_delta

    def max_interval_time(self):
        return self.average_interval_time + self.random_interval_time_delta

    def get_duration(self):
        # Rendre cette durée aléatoire ?
        return self.display_duration

    def generate_test_session(self):
        test_session = StimuliTestSession()
        current_time = 0
        min = self.min_interval_time()
        max = self.max_interval_time()
        for i in range(self.number_of_stimuli):
            current_time += min
            stimulus_value = random.choice(self.stimuli_values)
            duration = self.get_duration()
            stimulus = Stimulus(stimulus_value, current_time, duration)
            test_session.stimuli.append(stimulus)
        return test_session