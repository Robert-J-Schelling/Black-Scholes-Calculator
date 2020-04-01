import sys
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QGridLayout,QLabel, QDateEdit,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, Qt
import qdarkstyle
import QGridLayout
from IDs import IDs
class CustomQComboBox(QComboBox,IDs):
    def __init__(self, *args, **kwargs):
        isOrange = kwargs.get('isOrange', False)
        self.qGridLayout = kwargs.get('qGridLayout',None)
        ID = kwargs.get('ID', None)
        QComboBox.__init__(self, *args)
        if(isOrange):
            self.setStyleSheet("color: Orange;")
        if(ID != None):
            self.setID(ID)

    def focusInEvent(self, e):
        if(self.ID != None):
            self.currentIndexChanged.connect(lambda: self.qGridLayout.calculate(self.ID))
            super().focusInEvent(e)

    def focusOutEvent(self, e):
        if(self.qGridLayout != None):
            self.qGridLayout.calculate(self.ID)
        super().focusOutEvent(e)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter or e.key() == 16777220 and self.qGridLayout != None:
            self.qGridLayout.calculate(self.ID)
        else:
            super().keyPressEvent(e)
