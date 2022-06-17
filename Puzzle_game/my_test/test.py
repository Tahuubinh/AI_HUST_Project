from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.setupUi()

    def setupUi(self):
        self.setMinimumSize(QtCore.QSize(330, 280))
        self.setMaximumSize(QtCore.QSize(330, 280))

        self.centralwidget = QWidget()


        # self.pButton_0 = QPushButton(self.centralwidget)
        # self.pButton_0.setGeometry(QtCore.QRect(10, 200, 51, 41))
        # self.pButton_0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.pButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pButton_0.setGeometry(QtCore.QRect(10, 200, 51, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pButton_0.setFont(font)
        self.pButton_0.setObjectName("pushButton_1")

        self.setCentralWidget(self.centralwidget)
        

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Simple Calculator"))
        self.setToolTip(_translate("MainWindow", "Simple Calculator"))
        self.pButton_0.setToolTip(_translate("MainWindow", "0"))
        self.pButton_0.setText(_translate("MainWindow", "0"))
        self.pButton_0.clicked.connect(lambda: print("hello"))

    def keyPressEvent(self, e):
        print(e.key())

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()

    sys.exit(app.exec_())