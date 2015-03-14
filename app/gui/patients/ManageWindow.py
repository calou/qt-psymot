# -*- coding: utf8 -*-

from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import pyqtSlot
from app.gui.design.StylesheetHelper import *

from app.gui.widget import *
from app.gui.base import *
from app.model.Person import *
from app.db.PersonRepository import PersonRepository


class PersonListWidgetItem(QtWidgets.QWidget):
    delete_clicked = QtCore.pyqtSignal(Person, name='deleteClicked')

    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.person = None
        self.item_name_label = QtWidgets.QLabel("")
        self.delete_button = DeleteImageButton()
        self.delete_button.setFixedWidth(16)
        self.delete_button.setToolTip(u"Supprimer le patient")
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.item_name_label)
        self.hbox.addWidget(self.delete_button)
        self.setLayout(self.hbox)

        self.delete_button.clicked.connect(self.handle_delete_button_clicked)


    def set_person(self, person):
        self.person = person
        self.item_name_label.setText(person.fullname())

    def handle_delete_button_clicked(self):
        self.delete_clicked.emit(self.person)

class ManagePatientWindow(Window):
    def __init__(self):
        super(ManagePatientWindow, self).__init__()
        self.back_button = QtWidgets.QPushButton(self)

        self.layout = QtWidgets.QVBoxLayout()
        self.search_input = QtWidgets.QLineEdit(self)
        self.list_widget = QtWidgets.QListWidget(self)

        self.first_name_widget = QtWidgets.QLineEdit()
        self.last_name_widget = QtWidgets.QLineEdit()
        self.birth_date_widget = QtWidgets.QDateEdit()

        self.person_repository = PersonRepository()
        self.current_patient = Person()
        self.patients = []
        self.refresh_patients()
        self.init_ui()

    def init_patient_form(self):
        form_layout = QtWidgets.QFormLayout()

        form_layout.setContentsMargins(20, 10, 0, 0)
        self.birth_date_widget.setDisplayFormat("dd/MM/yyyy")
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)
        form_layout.addRow(u"Prénom", self.first_name_widget)
        form_layout.addRow(u"Nom", self.last_name_widget)
        form_layout.addRow(u"Date de naissance", self.birth_date_widget)
        save_button = QtWidgets.QPushButton(u"Enregistrer")
        save_button.setFixedWidth(120)
        save_button.clicked.connect(self.save_patient)
        form_layout.addWidget(save_button)

        form_widget = DummyWidget(self)
        form_widget.setLayout(form_layout)
        form_widget.setGeometry(240, 140, 630, 410)


    def init_ui(self):
        self.setTitle(u"Gestion des patients")
        new_patient_button = QtWidgets.QPushButton(u"Nouveau patient")
        new_patient_button.setGeometry(120, 770, 560, 3)
        new_patient_button.clicked.connect(self.new_patient)

        self.list_widget.itemClicked.connect(self.item_clicked)
        self.list_widget.setGeometry(30, 130, 200, 350)
        self.redraw_person_list()

        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.setGeometry(30, 90, 200, 32)
        self.search_input.textChanged.connect(self.search_patients)

        self.back_button.setText(u"Retour")
        self.back_button.setGeometry(10, 560, 120, 32)


        form_title = QtWidgets.QLabel(self)
        form_title.setText(u"Informations sur le patients")
        form_title.setGeometry(240, 90, 630, 41)
        form_title.setStyleSheet(MEDIUM_TEXT_STYLESHEET+DARK_COLOR)

        self.init_patient_form()


    def item_clicked(self, item):
        person_widget = self.list_widget.itemWidget(item)
        person_widget.delete_button.show()
        self.set_patient(person_widget.person)

    def refresh_patients(self):
        self.patients = self.person_repository.list()
        self.redraw_person_list()

    def redraw_person_list(self):
        self.list_widget.clear()
        for patient in self.patients:
            item = QtWidgets.QListWidgetItem(self.list_widget)
            item_widget = PersonListWidgetItem()
            item_widget.delete_clicked.connect(self.delete_patient)
            item_widget.set_person(patient)
            item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)

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

    @pyqtSlot(Person)
    def delete_patient(self, patient):
        message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon, 'Supprimer',
            "Etes-vous sûr de vouloir supprimer le patient %s\u00A0?" % patient.fullname(), QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No,self, QtCore.Qt.FramelessWindowHint)
        message_box.setInformativeText("Cette opération est irréversible.")
        message_box.show()
        if message_box.exec() == QMessageBox.Yes:
            self.person_repository.delete(patient)
            self.refresh_patients()
            self.redraw_person_list()

    def new_patient(self):
        self.hide_all_delete_buttons()
        self.list_widget.clearSelection()
        patient = Person()
        self.set_patient(patient)

    def search_patients(self):
        search_value = self.search_input.text()
        if(search_value == ''):
            self.refresh_patients()
        else:
            self.patients = self.person_repository.search(search_value)
        self.redraw_person_list()