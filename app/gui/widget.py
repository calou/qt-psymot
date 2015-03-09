from PyQt5 import QtWidgets, QtGui


class MyListWidget(QtWidgets.QListWidget):
    def __init__(self):
        QtWidgets.QListWidget.__init__(self)

    def removeSelection(self):
        for i in range(self.count()):
            item = self.item(i)
            item.setSelected(False)


class ImageButton(QtWidgets.QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(ImageButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)


    def sizeHint(self):
        return self.pixmap.size()


class DeleteImageButton(ImageButton):
    def __init__(self, parent=None):
        super(ImageButton, self).__init__(parent)
        self.pixmap = QtGui.QPixmap("assets/delete.png")

