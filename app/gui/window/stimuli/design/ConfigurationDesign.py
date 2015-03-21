# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/design/window/testingsetupdesign.ui'
#
# Created: Fri Mar 13 22:49:27 2015
# by: PyQt4 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_TestingSetupDesign(object):
    def setupUi(self, TestingSetupDesign):
        TestingSetupDesign.setObjectName("TestingSetupDesign")
        TestingSetupDesign.resize(900, 600)
        self.patient_select = QtGui.QComboBox(TestingSetupDesign)
        self.patient_select.setGeometry(QtCore.QRect(40, 140, 300, 32))
        self.patient_select.setObjectName("patient_select")
        self.testing_select = QtGui.QComboBox(TestingSetupDesign)
        self.testing_select.setGeometry(QtCore.QRect(390, 140, 300, 32))
        self.testing_select.setObjectName("testing_select")
        self.label = QtGui.QLabel(TestingSetupDesign)
        self.label.setGeometry(QtCore.QRect(40, 100, 191, 31))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(TestingSetupDesign)
        self.label_2.setGeometry(QtCore.QRect(390, 100, 191, 31))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtGui.QSpinBox(TestingSetupDesign)
        self.spinBox.setGeometry(QtCore.QRect(220, 250, 71, 32))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtGui.QLabel(TestingSetupDesign)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 151, 32))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.start_button = QtGui.QPushButton(TestingSetupDesign)
        self.start_button.setGeometry(QtCore.QRect(730, 560, 160, 32))
        self.start_button.setObjectName("start_button")
        self.back_button = QtGui.QPushButton(TestingSetupDesign)
        self.back_button.setGeometry(QtCore.QRect(10, 560, 160, 32))
        self.back_button.setObjectName("back_button")
        self.label_4 = QtGui.QLabel(TestingSetupDesign)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 151, 32))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtGui.QLabel(TestingSetupDesign)
        self.label_6.setGeometry(QtCore.QRect(50, 200, 151, 32))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.consigne = QtGui.QLabel(TestingSetupDesign)
        self.consigne.setGeometry(QtCore.QRect(220, 200, 591, 41))
        self.consigne.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.consigne.setObjectName("consigne")
        self.label_5 = QtGui.QLabel(TestingSetupDesign)
        self.label_5.setGeometry(QtCore.QRect(470, 300, 171, 32))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        self.all_values = QtGui.QTextEdit(TestingSetupDesign)
        self.all_values.setGeometry(QtCore.QRect(220, 290, 231, 211))
        self.all_values.setObjectName("all_values")
        self.valid_values = QtGui.QTextEdit(TestingSetupDesign)
        self.valid_values.setGeometry(QtCore.QRect(660, 290, 231, 211))
        self.valid_values.setObjectName("valid_values")

        self.retranslateUi(TestingSetupDesign)
        QtCore.QMetaObject.connectSlotsByName(TestingSetupDesign)

    def retranslateUi(self, TestingSetupDesign):
        _translate = QtCore.QCoreApplication.translate
        TestingSetupDesign.setWindowTitle(_translate("TestingSetupDesign", "TestingSetupDesign"))
        self.label.setText(_translate("TestingSetupDesign", "Patient"))
        self.label_2.setText(_translate("TestingSetupDesign", "Test"))
        self.label_3.setText(_translate("TestingSetupDesign", "Nombre de stimuli"))
        self.start_button.setText(_translate("TestingSetupDesign", "Démarrer"))
        self.back_button.setText(_translate("TestingSetupDesign", "Retour"))
        self.label_4.setText(_translate("TestingSetupDesign", "Valeurs"))
        self.label_6.setText(_translate("TestingSetupDesign", "Consigne :"))
        self.consigne.setText(_translate("TestingSetupDesign", "consigne_text"))
        self.label_5.setText(_translate("TestingSetupDesign", "Valeurs valides"))

