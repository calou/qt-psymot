from PyQt5 import QtWidgets
from app.gui.ManagePatientsWindow import *

class HomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.start_test_button = QtWidgets.QPushButton(u"Démarrer un test")
        self.manage_patients_button = QtWidgets.QPushButton(u"Gérer les patients")
        self.init_ui()


    def init_ui(self):
        home_layout = QtWidgets.QHBoxLayout()
        menu_box = QtWidgets.QGridLayout()

        menu_box.addWidget(self.start_test_button, 0, 0)
        menu_box.addWidget(self.manage_patients_button, 1, 0)

        home_layout.addLayout(menu_box)
        personFormLayout = QtWidgets.QFormLayout()
        self.firstNameWidget = QtWidgets.QLineEdit()
        self.lastNameWidget = QtWidgets.QLineEdit()
        self.birthDateWidget = QtWidgets.QDateEdit()
        personFormLayout.addRow(u"Prénom", self.firstNameWidget)
        personFormLayout.addRow(u"Nom", self.lastNameWidget)
        personFormLayout.addRow(u"Date de naissance", self.birthDateWidget)

        home_layout.addLayout(personFormLayout)
        self.setLayout(home_layout)
