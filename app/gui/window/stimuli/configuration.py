# -*- coding: utf8 -*-
from PyQt4 import QtGui, Qt
from model.stimuli import *
from gui.button import *

from gui.base import *
from db.stimuli_repositories import ConfigurationRepository


class ConfigurationWindow(Window):
    def __init__(self, parent):
        super(ConfigurationWindow, self).__init__(parent)

        self.search_input = QtGui.QLineEdit(self)
        self.list_widget = QtGui.QListWidget(self)
        self.configuration_tabs = ConfigurationTabWidget(self)

        self.repository = ConfigurationRepository()

        self.configurations = []
        self.current_configuration = StimuliConfiguration()
        self.search_patients()
        self.init_ui()
        Window.init(self, parent, "Configuration de tests")

    def init_ui(self):
        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.textChanged.connect(self.search_patients)
        self.list_widget.itemClicked.connect(self.on_item_selected)
        self.configuration_tabs.save_clicked.connect(self.on_save_button_clicked)
        self.update_tabs()

    def on_item_selected(self):
        self.current_configuration = self.configurations[self.list_widget.currentIndex().row()]
        self.update_tabs()

    def update_tabs(self):
        print(self.list_widget.currentIndex().row())
        self.configuration_tabs.update_tabs(self.current_configuration)

    def search_patients(self):
        search_value = self.search_input.text()
        if '' == search_value:
            self.configurations = self.repository.list()
        else:
            self.configurations = self.repository.search(search_value)
        self.redraw_list()

    def redraw_list(self):
        self.list_widget.clear()
        for c in self.configurations:
            self.list_widget.addItem(c.name)

    def resizeEvent(self, ev):
        Window.on_resize(self)
        qrect = Window.get_central_geometry(self)
        self.configuration_tabs.setGeometry(qrect.x() + 310, qrect.y(), qrect.width() - 310, qrect.height())
        self.list_widget.setGeometry(qrect.x(), qrect.y() + 40, 300, qrect.height() - 40)
        self.search_input.setGeometry(qrect.x(), qrect.y(), 300, 32)

    def on_save_button_clicked(self, configuration):
        self.repository.save(configuration)
        self.search_patients()

class ConfigurationFormTab(QtGui.QWidget):
    save_clicked = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ConfigurationFormTab, self).__init__(parent)

        self.name_input = QtGui.QLineEdit()
        self.number_of_stimuli_input = QtGui.QSpinBox()
        self.average_interval_time_input = QtGui.QDoubleSpinBox()
        self.average_interval_time_input.setSingleStep(0.1)
        self.random_interval_time_delta_input = QtGui.QDoubleSpinBox()
        self.random_interval_time_delta_input.setSingleStep(0.05)
        self.display_duration_input = QtGui.QDoubleSpinBox()
        self.display_duration_input.setSingleStep(0.1)

        save_button = QtGui.QPushButton()
        save_button.setText(u"Enregistrer")
        save_button.setFixedWidth(120)
        save_button.clicked.connect(self.on_save_button_clicked)

        form_layout = QtGui.QFormLayout()
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)

        form_layout.addRow(u"Nom", self.name_input)
        form_layout.addRow(u"Nombre de stimuli", self.number_of_stimuli_input)
        form_layout.addRow(u"Intervalle moyen", self.average_interval_time_input)
        form_layout.addRow(u"Composante aléatoire", self.random_interval_time_delta_input)
        form_layout.addRow(u"Durée d'affichage", self.display_duration_input)
        form_layout.addWidget(save_button)

        self.setLayout(form_layout)

        self.configuration = None

    def update_tab(self, configuration):
        self.configuration = configuration
        self.name_input.setText(self.configuration.name)
        self.number_of_stimuli_input.setValue(self.configuration.number_of_stimuli)
        self.average_interval_time_input.setValue(self.configuration.average_interval_time)
        self.random_interval_time_delta_input.setValue(self.configuration.random_interval_time_delta)
        self.display_duration_input.setValue(self.configuration.display_duration)

    def on_save_button_clicked(self):
        self.configuration.name = self.name_input.text()
        self.configuration.number_of_stimuli = self.number_of_stimuli_input.text()
        self.configuration.average_interval_time = self.average_interval_time_input.text()
        self.configuration.random_interval_time_delta = self.random_interval_time_delta_input.text()
        self.configuration.display_duration = self.display_duration_input.text()
        self.save_clicked.emit(self.configuration)

class ConfigurationTabWidget(QtGui.QTabWidget):
    save_clicked = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ConfigurationTabWidget, self).__init__(parent)
        self.configuration = None
        self.form_tab = ConfigurationFormTab()
        self.consigne_input = QtGui.QTextEdit()
        self.init_ui()

    def init_ui(self):
        self.consigne_input.setStyleSheet("border:none;")
        self.addTab(self.form_tab, u"Informations générales")
        self.addTab(self.consigne_input, u"Consigne")
        self.form_tab.save_clicked.connect(self.on_save_button_clicked)

    def update_tabs(self, configuration):
        self.configuration = configuration
        self.form_tab.update_tab(configuration)
        self.consigne_input.setText(configuration.consigne)

    def on_save_button_clicked(self, configuration):
        self.save_clicked.emit(configuration)