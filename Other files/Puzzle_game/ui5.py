# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Puzzle_game/ui5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 720, 720))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(739, 49, 311, 721))
        self.widget_2.setObjectName("widget_2")
        self.time_value_7 = QtWidgets.QLabel(self.widget_2)
        self.time_value_7.setGeometry(QtCore.QRect(150, 580, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_7.setFont(font)
        self.time_value_7.setText("")
        self.time_value_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_7.setWordWrap(True)
        self.time_value_7.setObjectName("time_value_7")
        self.line_13 = QtWidgets.QFrame(self.widget_2)
        self.line_13.setGeometry(QtCore.QRect(10, 308, 3, 40))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setGeometry(QtCore.QRect(10, 30, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.time_value_1 = QtWidgets.QLabel(self.widget_2)
        self.time_value_1.setGeometry(QtCore.QRect(150, 40, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_1.setFont(font)
        self.time_value_1.setText("")
        self.time_value_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_1.setWordWrap(True)
        self.time_value_1.setObjectName("time_value_1")
        self.line_18 = QtWidgets.QFrame(self.widget_2)
        self.line_18.setGeometry(QtCore.QRect(290, 400, 3, 40))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.time_2 = QtWidgets.QLabel(self.widget_2)
        self.time_2.setGeometry(QtCore.QRect(10, 130, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_2.setFont(font)
        self.time_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_2.setWordWrap(True)
        self.time_2.setObjectName("time_2")
        self.line_17 = QtWidgets.QFrame(self.widget_2)
        self.line_17.setGeometry(QtCore.QRect(10, 398, 3, 40))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_31 = QtWidgets.QFrame(self.widget_2)
        self.line_31.setGeometry(QtCore.QRect(10, 660, 281, 16))
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.num_of_steps_3 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_3.setGeometry(QtCore.QRect(10, 240, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_3.setFont(font)
        self.num_of_steps_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_3.setWordWrap(True)
        self.num_of_steps_3.setObjectName("num_of_steps_3")
        self.line_22 = QtWidgets.QFrame(self.widget_2)
        self.line_22.setGeometry(QtCore.QRect(290, 490, 3, 40))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_30 = QtWidgets.QFrame(self.widget_2)
        self.line_30.setGeometry(QtCore.QRect(290, 670, 3, 40))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_10 = QtWidgets.QFrame(self.widget_2)
        self.line_10.setGeometry(QtCore.QRect(290, 220, 3, 40))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.time_1 = QtWidgets.QLabel(self.widget_2)
        self.time_1.setGeometry(QtCore.QRect(10, 40, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_1.setFont(font)
        self.time_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_1.setWordWrap(True)
        self.time_1.setObjectName("time_1")
        self.line_27 = QtWidgets.QFrame(self.widget_2)
        self.line_27.setGeometry(QtCore.QRect(10, 570, 281, 16))
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.num_of_steps_1 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_1.setGeometry(QtCore.QRect(10, 60, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_1.setFont(font)
        self.num_of_steps_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_1.setWordWrap(True)
        self.num_of_steps_1.setObjectName("num_of_steps_1")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 450, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.time_4 = QtWidgets.QLabel(self.widget_2)
        self.time_4.setGeometry(QtCore.QRect(10, 310, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_4.setFont(font)
        self.time_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_4.setWordWrap(True)
        self.time_4.setObjectName("time_4")
        self.time_7 = QtWidgets.QLabel(self.widget_2)
        self.time_7.setGeometry(QtCore.QRect(10, 580, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_7.setFont(font)
        self.time_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_7.setWordWrap(True)
        self.time_7.setObjectName("time_7")
        self.num_of_steps_value_3 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_3.setGeometry(QtCore.QRect(150, 240, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_3.setFont(font)
        self.num_of_steps_value_3.setText("")
        self.num_of_steps_value_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_3.setWordWrap(True)
        self.num_of_steps_value_3.setObjectName("num_of_steps_value_3")
        self.num_of_steps_value_4 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_4.setGeometry(QtCore.QRect(150, 330, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_4.setFont(font)
        self.num_of_steps_value_4.setText("")
        self.num_of_steps_value_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_4.setWordWrap(True)
        self.num_of_steps_value_4.setObjectName("num_of_steps_value_4")
        self.line_11 = QtWidgets.QFrame(self.widget_2)
        self.line_11.setGeometry(QtCore.QRect(10, 210, 281, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.time_8 = QtWidgets.QLabel(self.widget_2)
        self.time_8.setGeometry(QtCore.QRect(10, 670, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_8.setFont(font)
        self.time_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_8.setWordWrap(True)
        self.time_8.setObjectName("time_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 630, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.num_of_steps_value_2 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_2.setGeometry(QtCore.QRect(150, 150, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_2.setFont(font)
        self.num_of_steps_value_2.setText("")
        self.num_of_steps_value_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_2.setWordWrap(True)
        self.num_of_steps_value_2.setObjectName("num_of_steps_value_2")
        self.num_of_steps_8 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_8.setGeometry(QtCore.QRect(10, 690, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_8.setFont(font)
        self.num_of_steps_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_8.setWordWrap(True)
        self.num_of_steps_8.setObjectName("num_of_steps_8")
        self.time_value_8 = QtWidgets.QLabel(self.widget_2)
        self.time_value_8.setGeometry(QtCore.QRect(150, 670, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_8.setFont(font)
        self.time_value_8.setText("")
        self.time_value_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_8.setWordWrap(True)
        self.time_value_8.setObjectName("time_value_8")
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(290, 40, 3, 40))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setGeometry(QtCore.QRect(10, 71, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_28 = QtWidgets.QFrame(self.widget_2)
        self.line_28.setGeometry(QtCore.QRect(10, 611, 281, 16))
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.time_value_6 = QtWidgets.QLabel(self.widget_2)
        self.time_value_6.setGeometry(QtCore.QRect(150, 490, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_6.setFont(font)
        self.time_value_6.setText("")
        self.time_value_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_6.setWordWrap(True)
        self.time_value_6.setObjectName("time_value_6")
        self.line_29 = QtWidgets.QFrame(self.widget_2)
        self.line_29.setGeometry(QtCore.QRect(10, 668, 3, 40))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.time_value_4 = QtWidgets.QLabel(self.widget_2)
        self.time_value_4.setGeometry(QtCore.QRect(150, 310, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_4.setFont(font)
        self.time_value_4.setText("")
        self.time_value_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_4.setWordWrap(True)
        self.time_value_4.setObjectName("time_value_4")
        self.num_of_steps_7 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_7.setGeometry(QtCore.QRect(10, 600, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_7.setFont(font)
        self.num_of_steps_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_7.setWordWrap(True)
        self.num_of_steps_7.setObjectName("num_of_steps_7")
        self.line_7 = QtWidgets.QFrame(self.widget_2)
        self.line_7.setGeometry(QtCore.QRect(10, 120, 281, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.num_of_steps_value_7 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_7.setGeometry(QtCore.QRect(150, 600, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_7.setFont(font)
        self.num_of_steps_value_7.setText("")
        self.num_of_steps_value_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_7.setWordWrap(True)
        self.num_of_steps_value_7.setObjectName("num_of_steps_value_7")
        self.line_8 = QtWidgets.QFrame(self.widget_2)
        self.line_8.setGeometry(QtCore.QRect(10, 161, 281, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.time_value_5 = QtWidgets.QLabel(self.widget_2)
        self.time_value_5.setGeometry(QtCore.QRect(150, 400, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_5.setFont(font)
        self.time_value_5.setText("")
        self.time_value_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_5.setWordWrap(True)
        self.time_value_5.setObjectName("time_value_5")
        self.line_6 = QtWidgets.QFrame(self.widget_2)
        self.line_6.setGeometry(QtCore.QRect(290, 130, 3, 40))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_12 = QtWidgets.QFrame(self.widget_2)
        self.line_12.setGeometry(QtCore.QRect(10, 251, 281, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_15 = QtWidgets.QFrame(self.widget_2)
        self.line_15.setGeometry(QtCore.QRect(10, 300, 281, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.num_of_steps_value_8 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_8.setGeometry(QtCore.QRect(150, 690, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_8.setFont(font)
        self.num_of_steps_value_8.setText("")
        self.num_of_steps_value_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_8.setWordWrap(True)
        self.num_of_steps_value_8.setObjectName("num_of_steps_value_8")
        self.num_of_steps_5 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_5.setGeometry(QtCore.QRect(10, 420, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_5.setFont(font)
        self.num_of_steps_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_5.setWordWrap(True)
        self.num_of_steps_5.setObjectName("num_of_steps_5")
        self.num_of_steps_6 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_6.setGeometry(QtCore.QRect(10, 510, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_6.setFont(font)
        self.num_of_steps_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_6.setWordWrap(True)
        self.num_of_steps_6.setObjectName("num_of_steps_6")
        self.num_of_steps_value_1 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_1.setGeometry(QtCore.QRect(150, 60, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_1.setFont(font)
        self.num_of_steps_value_1.setText("")
        self.num_of_steps_value_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_1.setWordWrap(True)
        self.num_of_steps_value_1.setObjectName("num_of_steps_value_1")
        self.time_value_3 = QtWidgets.QLabel(self.widget_2)
        self.time_value_3.setGeometry(QtCore.QRect(150, 220, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_3.setFont(font)
        self.time_value_3.setText("")
        self.time_value_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_3.setWordWrap(True)
        self.time_value_3.setObjectName("time_value_3")
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(10, 128, 3, 40))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_25 = QtWidgets.QFrame(self.widget_2)
        self.line_25.setGeometry(QtCore.QRect(10, 578, 3, 40))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 180, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_24 = QtWidgets.QFrame(self.widget_2)
        self.line_24.setGeometry(QtCore.QRect(10, 521, 281, 16))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_23 = QtWidgets.QFrame(self.widget_2)
        self.line_23.setGeometry(QtCore.QRect(10, 480, 281, 16))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.num_of_steps_2 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_2.setGeometry(QtCore.QRect(10, 150, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_2.setFont(font)
        self.num_of_steps_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_2.setWordWrap(True)
        self.num_of_steps_2.setObjectName("num_of_steps_2")
        self.time_6 = QtWidgets.QLabel(self.widget_2)
        self.time_6.setGeometry(QtCore.QRect(10, 490, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_6.setFont(font)
        self.time_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_6.setWordWrap(True)
        self.time_6.setObjectName("time_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 540, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_9 = QtWidgets.QFrame(self.widget_2)
        self.line_9.setGeometry(QtCore.QRect(10, 218, 3, 40))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_14 = QtWidgets.QFrame(self.widget_2)
        self.line_14.setGeometry(QtCore.QRect(290, 310, 3, 40))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.num_of_steps_4 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_4.setGeometry(QtCore.QRect(10, 330, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_of_steps_4.setFont(font)
        self.num_of_steps_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_4.setWordWrap(True)
        self.num_of_steps_4.setObjectName("num_of_steps_4")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setGeometry(QtCore.QRect(10, 38, 3, 40))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_32 = QtWidgets.QFrame(self.widget_2)
        self.line_32.setGeometry(QtCore.QRect(10, 701, 281, 16))
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.num_of_steps_value_6 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_6.setGeometry(QtCore.QRect(150, 510, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_6.setFont(font)
        self.num_of_steps_value_6.setText("")
        self.num_of_steps_value_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_6.setWordWrap(True)
        self.num_of_steps_value_6.setObjectName("num_of_steps_value_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 0, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda: print("hello"))
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_26 = QtWidgets.QFrame(self.widget_2)
        self.line_26.setGeometry(QtCore.QRect(290, 580, 3, 40))
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.time_5 = QtWidgets.QLabel(self.widget_2)
        self.time_5.setGeometry(QtCore.QRect(10, 400, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_5.setFont(font)
        self.time_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_5.setWordWrap(True)
        self.time_5.setObjectName("time_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 360, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_21 = QtWidgets.QFrame(self.widget_2)
        self.line_21.setGeometry(QtCore.QRect(10, 488, 3, 40))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.time_3 = QtWidgets.QLabel(self.widget_2)
        self.time_3.setGeometry(QtCore.QRect(10, 220, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_3.setFont(font)
        self.time_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_3.setWordWrap(True)
        self.time_3.setObjectName("time_3")
        self.line_16 = QtWidgets.QFrame(self.widget_2)
        self.line_16.setGeometry(QtCore.QRect(10, 341, 281, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.num_of_steps_value_5 = QtWidgets.QLabel(self.widget_2)
        self.num_of_steps_value_5.setGeometry(QtCore.QRect(150, 420, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.num_of_steps_value_5.setFont(font)
        self.num_of_steps_value_5.setText("")
        self.num_of_steps_value_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.num_of_steps_value_5.setWordWrap(True)
        self.num_of_steps_value_5.setObjectName("num_of_steps_value_5")
        self.line_20 = QtWidgets.QFrame(self.widget_2)
        self.line_20.setGeometry(QtCore.QRect(10, 431, 281, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.time_value_2 = QtWidgets.QLabel(self.widget_2)
        self.time_value_2.setGeometry(QtCore.QRect(150, 130, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.time_value_2.setFont(font)
        self.time_value_2.setText("")
        self.time_value_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.time_value_2.setWordWrap(True)
        self.time_value_2.setObjectName("time_value_2")
        self.line_19 = QtWidgets.QFrame(self.widget_2)
        self.line_19.setGeometry(QtCore.QRect(10, 390, 281, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 270, 281, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_2.setText(_translate("MainWindow", "  Time: "))
        self.num_of_steps_3.setText(_translate("MainWindow", "  Number of steps: "))
        self.time_1.setText(_translate("MainWindow", "  Time: "))
        self.num_of_steps_1.setText(_translate("MainWindow", "  Number of steps: "))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.time_4.setText(_translate("MainWindow", "  Time: "))
        self.time_7.setText(_translate("MainWindow", "  Time: "))
        self.time_8.setText(_translate("MainWindow", "  Time: "))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.num_of_steps_8.setText(_translate("MainWindow", "  Number of steps: "))
        self.num_of_steps_7.setText(_translate("MainWindow", "  Number of steps: "))
        self.num_of_steps_5.setText(_translate("MainWindow", "  Number of steps: "))
        self.num_of_steps_6.setText(_translate("MainWindow", "  Number of steps: "))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.num_of_steps_2.setText(_translate("MainWindow", "  Number of steps: "))
        self.time_6.setText(_translate("MainWindow", "  Time: "))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.num_of_steps_4.setText(_translate("MainWindow", "  Number of steps: "))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.time_5.setText(_translate("MainWindow", "  Time: "))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.time_3.setText(_translate("MainWindow", "  Time: "))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))

    def keyPressEvent(self, e):
        print(e.key())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
