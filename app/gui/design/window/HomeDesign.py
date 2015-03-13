# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/design/window/home.ui'
#
# Created: Fri Mar 13 23:14:53 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeDesign(object):
    def setupUi(self, HomeDesign):
        HomeDesign.setObjectName("HomeDesign")
        HomeDesign.resize(900, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(HomeDesign)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(HomeDesign)
        QtCore.QMetaObject.connectSlotsByName(HomeDesign)

    def retranslateUi(self, HomeDesign):
        _translate = QtCore.QCoreApplication.translate
        HomeDesign.setWindowTitle(_translate("HomeDesign", "Form"))

