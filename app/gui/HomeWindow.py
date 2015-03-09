from PyQt5 import QtWidgets, QtCore
from app.gui.ManagePatientsWindow import *


class HomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.start_test_button = QtWidgets.QPushButton(u"Démarrer un test")
        self.manage_patients_button = QtWidgets.QPushButton(u"Gérer les patients")
        self.init_ui()


    def init_ui(self):
        home_layout = QtWidgets.QHBoxLayout()

        menu_box_widget = QtWidgets.QWidget(self)
        menu_box_widget.setGeometry(QtCore.QRect(10, 10, 130, 60))
        menu_box = QtWidgets.QVBoxLayout(menu_box_widget)
        menu_box.setContentsMargins(0, 0, 0, 0)

        menu_box.addWidget(self.start_test_button)
        menu_box.addWidget(self.manage_patients_button)

        home_layout.addLayout(menu_box)
        self.setLayout(home_layout)
