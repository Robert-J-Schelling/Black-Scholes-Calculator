import sys
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QGridLayout,QLabel, QDateEdit,QLineEdit,QComboBox,QToolButton,QTabBar
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, Qt,pyqtSignal
import qdarkstyle
import QGridLayout

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Black Scholes Calculator'
        self.width = 1028
        self.height = 720
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTabWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()

class MyTableWidget(QWidget):
    tab_list = []

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tb = QToolButton()
        self.tb.setText("+")
        self.tabs = QTabWidget()
        self.tb.clicked.connect(self.addTab)
        self.tabs.addTab(QLabel("Add tabs by pressing \"+\""),"")
        self.tabs.setTabEnabled(0, False)
        self.tabs.tabBar().setTabButton(0, QTabBar().RightSide, self.tb)

        self.addTab()

        self.tabs.resize(1028,720)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.removeTab)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def addTab(self):
        self.tab_list.append(QWidget())
        self.index = len(self.tab_list) - 1
        self.tabs.insertTab(self.index,self.tab_list[-1],"Option")
        self.tab_list[-1].layout = QGridLayout.QGridLayout()
        self.tab_list[-1].setLayout(self.tab_list[-1].layout)
        self.tabs.setCurrentIndex(self.index)

    def removeTab(self,index):
        self.tabs.removeTab(index)
        self.tab_list.pop(index)
        self.tabs.setCurrentIndex(index-1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ex = App()
    sys.exit(app.exec_())
