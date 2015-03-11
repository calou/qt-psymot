# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextStimuliTestingDesignWidget.ui'
#
# Created: Wed Mar 11 07:49:25 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextStimuliTestingDesignWidget(object):
    def setupUi(self, TextStimuliTestingDesignWidget):
        TextStimuliTestingDesignWidget.setObjectName("TextStimuliTestingDesignWidget")
        TextStimuliTestingDesignWidget.resize(400, 300)
        self.text_widget = QtWidgets.QLabel(TextStimuliTestingDesignWidget)
        self.text_widget.setGeometry(QtCore.QRect(140, 120, 200, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text_widget.sizePolicy().hasHeightForWidth())
        self.text_widget.setSizePolicy(sizePolicy)
        self.text_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.text_widget.setObjectName("text_widget")

        self.retranslateUi(TextStimuliTestingDesignWidget)
        QtCore.QMetaObject.connectSlotsByName(TextStimuliTestingDesignWidget)

    def retranslateUi(self, TextStimuliTestingDesignWidget):
        _translate = QtCore.QCoreApplication.translate
        TextStimuliTestingDesignWidget.setWindowTitle(_translate("TextStimuliTestingDesignWidget", "Form"))
        self.text_widget.setText(_translate("TextStimuliTestingDesignWidget", "TextLabel"))

