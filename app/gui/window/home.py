# -*- coding: utf8 -*-
from PyQt4 import QtGui, QtSvg, Qt

from model.stimuli import *
from gui.window.stimuli.details import DetailsWindow
from gui.window.stimuli.configuration import ConfigurationWindow
from gui.window.patients import ManagePatientWindow
from gui.window.stimuli.setup import SetUpWindow


class Home(QtGui.QWidget):
    go_to_testing = QtCore.pyqtSignal()
    go_to_patients = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.root_widget = parent
        self.gridLayout = QtGui.QGridLayout()
        self.init_ui()

    def init_ui(self):
        testing_section = HomeSection(["Démarrer un test", "Consulter un test", "Configurer"],
                                      "assets/images/checklist.svg")
        testing_section.push_buttons[0].clicked.connect(self.go_to_testing)
        testing_section.push_buttons[1].clicked.connect(self.go_to_testing_details)
        testing_section.push_buttons[2].clicked.connect(self.go_to_configuration)
        self.gridLayout.addWidget(testing_section, 0, 0)

        patients_section = HomeSection(["Gérer les patients"], "assets/images/people.svg")
        patients_section.push_buttons[0].clicked.connect(self.go_to_patients)
        self.gridLayout.addWidget(patients_section, 0, 1)

        shape_section = HomeSection(["Démarrer un test"], "assets/images/jigsaw.svg")
        shape_section.push_buttons[0].clicked.connect(self.go_to_patients)
        self.gridLayout.addWidget(shape_section, 1, 0)


        self.setLayout(self.gridLayout)

    def go_to_testing(self):
        widget = SetUpWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)

    def go_to_patients(self):
        widget = ManagePatientWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)

    def go_to_configuration(self):
        widget = ConfigurationWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)


    def go_to_testing_details(self):
        widget = DetailsWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)


class HomeSection(QtGui.QWidget):
    def __init__(self, button_texts, background_image):
        super(HomeSection, self).__init__()
        self.background_image = background_image

        self.setMinimumSize(440, 250)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.background_widget = QtSvg.QSvgWidget(self)
        self.background_widget.load(background_image)

        self.push_buttons = []
        button_layout = QtGui.QVBoxLayout()
        for i in range(len(button_texts)):
            button = QtGui.QPushButton(self)
            button.setText(button_texts[i])
            self.push_buttons.append(button)
            button_layout.addWidget(button, 1)


    def resizeEvent(self, ev):
        w = self.width()
        h = self.height()

        for i in range(len(self.push_buttons)):
            button = self.push_buttons[i]
            button.setGeometry(Qt.QRect(w - 230, h - (45 + i * 35), 220, 32))

        m = min(w, h)
        self.background_widget.setGeometry(Qt.QRect((w - m) / 2, (h - m) / 2, m, m))