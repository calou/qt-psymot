# -*- coding: utf8 -*-

from PyQt5 import QtWidgets,QtCore

from app.gui.widget import *
from app.gui.base import *
from app.model.Person import *
from app.db.PersonRepository import PersonRepository


class PersonListWidgetItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.person = None
        self.item_name_label = QtWidgets.QLabel("Name:")
        self.delete_button = DeleteImageButton()
        self.delete_button.setFixedWidth(16)
        self.delete_button.setToolTip(u"Supprimer le patient")
        self.delete_button.hide()
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.item_name_label)
        self.hbox.addWidget(self.delete_button)
        self.setLayout(self.hbox)

    def set_person(self, person):
        self.person = person
        self.item_name_label.setText(person.fullname())


class ManagePatientWindow(Window):
    def __init__(self):
        super(ManagePatientWindow, self).__init__()
        self.back_button = QtWidgets.QPushButton(u"Retour")
        self.setContentsMargins(15, 10, 15, 10)

        self.layout = QtWidgets.QVBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.list_widget = QtWidgets.QListWidget()

        self.first_name_widget = QtWidgets.QLineEdit()
        self.last_name_widget = QtWidgets.QLineEdit()
        self.birth_date_widget = QtWidgets.QDateEdit()

        self.person_repository = PersonRepository()
        self.current_patient = Person()
        self.patients = []
        self.refresh_patients()
        self.init_ui()

    def init_title(self):
        title = self.setTitle(u"Gestion des patients")
        new_patient_button = QtWidgets.QPushButton(u"Nouveau patient")
        new_patient_button.clicked.connect(self.new_patient)
        title_layout = QtWidgets.QHBoxLayout()
        title_layout.addWidget(title, 0, QtCore.Qt.AlignLeft)
        title_layout.addWidget(new_patient_button, 0, QtCore.Qt.AlignRight)
        self.layout.addLayout(title_layout)

    def init_patients_list(self):
        self.list_widget.itemClicked.connect(self.item_clicked)
        self.list_widget.setFixedWidth(300)
        self.redraw_person_list()

    def init_search_input(self):
        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.setFixedWidth(200)
        self.layout.addWidget(self.search_input)
        self.search_input.textChanged.connect(self.search_patients)

    def init_patient_form(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.setContentsMargins(20, 10, 0, 0)
        self.birth_date_widget.setDisplayFormat("dd/MM/yyyy")
        form_title = QtWidgets.QLabel(u"Informations sur le patients")
        form_title.setFont(FontManager.get_title_font())
        form_title.setStyleSheet("font-size:25px;margin-bottom:10px;")
        form_layout.addRow(form_title)
        form_layout.addRow(u"Prénom", self.first_name_widget)
        form_layout.addRow(u"Nom", self.last_name_widget)
        form_layout.addRow(u"Date de naissance", self.birth_date_widget)
        save_button = QtWidgets.QPushButton(u"Enregistrer")
        save_button.setFixedWidth(120)
        save_button.clicked.connect(self.save_patient)
        form_layout.addWidget(save_button)
        return form_layout

    def init_button_layout(self):
        button_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        button_layout.addStretch(0)
        button_layout.addWidget(self.back_button)
        self.layout.addLayout(button_layout)

    def init_ui(self):
        self.init_title()
        self.init_patients_list()
        self.init_search_input()

        form_layout = self.init_patient_form()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.list_widget)
        hbox.addLayout(form_layout)
        self.layout.addLayout(hbox)
        self.init_button_layout()
        self.setLayout(self.layout)

    def hide_all_delete_buttons(self):
        for it in range(self.list_widget.count()):
            self.list_widget.itemWidget(self.list_widget.item(it)).delete_button.hide()

    def item_clicked(self, item):
        self.hide_all_delete_buttons()
        personWidget = self.list_widget.itemWidget(item)
        personWidget.delete_button.show()
        self.set_patient(personWidget.person)

    def refresh_patients(self):
        self.patients = self.person_repository.list()
        self.redraw_person_list()

    def redraw_person_list(self):
        self.list_widget.clear()
        for patient in self.patients:
            item = QtWidgets.QListWidgetItem(self.list_widget)
            item_widget = PersonListWidgetItem()
            item_widget.delete_button.clicked.connect(self.delete_patient)
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

    def delete_patient(self):
        reply = QtWidgets.QMessageBox.question(self, 'Supprimer',
            "Etes-vous sûr de vouloir supprimer ce patient", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.person_repository.delete(self.current_patient)
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