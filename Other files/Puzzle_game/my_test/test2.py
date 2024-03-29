import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Direction(IntEnum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3 

class Ui_Form(QWidget):
    def __init__(self):
        #super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.num_row = 2
        self.gltMain = QGridLayout()
        # self.gltMain.setSpacing(int(720 / self.num_row))
        #self.initUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.test_method()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1030, 783)
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 50, 720, 720))
        self.widget.setObjectName("widget")
        self.widget.setLayout(self.gltMain)
        self.gltMain.setSpacing(20)
        self.onInit()
        # Set layout.
        self.widget.setLayout(self.gltMain)
        # Set window title.
        #self.widget.setWindowTitle('N-puzzle Game.')
        # Set window background color.
        self.widget.setStyleSheet("background-color:gray;")

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(730, 50, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 140, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 230, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 320, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 410, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(730, 500, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 590, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(730, 680, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.labelCombobox = QtWidgets.QLabel(Form)
        self.labelCombobox.setGeometry(QtCore.QRect(20, 10, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCombobox.setFont(font)
        self.labelCombobox.setObjectName("labelCombobox")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(196, 12, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.resetBtn = QtWidgets.QPushButton(Form)
        self.resetBtn.setGeometry(QtCore.QRect(830, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resetBtn.setFont(font)
        self.resetBtn.setObjectName("resetBtn")
        self.time_1 = QtWidgets.QLabel(Form)
        self.time_1.setGeometry(QtCore.QRect(730, 90, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_1.setFont(font)
        self.time_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_1.setWordWrap(True)
        self.time_1.setObjectName("time_1")
        self.num_of_steps_1 = QtWidgets.QLabel(Form)
        self.num_of_steps_1.setGeometry(QtCore.QRect(730, 110, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_1.setFont(font)
        self.num_of_steps_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_1.setWordWrap(True)
        self.num_of_steps_1.setObjectName("num_of_steps_1")
        self.time_value_1 = QtWidgets.QLabel(Form)
        self.time_value_1.setGeometry(QtCore.QRect(870, 90, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_1.setFont(font)
        self.time_value_1.setText("")
        self.time_value_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_1.setWordWrap(True)
        self.time_value_1.setObjectName("time_value_1")
        self.num_of_steps_value_1 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_1.setGeometry(QtCore.QRect(870, 110, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_1.setFont(font)
        self.num_of_steps_value_1.setText("")
        self.num_of_steps_value_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_1.setWordWrap(True)
        self.num_of_steps_value_1.setObjectName("num_of_steps_value_1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(730, 80, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(730, 121, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(730, 88, 3, 40))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(1010, 90, 3, 40))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(730, 178, 3, 40))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(1010, 180, 3, 40))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(730, 170, 281, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.num_of_steps_2 = QtWidgets.QLabel(Form)
        self.num_of_steps_2.setGeometry(QtCore.QRect(730, 200, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_2.setFont(font)
        self.num_of_steps_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_2.setWordWrap(True)
        self.num_of_steps_2.setObjectName("num_of_steps_2")
        self.time_2 = QtWidgets.QLabel(Form)
        self.time_2.setGeometry(QtCore.QRect(730, 180, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_2.setFont(font)
        self.time_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_2.setWordWrap(True)
        self.time_2.setObjectName("time_2")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(730, 211, 281, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.time_value_2 = QtWidgets.QLabel(Form)
        self.time_value_2.setGeometry(QtCore.QRect(870, 180, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_2.setFont(font)
        self.time_value_2.setText("")
        self.time_value_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_2.setWordWrap(True)
        self.time_value_2.setObjectName("time_value_2")
        self.num_of_steps_value_2 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_2.setGeometry(QtCore.QRect(870, 200, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_2.setFont(font)
        self.num_of_steps_value_2.setText("")
        self.num_of_steps_value_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_2.setWordWrap(True)
        self.num_of_steps_value_2.setObjectName("num_of_steps_value_2")
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(730, 268, 3, 40))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(1010, 270, 3, 40))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Form)
        self.line_11.setGeometry(QtCore.QRect(730, 260, 281, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.num_of_steps_3 = QtWidgets.QLabel(Form)
        self.num_of_steps_3.setGeometry(QtCore.QRect(730, 290, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_3.setFont(font)
        self.num_of_steps_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_3.setWordWrap(True)
        self.num_of_steps_3.setObjectName("num_of_steps_3")
        self.time_3 = QtWidgets.QLabel(Form)
        self.time_3.setGeometry(QtCore.QRect(730, 270, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_3.setFont(font)
        self.time_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_3.setWordWrap(True)
        self.time_3.setObjectName("time_3")
        self.line_12 = QtWidgets.QFrame(Form)
        self.line_12.setGeometry(QtCore.QRect(730, 301, 281, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.time_value_3 = QtWidgets.QLabel(Form)
        self.time_value_3.setGeometry(QtCore.QRect(870, 270, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_3.setFont(font)
        self.time_value_3.setText("")
        self.time_value_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_3.setWordWrap(True)
        self.time_value_3.setObjectName("time_value_3")
        self.num_of_steps_value_3 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_3.setGeometry(QtCore.QRect(870, 290, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_3.setFont(font)
        self.num_of_steps_value_3.setText("")
        self.num_of_steps_value_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_3.setWordWrap(True)
        self.num_of_steps_value_3.setObjectName("num_of_steps_value_3")
        self.line_13 = QtWidgets.QFrame(Form)
        self.line_13.setGeometry(QtCore.QRect(730, 358, 3, 40))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(Form)
        self.line_14.setGeometry(QtCore.QRect(1010, 360, 3, 40))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(Form)
        self.line_15.setGeometry(QtCore.QRect(730, 350, 281, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.num_of_steps_4 = QtWidgets.QLabel(Form)
        self.num_of_steps_4.setGeometry(QtCore.QRect(730, 380, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_4.setFont(font)
        self.num_of_steps_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_4.setWordWrap(True)
        self.num_of_steps_4.setObjectName("num_of_steps_4")
        self.time_4 = QtWidgets.QLabel(Form)
        self.time_4.setGeometry(QtCore.QRect(730, 360, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_4.setFont(font)
        self.time_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_4.setWordWrap(True)
        self.time_4.setObjectName("time_4")
        self.line_16 = QtWidgets.QFrame(Form)
        self.line_16.setGeometry(QtCore.QRect(730, 391, 281, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.time_value_4 = QtWidgets.QLabel(Form)
        self.time_value_4.setGeometry(QtCore.QRect(870, 360, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_4.setFont(font)
        self.time_value_4.setText("")
        self.time_value_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_4.setWordWrap(True)
        self.time_value_4.setObjectName("time_value_4")
        self.num_of_steps_value_4 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_4.setGeometry(QtCore.QRect(870, 380, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_4.setFont(font)
        self.num_of_steps_value_4.setText("")
        self.num_of_steps_value_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_4.setWordWrap(True)
        self.num_of_steps_value_4.setObjectName("num_of_steps_value_4")
        self.line_17 = QtWidgets.QFrame(Form)
        self.line_17.setGeometry(QtCore.QRect(730, 448, 3, 40))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(Form)
        self.line_18.setGeometry(QtCore.QRect(1010, 450, 3, 40))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(Form)
        self.line_19.setGeometry(QtCore.QRect(730, 440, 281, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.num_of_steps_5 = QtWidgets.QLabel(Form)
        self.num_of_steps_5.setGeometry(QtCore.QRect(730, 470, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_5.setFont(font)
        self.num_of_steps_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_5.setWordWrap(True)
        self.num_of_steps_5.setObjectName("num_of_steps_5")
        self.time_5 = QtWidgets.QLabel(Form)
        self.time_5.setGeometry(QtCore.QRect(730, 450, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_5.setFont(font)
        self.time_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_5.setWordWrap(True)
        self.time_5.setObjectName("time_5")
        self.line_20 = QtWidgets.QFrame(Form)
        self.line_20.setGeometry(QtCore.QRect(730, 481, 281, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.time_value_5 = QtWidgets.QLabel(Form)
        self.time_value_5.setGeometry(QtCore.QRect(870, 450, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_5.setFont(font)
        self.time_value_5.setText("")
        self.time_value_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_5.setWordWrap(True)
        self.time_value_5.setObjectName("time_value_5")
        self.num_of_steps_value_5 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_5.setGeometry(QtCore.QRect(870, 470, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_5.setFont(font)
        self.num_of_steps_value_5.setText("")
        self.num_of_steps_value_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_5.setWordWrap(True)
        self.num_of_steps_value_5.setObjectName("num_of_steps_value_5")
        self.line_21 = QtWidgets.QFrame(Form)
        self.line_21.setGeometry(QtCore.QRect(730, 538, 3, 40))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(Form)
        self.line_22.setGeometry(QtCore.QRect(1010, 540, 3, 40))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(Form)
        self.line_23.setGeometry(QtCore.QRect(730, 530, 281, 16))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.num_of_steps_6 = QtWidgets.QLabel(Form)
        self.num_of_steps_6.setGeometry(QtCore.QRect(730, 560, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_6.setFont(font)
        self.num_of_steps_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_6.setWordWrap(True)
        self.num_of_steps_6.setObjectName("num_of_steps_6")
        self.time_6 = QtWidgets.QLabel(Form)
        self.time_6.setGeometry(QtCore.QRect(730, 540, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_6.setFont(font)
        self.time_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_6.setWordWrap(True)
        self.time_6.setObjectName("time_6")
        self.line_24 = QtWidgets.QFrame(Form)
        self.line_24.setGeometry(QtCore.QRect(730, 571, 281, 16))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.time_value_6 = QtWidgets.QLabel(Form)
        self.time_value_6.setGeometry(QtCore.QRect(870, 540, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_6.setFont(font)
        self.time_value_6.setText("")
        self.time_value_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_6.setWordWrap(True)
        self.time_value_6.setObjectName("time_value_6")
        self.num_of_steps_value_6 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_6.setGeometry(QtCore.QRect(870, 560, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_6.setFont(font)
        self.num_of_steps_value_6.setText("")
        self.num_of_steps_value_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_6.setWordWrap(True)
        self.num_of_steps_value_6.setObjectName("num_of_steps_value_6")
        self.line_25 = QtWidgets.QFrame(Form)
        self.line_25.setGeometry(QtCore.QRect(730, 628, 3, 40))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(Form)
        self.line_26.setGeometry(QtCore.QRect(1010, 630, 3, 40))
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(Form)
        self.line_27.setGeometry(QtCore.QRect(730, 620, 281, 16))
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.num_of_steps_7 = QtWidgets.QLabel(Form)
        self.num_of_steps_7.setGeometry(QtCore.QRect(730, 650, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_7.setFont(font)
        self.num_of_steps_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_7.setWordWrap(True)
        self.num_of_steps_7.setObjectName("num_of_steps_7")
        self.time_7 = QtWidgets.QLabel(Form)
        self.time_7.setGeometry(QtCore.QRect(730, 630, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_7.setFont(font)
        self.time_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_7.setWordWrap(True)
        self.time_7.setObjectName("time_7")
        self.line_28 = QtWidgets.QFrame(Form)
        self.line_28.setGeometry(QtCore.QRect(730, 661, 281, 16))
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.time_value_7 = QtWidgets.QLabel(Form)
        self.time_value_7.setGeometry(QtCore.QRect(870, 630, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_7.setFont(font)
        self.time_value_7.setText("")
        self.time_value_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_7.setWordWrap(True)
        self.time_value_7.setObjectName("time_value_7")
        self.num_of_steps_value_7 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_7.setGeometry(QtCore.QRect(870, 650, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_7.setFont(font)
        self.num_of_steps_value_7.setText("")
        self.num_of_steps_value_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_7.setWordWrap(True)
        self.num_of_steps_value_7.setObjectName("num_of_steps_value_7")
        self.line_29 = QtWidgets.QFrame(Form)
        self.line_29.setGeometry(QtCore.QRect(730, 718, 3, 40))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(Form)
        self.line_30.setGeometry(QtCore.QRect(1010, 720, 3, 40))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(Form)
        self.line_31.setGeometry(QtCore.QRect(730, 710, 281, 16))
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.num_of_steps_8 = QtWidgets.QLabel(Form)
        self.num_of_steps_8.setGeometry(QtCore.QRect(730, 740, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_8.setFont(font)
        self.num_of_steps_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_8.setWordWrap(True)
        self.num_of_steps_8.setObjectName("num_of_steps_8")
        self.time_8 = QtWidgets.QLabel(Form)
        self.time_8.setGeometry(QtCore.QRect(730, 720, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_8.setFont(font)
        self.time_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_8.setWordWrap(True)
        self.time_8.setObjectName("time_8")
        self.line_32 = QtWidgets.QFrame(Form)
        self.line_32.setGeometry(QtCore.QRect(730, 751, 281, 16))
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.time_value_8 = QtWidgets.QLabel(Form)
        self.time_value_8.setGeometry(QtCore.QRect(870, 720, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_8.setFont(font)
        self.time_value_8.setText("")
        self.time_value_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_8.setWordWrap(True)
        self.time_value_8.setObjectName("time_value_8")
        self.num_of_steps_value_8 = QtWidgets.QLabel(Form)
        self.num_of_steps_value_8.setGeometry(QtCore.QRect(870, 740, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_8.setFont(font)
        self.num_of_steps_value_8.setText("")
        self.num_of_steps_value_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_8.setWordWrap(True)
        self.num_of_steps_value_8.setObjectName("num_of_steps_value_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "a"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))
        self.labelCombobox.setText(_translate("Form", "Number of rows:"))
        self.comboBox.setItemText(0, _translate("Form", "2"))
        self.comboBox.setItemText(1, _translate("Form", "3"))
        self.comboBox.setItemText(2, _translate("Form", "4"))
        self.comboBox.setItemText(3, _translate("Form", "5"))
        self.comboBox.setItemText(4, _translate("Form", "6"))
        self.comboBox.setItemText(5, _translate("Form", "7"))
        self.comboBox.setItemText(6, _translate("Form", "8"))
        self.comboBox.setItemText(7, _translate("Form", "9"))
        self.comboBox.setItemText(8, _translate("Form", "10"))
        self.resetBtn.setText(_translate("Form", "Reset"))
        #self.resetBtn.clicked.connect(lambda: print("hello"))
        self.clicked()
        def clicked():
            for i in reversed(range(self.gltMain.count())): 
                self.gltMain.itemAt(i).widget().setParent(None)
            content = int(self.comboBox.currentText())
            
            self.num_row = content
            self.onInit()
            # for i in range(500):
            #     random_num = random.randint(0, 3)
            #     self.move(Direction(random_num))
            # self.updatePanel()
        self.resetBtn.clicked.connect(clicked)

        self.time_1.setText(_translate("Form", "  Time: "))
        self.num_of_steps_1.setText(_translate("Form", "  Number of steps: "))
        self.num_of_steps_2.setText(_translate("Form", "  Number of steps: "))
        self.time_2.setText(_translate("Form", "  Time: "))
        self.num_of_steps_3.setText(_translate("Form", "  Number of steps: "))
        self.time_3.setText(_translate("Form", "  Time: "))
        self.num_of_steps_4.setText(_translate("Form", "  Number of steps: "))
        self.time_4.setText(_translate("Form", "  Time: "))
        self.num_of_steps_5.setText(_translate("Form", "  Number of steps: "))
        self.time_5.setText(_translate("Form", "  Time: "))
        self.num_of_steps_6.setText(_translate("Form", "  Number of steps: "))
        self.time_6.setText(_translate("Form", "  Time: "))
        self.num_of_steps_7.setText(_translate("Form", "  Number of steps: "))
        self.time_7.setText(_translate("Form", "  Time: "))
        self.num_of_steps_8.setText(_translate("Form", "  Number of steps: "))
        self.time_8.setText(_translate("Form", "  Time: "))

    def clicked(self):
        print("fsadf")

    def initUI(self):      
        # Set number block spacing
        self.gltMain.setSpacing(20)
        self.onInit()
        # Set layout.
        self.setLayout(self.gltMain)
        # Set window width and height.
        self.setFixedSize(400, 400)
        # Set window title.
        self.setWindowTitle('N-puzzle Game.')
        # Set window background color.
        self.setStyleSheet("background-color:gray;")
        #self.show()
    # Initialize layout.
    def onInit(self):
        # Create sequential array.
        self.numbers = list(range(1, self.num_row * self.num_row))
        self.numbers.append(0)
        # Add number to the two-dimensional array.
        self.blocks = []
        for row in range(self.num_row):
            self.blocks.append([])
            for column in range(self.num_row):
                temp = self.numbers[row * self.num_row + column]
                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)
        # Scrambling the array.
        for i in range(500):
            random_num = random.randint(0, 3)
            self.move(Direction(random_num))
        self.updatePanel()
    # Detect key press event.
    def keyPressEvent(self, e):
        print("haa")

    # def keyPressEvent(self, event):
    #     key = event.key()
    #     if(key == Qt.Key_Up or key == Qt.Key_W):
    #         self.move(Direction.UP)
    #     if(key == Qt.Key_Down or key == Qt.Key_S):
    #         self.move(Direction.DOWN)
    #     if(key == Qt.Key_Left or key == Qt.Key_A):
    #         self.move(Direction.LEFT)
    #     if(key == Qt.Key_Right or key == Qt.Key_D):
    #         self.move(Direction.RIGHT)
    #     self.updatePanel()
    #     if self.checkResult():
    #         if QMessageBox.Ok == QMessageBox.information(self, 'Challenge Results', 'Congratulations on completing the challenge!'):
    #             self.onInit()
    
    # Block moving algorithm.
    def move(self, direction):
        if(direction == Direction.UP): # Move up.
            if self.zero_row != self.num_row - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if(direction == Direction.DOWN): # Move down.
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
        if(direction == Direction.LEFT): # Move left.
            if self.zero_column != self.num_row - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if(direction == Direction.RIGHT): # Move right.
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1
    def updatePanel(self):
        for row in range(self.num_row):
            for column in range(self.num_row):
                self.gltMain.addWidget(Block(self.blocks[row][column], int(720 / self.num_row) - 15), row, column)
        self.widget.setLayout(self.gltMain)
    # Check whether the challenge is completed or not.
    def checkResult(self):
        # First check whether the block value in the bottom right corner is 0。
        if self.blocks[self.num_row - 1][self.num_row - 1] != 0:
            return False
        for row in range(self.num_row):
            for column in range(self.num_row):
                # The value of the block in the bottom right corner is 0, pass.
                if row == self.num_row - 1 and column == self.num_row - 1:
                    pass
                # Check whether the square block number is correct number.
                elif self.blocks[row][column] != row * self.num_row + column + 1:
                    return False
        return True

class Block(QLabel):
    """ Number block """
    def __init__(self, number, fixed_size):
        super().__init__()
        self.number = number
        self.fixed_size = fixed_size
        self.setFixedSize(self.fixed_size, self.fixed_size)
        # Set text font.
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)
        # Set text color.
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)
        # Set text alignment.
        self.setAlignment(Qt.AlignCenter)
        # Set background color, filleted corner and text content。
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:red;border-radius:10px;")
            self.setText(str(self.number))  

class Temp(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        print("haha") 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

