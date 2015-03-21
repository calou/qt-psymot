# -*- coding: utf8 -*-
from PyQt4 import QtCore
from utils.PercentageCalculator import PercentageCalculator
import random
import time
from datetime import datetime


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
    def __init__(self, stimulus_value=StimulusValue(""), ts=time.time(), duration=0, valid=False):
        self.id = -1
        self.stimulus_value = stimulus_value
        self.time = ts
        self.duration = duration
        self.effective_time = None
        self.stimulus_responses = []
        self.valid = valid
        self.action_time = None
        self.action_count = 0
        self.correct = False

    def get_duration(self):
        return self.duration

    def is_correct_with_valid_true(self):
        # Si le stimulus est valide et la liste des réponse n'est pas vide...
        return self.valid and self.stimulus_responses != []

    def is_correct_with_valid_false(self):
        # Si le stimulus n'est pas valide et la liste des réponse est vide...
        return (not self.valid) and self.stimulus_responses == []

    def is_correct(self):
        return self.is_correct_with_valid_true() or self.is_correct_with_valid_false()

    def get_response_time_in_ms(self):
        if not self.stimulus_responses:
            return None
        return 1000 * (self.stimulus_responses[0].time - self.effective_time)


class StimulusResponse():
    def __init__(self):
        self.time = time.time()


class StimuliTestingSession():
    def __init__(self):
        self.id = -1
        self.person = None
        self.configuration_name = ""
        self.start_date = None
        self.stimuli = []
        self.patient = None
        self.correct_responses = []
        self.correct_forbidden_responses = []
        self.correct_authorized_responses = []
        self.min_response_time = 99999
        self.max_response_time = 0
        self.average_response_time = 0

    def get_number_of_valid_stimuli(self):
        count = 0
        for stiumulus in self.stimuli:
            if stiumulus.valid:
                count += 1
        return count

    def get_number_of_forbidden_stimuli(self):
        count = 0
        for stiumulus in self.stimuli:
            if not stiumulus.valid:
                count += 1
        return count

    def get_correct_responses_percentage(self):
        return PercentageCalculator.calculate(len(self.correct_responses), len(self.stimuli))

    def get_correct_forbidden_responses_percentage(self):
        return PercentageCalculator.calculate(len(self.correct_forbidden_responses),
                                              self.get_number_of_forbidden_stimuli())

    def get_forbidden_responses_clicked_percentage(self):
        return PercentageCalculator.calculate(
            self.get_number_of_forbidden_stimuli() - len(self.correct_forbidden_responses),
            self.get_number_of_forbidden_stimuli())

    def get_correct_authorized_responses_percentage(self):
        return PercentageCalculator.calculate(len(self.correct_authorized_responses),
                                              self.get_number_of_valid_stimuli())

    def get_authorized_responses_not_clicked_percentage(self):
        return PercentageCalculator.calculate(
            self.get_number_of_valid_stimuli() - len(self.correct_authorized_responses),
            self.get_number_of_valid_stimuli())

    def compute_results(self):
        response_time_sum = 0

        for stimulus in self.stimuli:
            valid = stimulus.is_correct()
            ts = stimulus.get_response_time_in_ms()

            # Si la liste des réponses n'est pas vide ...
            if stimulus.stimulus_responses:
                QtCore.qDebug("%s - %s - %d ms" % (valid, stimulus.stimulus_value.value, ts))
            else:
                QtCore.qDebug("%s - %s - Aucun clic" % (valid, stimulus.stimulus_value.value))
            if stimulus.is_correct():
                self.correct_responses.append(stimulus)
                if stimulus.valid:
                    rt = stimulus.get_response_time_in_ms()
                    response_time_sum += rt
                    if rt < self.min_response_time:
                        self.min_response_time = rt

                    if rt > self.max_response_time:
                        self.max_response_time = rt
                    self.correct_authorized_responses.append(stimulus)

                else:
                    self.correct_forbidden_responses.append(stimulus)

        if not self.correct_authorized_responses:
            self.average_response_time = -1
        else:
            self.average_response_time = response_time_sum / len(self.correct_authorized_responses)


class StimuliTestingConfiguration():
    def __init__(self):
        self.id = -1
        self.name = ""
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

    def generate_testing_session(self):
        testing_session = StimuliTestingSession()
        testing_session.configuration_name = self.name
        testing_session.start_time = datetime.now()
        current_time = 0
        min = self.min_interval_time()
        delta = 2 * self.random_interval_time_delta
        for i in range(self.number_of_stimuli):
            current_time += min + random.randint(0, 100 * delta) / 100
            stimulus_value = random.choice(self.stimuli_values)
            duration = self.get_duration()
            valid = stimulus_value in self.valid_stimuli_values
            stimulus = Stimulus(stimulus_value, current_time, duration, valid)
            testing_session.stimuli.append(stimulus)
        return testing_session