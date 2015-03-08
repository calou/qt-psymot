from PyQt4 import QtGui

class MyListWidget(QtGui.QListWidget):
    def __init__(self):
        QtGui.QListWidget.__init__(self)

    def removeSelection(self):
        for i in range(self.count()):
            item = self.item(i)
            self.setItemSelected(item, False)