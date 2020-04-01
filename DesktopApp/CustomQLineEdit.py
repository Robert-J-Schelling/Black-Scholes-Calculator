import sys
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QGridLayout,QLabel, QDateEdit,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, Qt
import qdarkstyle
import QGridLayout
from IDs import IDs

class CustomQLineEdit(QLineEdit,IDs):
    def __init__(self, *args, **kwargs):
        isCentered = kwargs.get('isCentered', False)
        isDisabled = kwargs.get('isCentered', False)
        noBorder = kwargs.get('noBorder', False)
        isOrange = kwargs.get('isOrange', False)
        isOnlyReadable = kwargs.get('isOnlyReadable', False)
        self.postfix = kwargs.get('postfix',None)
        self.qGridLayout = kwargs.get('qGridLayout',None)
        ID = kwargs.get('ID', None)
        QLineEdit.__init__(self, *args)
        self.onlyDouble =QDoubleValidator()
        self.setValidator(self.onlyDouble)
        if(isCentered):
            self.setAlignment(Qt.AlignCenter)
        if(isDisabled):
            self.setDisabled(True)
        if(noBorder):
            self.setStyleSheet("CustomQLineEdit { border: none }")
        if(isOrange):
            self.setStyleSheet("color: Orange;")
        if(isOnlyReadable):
            self.setReadOnly(True)
        if(ID != None):
            self.setID(ID)

    # def focusInEvent(self, e):
    #     if(self.ID != None):
    #         self.textChanged.connect(lambda: self.qGridLayout.calculate(self.ID))
    #         super().focusInEvent(e)

    def focusOutEvent(self, e):
        if(self.qGridLayout != None):
            self.qGridLayout.calculate(self.ID)
        super().focusOutEvent(e)
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter or e.key() == 16777220 and self.qGridLayout != None:
            self.qGridLayout.calculate(self.ID)
        else:
            super().keyPressEvent(e)

    # def postfixSetText(self,string):
    #     if(string == None):
    #         self.setText(self.text() + self.postfix)
    #     else:
    #         self.setText(string + self.postfix)
