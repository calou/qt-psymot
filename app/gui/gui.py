# -*- coding: utf8 -*-

from PyQt5 import QtCore, QtWidgets

from app.gui.MyWidgets import *
from app.gui.base import Window
from app.model.Person import *
from app.db.PersonRepository import PersonRepository


class ApplicationHome(QtWidgets.QWidget):
    def __init__(self):
        super(ApplicationHome, self).__init__()
        self.initUI()

    def initUI(self):
        self.drawHome()

    def drawHome(self):
        self.homeLayout = QtWidgets.QHBoxLayout()
        leftBox = QtWidgets.QGridLayout()
        startTestButton = QtWidgets.QPushButton(u"Démarrer un test")
        managePatientsButton = QtWidgets.QPushButton(u"Gérer les patients")
        managePatientsButton.clicked.connect(self.managePatientsButtonClicked)

        leftBox.addWidget(startTestButton, 0, 0)
        leftBox.addWidget(managePatientsButton, 1, 0)

        self.homeLayout.addLayout(leftBox)
        personFormLayout = QtWidgets.QFormLayout()
        self.firstNameWidget = QtWidgets.QLineEdit()
        self.lastNameWidget = QtWidgets.QLineEdit()
        self.birthDateWidget = QtWidgets.QDateEdit()
        personFormLayout.addRow(u"Prénom", self.firstNameWidget)
        personFormLayout.addRow(u"Nom", self.lastNameWidget)
        personFormLayout.addRow(u"Date de naissance", self.birthDateWidget)

        self.homeLayout.addLayout(personFormLayout)

        self.setLayout(self.homeLayout)

        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')
        self.show()


class PersonListWidgetItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.person = None
        self.item_name_label = QtWidgets.QLabel("Name:")

        vert = QtWidgets.QVBoxLayout()
        vert.addWidget(self.item_name_label)
        self.setLayout(vert)

    def set_person(self, person):
        self.person = person
        self.item_name_label.setText(person.fullname())


class ManagePatientWindow(Window):
    def refresh_patients(self):
        self.patients = self.person_repository.list()

    def __init__(self):
        super(ManagePatientWindow, self).__init__()
        self.patients = []

        self.manage_patients_layout = QtWidgets.QVBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.patient_list_widget = MyListWidget()
        self.first_name_widget = QtWidgets.QLineEdit()
        self.last_name_widget = QtWidgets.QLineEdit()
        self.birth_date_widget = QtWidgets.QDateEdit()

        self.person_repository = PersonRepository()
        self.refresh_patients()
        self.initUI()

    def item_click(self, item):
        personWidget = self.patient_list_widget.itemWidget(item)
        self.set_patient(personWidget.person)

    def initUI(self):
        title = self.setTitle(u"Gestion des patients")

        self.manage_patients_layout.addWidget(title)

        self.patient_list_widget.itemClicked.connect(self.item_click)
        person_form_layout = QtWidgets.QFormLayout()
        self.redraw_person_list()
        hbox = QtWidgets.QHBoxLayout()

        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.setFixedWidth(200)
        self.manage_patients_layout.addWidget(self.search_input)
        self.search_input.textChanged.connect(self.search_patients)

        hbox.addWidget(self.patient_list_widget)

        self.birth_date_widget.setDisplayFormat("dd/MM/yyyy")

        person_form_layout.addRow(u"Prénom", self.first_name_widget)
        person_form_layout.addRow(u"Nom", self.last_name_widget)
        person_form_layout.addRow(u"Date de naissance", self.birth_date_widget)

        save_button = QtWidgets.QPushButton(u"Enregistrer")
        save_button.clicked.connect(self.save_patient)
        new_patient_button = QtWidgets.QPushButton(u"Nouveau patient")
        new_patient_button.clicked.connect(self.new_patient)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(new_patient_button)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(person_form_layout)
        vbox.addLayout(button_layout)

        hbox.addLayout(vbox)
        self.manage_patients_layout.addLayout(hbox)

        self.setLayout(self.manage_patients_layout)
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.redraw_person_list()
        self.new_patient()
        self.show()

    def redraw_person_list(self):
        self.patient_list_widget.clear()
        for patient in self.patients:
            item = QtWidgets.QListWidgetItem(self.patient_list_widget)
            item_widget = PersonListWidgetItem()
            item_widget.set_person(patient)
            item.setSizeHint(item_widget.sizeHint())
            self.patient_list_widget.addItem(item)
            self.patient_list_widget.setItemWidget(item, item_widget)

    def set_patient(self, patient):
        self.current_patient = patient
        self.first_name_widget.setText(patient.first_name)
        self.last_name_widget.setText(patient.last_name)
        q_date = QtCore.QDate(patient.birth_date.year, patient.birth_date.month, patient.birth_date.day)
        self.birth_date_widget.setDate(q_date)

    def save_patient(self):
        self.current_patient.first_name = self.first_name_widget.text()
        self.current_patient.last_name = self.last_name_widget.text()
        self.current_patient.birth_date = self.birth_date_widget.date().toPyDate()
        if (self.current_patient.id >= 0):
            self.person_repository.update(self.current_patient)
        else:
            self.person_repository.save(self.current_patient)
        self.refresh_patients()
        self.redraw_person_list()

    def new_patient(self):
        self.patient_list_widget.removeSelection()
        patient = Person()
        self.set_patient(patient)

    def search_patients(self):
        search_value = self.search_input.text()
        print(search_value)
        if(search_value == ''):
            self.refresh_patients()
        else:
            self.patients = self.person_repository.search(search_value)
        self.redraw_person_list()