# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/design/window/testingsetupdesign.ui'
#
# Created: Thu Mar 12 21:45:40 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestingSetupDesign(object):
    def setupUi(self, TestingSetupDesign):
        TestingSetupDesign.setObjectName("TestingSetupDesign")
        TestingSetupDesign.resize(900, 600)
        self.patient_select = QtWidgets.QComboBox(TestingSetupDesign)
        self.patient_select.setGeometry(QtCore.QRect(40, 150, 200, 32))
        self.patient_select.setObjectName("patient_select")
        self.testing_select = QtWidgets.QComboBox(TestingSetupDesign)
        self.testing_select.setGeometry(QtCore.QRect(300, 150, 200, 32))
        self.testing_select.setObjectName("testing_select")
        self.title = QtWidgets.QLabel(TestingSetupDesign)
        self.title.setGeometry(QtCore.QRect(40, 20, 471, 51))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(TestingSetupDesign)
        self.label.setGeometry(QtCore.QRect(40, 110, 191, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TestingSetupDesign)
        self.label_2.setGeometry(QtCore.QRect(300, 110, 191, 31))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(TestingSetupDesign)
        self.spinBox.setGeometry(QtCore.QRect(250, 270, 71, 32))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(TestingSetupDesign)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 191, 32))
        self.label_3.setObjectName("label_3")
        self.start_button = QtWidgets.QPushButton(TestingSetupDesign)
        self.start_button.setGeometry(QtCore.QRect(720, 550, 160, 32))
        self.start_button.setObjectName("start_button")
        self.back_button = QtWidgets.QPushButton(TestingSetupDesign)
        self.back_button.setGeometry(QtCore.QRect(10, 550, 160, 32))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(TestingSetupDesign)
        QtCore.QMetaObject.connectSlotsByName(TestingSetupDesign)

    def retranslateUi(self, TestingSetupDesign):
        _translate = QtCore.QCoreApplication.translate
        TestingSetupDesign.setWindowTitle(_translate("TestingSetupDesign", "TestingSetupDesign"))
        self.title.setText(_translate("TestingSetupDesign", "Choix du test"))
        self.label.setText(_translate("TestingSetupDesign", "Patient"))
        self.label_2.setText(_translate("TestingSetupDesign", "Test"))
        self.label_3.setText(_translate("TestingSetupDesign", "Nombre de stimuli"))
        self.start_button.setText(_translate("TestingSetupDesign", "Démarrer"))
        self.back_button.setText(_translate("TestingSetupDesign", "Retour"))

