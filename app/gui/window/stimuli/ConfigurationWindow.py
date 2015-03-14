# -*- coding: utf8 -*-

from app.gui.base import Window
from app.gui.design.StylesheetHelper import *
from app.gui.window.stimuli.TestingWindow import TestingWidget
from app.gui.button import *
from app.gui.window.stimuli.design.ConfigurationDesign import Ui_TestingSetupDesign
from app.db.StimuliRepositories import ConfigurationRepository
from app.db.PersonRepository import PersonRepository

class ConfigurationWindow(Window, Ui_TestingSetupDesign):

    def __init__(self, parent=None):
        super(ConfigurationWindow, self).__init__(parent)
        self.setupUi(self)
        self.root_widget = parent
        self.configurations = []
        self.patients = []

        self.conf_repository = ConfigurationRepository()
        self.person_repository = PersonRepository()

        self.current_patient = None
        self.current_configuration = None

        self.start_button.clicked.connect(self.start_testing)

        Window.init(self, parent, u"Définition du test")


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


    def start_testing(self):
        self.current_configuration.number_of_stimuli = self.spinBox.value()
        widget = TestingWidget(self.root_widget, self.current_configuration, self.current_patient)
        self.root_widget.replaceWindow(widget)

