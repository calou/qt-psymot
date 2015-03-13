# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/design/window/homesection.ui'
#
# Created: Sat Mar 14 00:09:35 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeSectionDesign(object):
    def setupUi(self, HomeSectionDesign):
        HomeSectionDesign.setObjectName("HomeSectionDesign")
        HomeSectionDesign.resize(440, 250)
        HomeSectionDesign.setStyleSheet("")
        self.frame = QtWidgets.QFrame(HomeSectionDesign)
        self.frame.setGeometry(QtCore.QRect(0, 0, 441, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.background_widget = QtWidgets.QWidget(self.frame)
        self.background_widget.setGeometry(QtCore.QRect(10, 10, 421, 231))
        self.background_widget.setObjectName("background_widget")
        self.pushButton = QtWidgets.QPushButton(HomeSectionDesign)
        self.pushButton.setGeometry(QtCore.QRect(250, 210, 181, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(HomeSectionDesign)
        QtCore.QMetaObject.connectSlotsByName(HomeSectionDesign)

    def retranslateUi(self, HomeSectionDesign):
        _translate = QtCore.QCoreApplication.translate
        HomeSectionDesign.setWindowTitle(_translate("HomeSectionDesign", "Form"))
        self.pushButton.setText(_translate("HomeSectionDesign", "PushButton"))

