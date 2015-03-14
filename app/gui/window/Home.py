# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from app.gui.design.window.HomeDesign import *
from app.gui.window.HomeSection import *
from app.model.stimuli import *


class Home(QtWidgets.QWidget, Ui_HomeDesign):
    go_to_testing = QtCore.pyqtSignal()
    go_to_patients = QtCore.pyqtSignal()

    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        testing_section = HomeSection("Démarrer un test", "assets/images/people.svg")
        testing_section.pushButton.clicked.connect(self.emit_go_to_testing)

        self.gridLayout.addWidget(testing_section, 0, 0)

        patients_section = HomeSection("Gérer les patients", "assets/images/people.svg")
        patients_section.pushButton.clicked.connect(self.emit_go_to_patients)
        self.gridLayout.addWidget(patients_section, 0, 1)


    def emit_go_to_testing(self):
        self.go_to_testing.emit()

    def emit_go_to_patients(self):
        self.go_to_patients.emit()