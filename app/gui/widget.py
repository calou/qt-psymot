from PyQt5 import QtWidgets

class MyListWidget(QtWidgets.QListWidget):
    def __init__(self):
        QtWidgets.QListWidget.__init__(self)

    def removeSelection(self):
        for i in range(self.count()):
            item = self.item(i)
            item.setSelected(False)