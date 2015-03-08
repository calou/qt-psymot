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
        self.item_name_label = QtGui.QLabel("Name:")

        vert = QtGui.QVBoxLayout()
        vert.addWidget(self.item_name_label)
        self.setLayout(vert)

    def setPerson(self, person):
        self.person = person
        self.item_name_label.setText(person.fullname())



class ManagePatientWidget(QtGui.QWidget):

    def __init__(self):
        super(ManagePatientWidget, self).__init__()
        self.patients = []

        self.initUI()


    def fakeData(self):
        for f,l,d in [("Marie", "Dubois", datetime(1990,12,24)), ("Jacques", "Martin", datetime(1952,7,3)),("Patrick", "Lahaye", datetime(1980,4,9))]:
            person = Person()
            person.firstName = f
            person.lastName = l
            person.birthDate = d
            self.patients.append(person)

    def initUI(self):
        self.managePatientsLayout = QtGui.QHBoxLayout()

        personFormLayout = QtGui.QFormLayout()
        self.redrawPersonList()
        hbox = QtGui.QHBoxLayout()
        self.patientListWidget = QtGui.QListWidget()
        self.patientListWidget.setUpdatesEnabled(True)

        self.fakeData()
        hbox.addWidget(self.patientListWidget)

        self.firstNameWidget = QtGui.QLineEdit()
        self.lastNameWidget = QtGui.QLineEdit()
        self.birthDateWidget = QtGui.QDateEdit()
        self.birthDateWidget.setDisplayFormat("dd/MM/yyyy")
        personFormLayout.addRow(u"Prénom", self.firstNameWidget)
        personFormLayout.addRow(u"Nom", self.lastNameWidget)
        personFormLayout.addRow(u"Date de naissance", self.birthDateWidget)

        saveButton = QtGui.QPushButton(u"Enregistrer")
        saveButton.clicked.connect(self.savePatient)
        personFormLayout.addWidget(saveButton)

        hbox.addLayout(personFormLayout)
        self.managePatientsLayout.addLayout(hbox)

        self.redrawPersonList()

        self.setLayout(self.managePatientsLayout)
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')
        self.show()

    def redrawPersonList(self):

        for patient in self.patients:
            item = QtGui.QListWidgetItem(self.patientListWidget)
            item_widget = PersonListWidgetItem()
            item_widget.setPerson(patient)
            item.setSizeHint(item_widget.sizeHint())
            self.patientListWidget.addItem(item)
            self.patientListWidget.setItemWidget(item, item_widget)



    def savePatient(self):
        patient = Person()
        patient.firstName = self.firstNameWidget.text()
        patient.lastName = self.lastNameWidget.text()
        patient.birthDate = self.birthDateWidget.date()
        self.patients.append(patient)
        self.redrawPersonList()
        print(self.patients)
