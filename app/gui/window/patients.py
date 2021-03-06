# -*- coding: utf8 -*-
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QValidator, QRegExpValidator

from gui.base import Window
from PyQt4 import QtGui, QtCore, Qt
from gui.design.StylesheetHelper import *
import datetime

from gui.button import *
from gui.base import *
from model.base_model import *
from db.base_model_repository import PersonRepository


class PersonListWidgetItem(QtGui.QWidget):
    delete_clicked = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.person = None
        self.item_name_label = QtGui.QLabel("")
        self.delete_button = DeleteImageButton()
        self.delete_button.setFixedWidth(16)
        self.delete_button.setToolTip(u"Supprimer le patient")
        self.hbox = QtGui.QHBoxLayout()
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
    def __init__(self, parent=None):
        super(ManagePatientWindow, self).__init__(None)

        self.new_patient_button = QtGui.QPushButton(self)
        self.search_input = QtGui.QLineEdit(self)
        self.list_widget = QtGui.QListWidget(self)
        self.form_widget = QtGui.QWidget(self)
        self.form_title = QtGui.QLabel(self)

        self.first_name_widget = QtGui.QLineEdit()
        self.last_name_widget = QtGui.QLineEdit()
        self.birth_date_widget = QtGui.QDateEdit()

        self.person_repository = PersonRepository()
        self.current_patient = Person()
        self.patients = []
        self.refresh_patients()
        self.init_ui()
        Window.init(self, parent, u"Gestion des patients")

    def init_patient_form(self):
        form_layout = QtGui.QFormLayout(self)
        form_layout.setContentsMargins(20, 10, 0, 0)
        self.birth_date_widget.setDisplayFormat("dd/MM/yyyy")

        """
        regexp = QRegExp("([A-Z])+");
        string_validator= QRegExpValidator(regexp)
        self.first_name_widget.setValidator(string_validator)
        self.last_name_widget.setValidator(string_validator)
        """

        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)
        form_layout.addRow(u"Prénom", self.first_name_widget)
        form_layout.addRow(u"Nom", self.last_name_widget)
        form_layout.addRow(u"Date de naissance", self.birth_date_widget)
        save_button = QtGui.QPushButton(u"Enregistrer")
        save_button.setFixedWidth(150)
        save_button.clicked.connect(self.save_patient)
        form_layout.addWidget(save_button)

        self.form_widget.setLayout(form_layout)


    def init_ui(self):
        self.new_patient_button.setText(u"Nouveau patient")
        self.new_patient_button.clicked.connect(self.new_patient)


        self.list_widget.itemClicked.connect(self.item_clicked)
        self.redraw_person_list()

        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.textChanged.connect(self.search_patients)

        self.form_title.setText(u"Informations sur le patients")
        self.form_title.setStyleSheet(MEDIUM_TEXT_STYLESHEET + DARK_COLOR)

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
            item = QtGui.QListWidgetItem(self.list_widget)
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
        if self.validate():
            self.current_patient.first_name = self.first_name_widget.text()
            self.current_patient.last_name = self.last_name_widget.text()
            self.current_patient.birth_date = self.birth_date_widget.date().toPyDate()
            self.person_repository.save_or_update(self.current_patient)
            self.refresh_patients()
            self.redraw_person_list()

    def validate(self):
        regexp = QRegExp(".+")
        regexp.setCaseSensitivity(False)
        string_validator = QRegExpValidator(regexp)
        state, str, pos = string_validator.validate(self.first_name_widget.text(), 0)
        state2, str, pos = string_validator.validate(self.last_name_widget.text(), 0)

        valid = (state == QtGui.QValidator.Acceptable and state2 == QtGui.QValidator.Acceptable)
        if valid:
            print("Valid", valid)
        else:
            print("invalid", valid)
        return valid

    @QtCore.pyqtSlot(object)
    def delete_patient(self, patient):
        message_box = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, 'Supprimer',
                                        u"Etes-vous sûr de vouloir supprimer le patient %s\u00A0?" % patient.fullname(),
                                        QtGui.QMessageBox.Yes |
                                        QtGui.QMessageBox.No, self, QtCore.Qt.FramelessWindowHint)
        message_box.setInformativeText("Cette opération est irréversible.")
        message_box.show()
        user_response = message_box.exec_()
        if user_response == QtGui.QMessageBox.Yes:
            self.person_repository.delete(patient)
            self.refresh_patients()
            self.redraw_person_list()

    def new_patient(self):
        self.list_widget.clearSelection()
        patient = Person()
        patient.birth_date = datetime.datetime(2000, 1, 1)
        self.set_patient(patient)

    def search_patients(self):
        search_value = self.search_input.text()
        if not search_value:
            self.refresh_patients()
        else:
            self.patients = self.person_repository.search(search_value)
        self.redraw_person_list()

    def resizeEvent(self, ev):
        Window.on_resize(self)
        qrect = Window.get_central_geometry(self)
        self.form_title.setGeometry(qrect.x() + 310, qrect.y(), qrect.width() - 310, 42)
        self.form_widget.setGeometry(qrect.x() + 310, qrect.y() + 42, qrect.width() - 310, qrect.height() - 42)
        self.list_widget.setGeometry(qrect.x(), qrect.y() + 40, 300, qrect.height() - 40)
        self.search_input.setGeometry(qrect.x(), qrect.y(), 300, 32)
        self.new_patient_button.setGeometry(self.get_right_button_geometry())