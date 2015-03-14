# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from app.gui.design.StylesheetHelper import *
from app.model.stimuli import *
from app.model.Person import Person
from app.gui.button import *
from app.gui.stimuli.design.ConfigurationDesign import Ui_TestingSetupDesign
from app.db.StimuliRepositories import ConfigurationRepository
from app.db.PersonRepository import PersonRepository

class ConfigurationWidget(QtWidgets.QWidget, Ui_TestingSetupDesign):
    testing_session_started = QtCore.pyqtSignal(StimuliTestingConfiguration, Person)

    def __init__(self, parent=None):
        super(ConfigurationWidget, self).__init__(parent)
        self.setupUi(self)

        self.configurations = []
        self.patients = []

        self.conf_repository = ConfigurationRepository()
        self.person_repository = PersonRepository()

        self.current_patient = None
        self.current_configuration = None

        self.start_button.clicked.connect(self.emit_testing_session_started)

        self.init_ui()

    def init_ui(self):
        self.title.setStyleSheet(BIG_TEXT_STYLESHEET)


    def fetch_data(self):
        self.configurations = self.conf_repository.list()
        self.patients = self.person_repository.list()

        self.init_combos()

    def init_combos(self):
        self.patient_select.clear()
        for p in self.patients:
            self.patient_select.addItem(p.full_name())
        self.on_patient_changed()

        self.testing_select.clear()
        for c in self.configurations:
            self.testing_select.addItem(c.name)
        self.on_conf_changed()
        self.testing_select.activated['QString'].connect(self.on_conf_changed)


    def on_patient_changed(self):
        self.current_patient = self.patients[self.patient_select.currentIndex()]

    def on_conf_changed(self):
        self.current_configuration = self.configurations[self.testing_select.currentIndex()]
        self.conf_repository.fetch_stimuli_values(self.current_configuration)

        self.spinBox.setValue(self.current_configuration.number_of_stimuli)
        self.consigne.setText(self.current_configuration.consigne)

        all_values = []
        valid_values = []
        for stimuli_value in self.current_configuration.stimuli_values:
            color = RED_COLOR
            if stimuli_value in self.current_configuration.valid_stimuli_values:
                color = GREEN_COLOR
            html = "<span style='%s'>%s</span>" % (color, stimuli_value.value)
            all_values.append(html)
        for stimuli_value in self.current_configuration.valid_stimuli_values:
            html = "<span>%s</span>" % (stimuli_value.value)
            valid_values.append(html)

        all_values_html = ", ".join(all_values)
        self.all_values.setText("<html><body>%s</body></html>" % all_values_html)

        valid_values_html = ", ".join(valid_values)
        self.valid_values.setText("<html><body>%s</body></html>" % valid_values_html)


    def emit_testing_session_started(self):
        self.current_configuration.number_of_stimuli = self.spinBox.value()
        self.testing_session_started.emit(self.current_configuration, self.current_patient)

