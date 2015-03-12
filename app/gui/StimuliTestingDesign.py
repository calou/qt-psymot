# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StimuliTestingDesign.ui'
#
# Created: Wed Mar 11 21:22:52 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextStimuliTestingDesignWidget(object):
    def setupUi(self, TextStimuliTestingDesignWidget):
        TextStimuliTestingDesignWidget.setObjectName("TextStimuliTestingDesignWidget")
        TextStimuliTestingDesignWidget.resize(900, 600)
        self.text_widget = QtWidgets.QLabel(TextStimuliTestingDesignWidget)
        self.text_widget.setGeometry(QtCore.QRect(0, 0, 900, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text_widget.sizePolicy().hasHeightForWidth())
        self.text_widget.setSizePolicy(sizePolicy)
        self.text_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.text_widget.setObjectName("text_widget")
        self.display_result_button = QtWidgets.QPushButton(TextStimuliTestingDesignWidget)
        self.display_result_button.setGeometry(QtCore.QRect(669, 560, 221, 32))
        self.display_result_button.setObjectName("display_result_button")

        self.retranslateUi(TextStimuliTestingDesignWidget)
        QtCore.QMetaObject.connectSlotsByName(TextStimuliTestingDesignWidget)

    def retranslateUi(self, TextStimuliTestingDesignWidget):
        _translate = QtCore.QCoreApplication.translate
        TextStimuliTestingDesignWidget.setWindowTitle(_translate("TextStimuliTestingDesignWidget", "Form"))
        self.text_widget.setText(_translate("TextStimuliTestingDesignWidget", "TextLabel"))
        self.display_result_button.setText(_translate("TextStimuliTestingDesignWidget", "Afficher les résultats"))

