# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/design/window/StimuliTestingDesign.ui'
#
# Created: Fri Mar 13 21:02:52 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextStimuliTestingDesignWidget(object):
    def setupUi(self, TextStimuliTestingDesignWidget):
        TextStimuliTestingDesignWidget.setObjectName("TextStimuliTestingDesignWidget")
        TextStimuliTestingDesignWidget.resize(900, 600)
        self.text_widget = QtWidgets.QLabel(TextStimuliTestingDesignWidget)
        self.text_widget.setGeometry(QtCore.QRect(0, 0, 900, 431))
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
        self.consigne = QtWidgets.QLabel(TextStimuliTestingDesignWidget)
        self.consigne.setGeometry(QtCore.QRect(50, 50, 800, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.consigne.sizePolicy().hasHeightForWidth())
        self.consigne.setSizePolicy(sizePolicy)
        self.consigne.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.consigne.setObjectName("consigne")
        self.begin_text = QtWidgets.QLabel(TextStimuliTestingDesignWidget)
        self.begin_text.setGeometry(QtCore.QRect(10, 360, 881, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.begin_text.sizePolicy().hasHeightForWidth())
        self.begin_text.setSizePolicy(sizePolicy)
        self.begin_text.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_text.setObjectName("begin_text")

        self.retranslateUi(TextStimuliTestingDesignWidget)
        QtCore.QMetaObject.connectSlotsByName(TextStimuliTestingDesignWidget)

    def retranslateUi(self, TextStimuliTestingDesignWidget):
        _translate = QtCore.QCoreApplication.translate
        TextStimuliTestingDesignWidget.setWindowTitle(_translate("TextStimuliTestingDesignWidget", "Form"))
        self.text_widget.setText(_translate("TextStimuliTestingDesignWidget", "TextLabel"))
        self.display_result_button.setText(_translate("TextStimuliTestingDesignWidget", "Afficher les résultats"))
        self.consigne.setText(_translate("TextStimuliTestingDesignWidget", "Consigne"))
        self.begin_text.setText(_translate("TextStimuliTestingDesignWidget", "Cliquer pour commencer le test"))

