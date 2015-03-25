# -*- coding: utf8 -*-
from PyQt4 import QtGui, Qt
from model.stimuli import *
from gui.button import *

from gui.base import *
from db.StimuliRepositories import ConfigurationRepository


class ConfigurationWindow(Window):
    def __init__(self, parent):
        super(ConfigurationWindow, self).__init__(parent)

        self.search_input = QtGui.QLineEdit(self)
        self.list_widget = QtGui.QListWidget(self)
        self.configuration_tabs = ConfigurationTabWidget(self)

        self.repository = ConfigurationRepository()

        self.configurations = []
        self.search_patients()
        self.init_ui()
        Window.init(self, parent, "Configuration de tests")

    def init_ui(self):
        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.textChanged.connect(self.search_patients)
        self.list_widget.itemClicked.connect(self.update_tabs)

    def update_tabs(self):
        print(self.list_widget.currentIndex().row())
        configuration = self.configurations[self.list_widget.currentIndex().row()]
        self.configuration_tabs.update_tabs(configuration)

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


class ConfigurationFormTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ConfigurationFormTab, self).__init__(parent)

        self.name_input = QtGui.QLineEdit()
        self.number_of_stimuli_input = QtGui.QSpinBox()
        self.average_interval_time = QtGui.QDoubleSpinBox()
        self.average_interval_time.setSingleStep(0.1)
        self.random_interval_time_delta_input = QtGui.QDoubleSpinBox()
        self.random_interval_time_delta_input.setSingleStep(0.05)
        self.display_duration = QtGui.QDoubleSpinBox()
        self.display_duration.setSingleStep(0.1)

        form_layout = QtGui.QFormLayout()
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)

        form_layout.addRow(u"Nom", self.name_input)
        form_layout.addRow(u"Nombre de stimuli", self.number_of_stimuli_input)
        form_layout.addRow(u"Intervalle moyen", self.average_interval_time)
        form_layout.addRow(u"Composante aléatoire", self.random_interval_time_delta_input)
        form_layout.addRow(u"Durée d'affichage", self.display_duration)

        self.setLayout(form_layout)

    def update_tab(self, configuration):
        self.name_input.setText(configuration.name)
        self.number_of_stimuli_input.setValue(configuration.number_of_stimuli)
        self.average_interval_time.setValue(configuration.average_interval_time)
        self.random_interval_time_delta_input.setValue(configuration.random_interval_time_delta)
        self.display_duration.setValue(configuration.display_duration)


class ConfigurationTabWidget(QtGui.QTabWidget):
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

    def update_tabs(self, configuration):
        self.configuration = configuration
        self.form_tab.update_tab(configuration)
        self.consigne_input.setText(configuration.consigne)

