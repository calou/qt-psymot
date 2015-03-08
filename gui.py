# -*- coding: utf8 -*-

from PyQt4 import QtGui, QtCore
from model import *


class ApplicationHome(QtGui.QWidget):
    def __init__(self):
        super(ApplicationHome, self).__init__()
        self.initUI()

    def initUI(self):
        self.drawHome()

    def drawHome(self):
        self.homeLayout = QtGui.QHBoxLayout()
        leftBox = QtGui.QGridLayout()
        startTestButton = QtGui.QPushButton(u"Démarrer un test")
        managePatientsButton = QtGui.QPushButton(u"Gérer les patients")
        managePatientsButton.clicked.connect(self.managePatientsButtonClicked)

        leftBox.addWidget(startTestButton, 0, 0)
        leftBox.addWidget(managePatientsButton, 1, 0)

        self.homeLayout.addLayout(leftBox)
        personFormLayout = QtGui.QFormLayout()
        self.firstNameWidget = QtGui.QLineEdit()
        self.lastNameWidget = QtGui.QLineEdit()
        self.birthDateWidget = QtGui.QDateEdit()
        personFormLayout.addRow(u"Prénom", self.firstNameWidget)
        personFormLayout.addRow(u"Nom", self.lastNameWidget)
        personFormLayout.addRow(u"Date de naissance", self.birthDateWidget)

        self.homeLayout.addLayout(personFormLayout)

        self.setLayout(self.homeLayout)

        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')
        self.show()


class PersonListWidgetItem(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.person = None
        self.item_name_label = QtGui.QLabel("Name:")

        vert = QtGui.QVBoxLayout()
        vert.addWidget(self.item_name_label)
        self.setLayout(vert)

    def set_person(self, person):
        self.person = person
        self.item_name_label.setText(person.fullname())


class PersonListWidget(QtGui.QListWidget):
    def __init__(self):
        QtGui.QListWidget.__init__(self)
        self.itemClicked.connect(self.item_click)

    def item_click(self, item):
        personWidget = self.itemWidget(item)
        person = personWidget.person
        print self.parent()
        self.parent().first_name_widget.setText(person.firstName)
        self.parent().last_name_widget.setText(person.lastName)
        self.parent().birth_date_widget.setDate(person.birthDate)



class ManagePatientWidget(QtGui.QWidget):
    def __init__(self):
        super(ManagePatientWidget, self).__init__()
        self.patients = []

        self.manage_patients_layout = QtGui.QHBoxLayout()
        self.patient_list_widget = PersonListWidget()
        self.first_name_widget = QtGui.QLineEdit()
        self.last_name_widget = QtGui.QLineEdit()
        self.birth_date_widget = QtGui.QDateEdit()

        self.initUI()


    def fakeData(self):
        for f, l, d in [("Marie", "Dubois", datetime(1990, 12, 24)), ("Jacques", "Martin", datetime(1952, 7, 3)),
                        ("Patrick", "Lahaye", datetime(1980, 4, 9))]:
            person = Person()
            person.firstName = f
            person.lastName = l
            person.birthDate = d
            self.patients.append(person)

    def initUI(self):
        person_form_layout = QtGui.QFormLayout()
        self.redraw_person_list()
        hbox = QtGui.QHBoxLayout()

        self.fakeData()
        hbox.addWidget(self.patient_list_widget)

        self.birth_date_widget.setDisplayFormat("dd/MM/yyyy")
        person_form_layout.addRow(u"Prénom", self.first_name_widget)
        person_form_layout.addRow(u"Nom", self.last_name_widget)
        person_form_layout.addRow(u"Date de naissance", self.birth_date_widget)

        save_button = QtGui.QPushButton(u"Enregistrer")
        save_button.clicked.connect(self.save_patient)
        person_form_layout.addWidget(save_button)

        hbox.addLayout(person_form_layout)
        self.manage_patients_layout.addLayout(hbox)

        self.setLayout(self.manage_patients_layout)
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.redraw_person_list()
        self.show()

    def redraw_person_list(self):
        self.patient_list_widget.clear()
        for patient in self.patients:
            item = QtGui.QListWidgetItem(self.patient_list_widget)
            item_widget = PersonListWidgetItem()
            item_widget.set_person(patient)
            item.setSizeHint(item_widget.sizeHint())
            self.patient_list_widget.addItem(item)
            self.patient_list_widget.setItemWidget(item, item_widget)


    def save_patient(self):
        patient = Person()
        patient.firstName = self.first_name_widget.text()
        patient.lastName = self.last_name_widget.text()
        patient.birthDate = self.birth_date_widget.date()
        self.patients.append(patient)
        self.redraw_person_list()

