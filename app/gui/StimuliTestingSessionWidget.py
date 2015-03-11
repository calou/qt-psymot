# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from app.model.stimuli import *
from app.gui.widget import *
from app.gui.base import *
from threading import *
import sched, time
from app.gui.TextStimuliTestingDesignWidget import Ui_TextStimuliTestingDesignWidget

class StimuliTestSessionWidget(QtWidgets.QWidget, Ui_TextStimuliTestingDesignWidget):
    def __init__(self):
        super(StimuliTestSessionWidget, self).__init__()
        self.setupUi(self)

        self.test_configuration = None
        self.test_session = None
        self.current_stimulus_index = 0

        self.init_data()
        self.init_ui()

    def init_data(self):
        self.test_configuration = StimuliTestingConfiguration()
        for i in range(6):
            self.test_configuration.stimuli_values.append(StimulusValue("%d"%(i), "%d"%(i)))
        self.test_session = self.test_configuration.generate_test_session()


    def init_ui(self):
        self.text_widget.setText("")
        self.text_widget.setStyleSheet("font-family:'Source Sans Pro'; font-weight: 600; font-size:96px;")

    def start(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        for stimulus in self.test_session.stimuli:
            Timer(stimulus.time, self.print_value, [stimulus]).start()
            Timer(stimulus.time + stimulus.duration, self.hide_value).start()

    def hide_value(self):
        self.text_widget.setText("")

    def print_value(self, stimulus):
        text = stimulus.stimulus_value.value
        print(text)

        self.text_widget.setText(text)
        stimulus.effective_time = time.time()
