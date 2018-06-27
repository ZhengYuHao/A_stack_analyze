# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sqlite3
from package_1 import title
# import image_1
# import image_2

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1700, 850)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(72, 91, 97);")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(330, 120, 262, 216))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 120, 111, 213))
        self.textBrowser_3.setStyleSheet("background-color: rgb(113, 154, 146);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 580, 111, 178))
        self.textBrowser_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 207, 207);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(330, 580, 262, 179))
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(80, 330, 111, 251))
        self.textBrowser_5.setStyleSheet("background-color: rgb(140, 182, 178);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_3.setGeometry(QtCore.QRect(330, 330, 262, 253))
        self.tableWidget_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(610, 120, 111, 105))
        self.textBrowser_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 182, 178);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.tableWidget_4 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_4.setGeometry(QtCore.QRect(860, 119, 262, 105))
        self.tableWidget_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(610, 223, 111, 101))
        self.textBrowser_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 154, 146);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.tableWidget_5 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_5.setGeometry(QtCore.QRect(860, 220, 262, 105))
        self.tableWidget_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1340, 120, 181, 33))
        self.pushButton.setStyleSheet("font: 75 9pt \"微软雅黑\";\n"
"background-color: rgb(113, 154, 146);")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(1260, 250, 341, 521))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1340, 180, 181, 33))
        self.pushButton_2.setStyleSheet("font: 75 9pt \"微软雅黑\";\n"
"background-color: rgb(172, 186, 197);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 150, 141, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 186, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 222, 141, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(83, 175, 190);color: rgb(0, 0, 0);")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 260, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(144, 209, 211);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 298, 141, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(190, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(247, 231, 190);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(190, 432, 141, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(144, 209, 211);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(190, 362, 141, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(0, 0, 0);")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(190, 472, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(0, 0, 0);")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(191, 398, 140, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(83, 175, 190);color: rgb(0, 0, 0);")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(190, 332, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(247, 231, 190);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(190, 510, 141, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(190, 550, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(83, 175, 190);color: rgb(0, 0, 0);")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(720, 250, 141, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(0, 0, 0);")
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(720, 286, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(83, 175, 190);color: rgb(0, 0, 0);")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(720, 221, 141, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(247, 231, 190);\n"
"color: rgb(0, 0, 0);")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(720, 186, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(720, 120, 141, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(247, 231, 190);\n"
"color: rgb(0, 0, 0);")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(720, 149, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(144, 209, 211);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(190, 682, 141, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(0, 0, 0);")
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(190, 610, 141, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(144, 209, 211);\n"
"color: rgb(0, 0, 0);")
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(190, 720, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(144, 209, 211);\n"
"color: rgb(0, 0, 0);")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(190, 646, 141, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(0, 0, 0);")
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(190, 580, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(247, 231, 190);\n"
"color: rgb(0, 0, 0);")
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(620, 360, 311, 391))
        self.textEdit.setStyleSheet("color: rgb(176, 204, 207);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(950, 400, 251, 211))
        self.textEdit_2.setStyleSheet("color: rgb(176, 204, 207);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.pushButton.clicked.connect(self.set_intia) 
        self.pushButton_2.clicked.connect(self.get_class)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "最大值"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从现金流量</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破解公司的</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">存活能力</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从经营能力</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破解公司做</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">生意真本事</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "最大值"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从获利能力</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破解公司做</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">生意真本事</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "最大值"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从财务结构</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破解公司的</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破产危机</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "最大值"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从偿债能力</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">破解公司</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">还钱本事</span></p></body></html>"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "最大值"))
        self.pushButton.setText(_translate("Dialog", "获取推荐指数"))
        self.pushButton_2.setText(_translate("Dialog", "自定义指数，并开始检索"))
        self.label.setText(_translate("Dialog", "现金流量比率"))
        self.label_2.setText(_translate("Dialog", "现金与约当现金比率"))
        self.label_3.setText(_translate("Dialog", "现金流量允当率"))
        self.label_4.setText(_translate("Dialog", "现金再投资比率"))
        self.label_5.setText(_translate("Dialog", "应收账款周转天数"))
        self.label_6.setText(_translate("Dialog", "现金流量"))
        self.label_7.setText(_translate("Dialog", "经营安全边际率"))
        self.label_8.setText(_translate("Dialog", "毛利率"))
        self.label_9.setText(_translate("Dialog", "净利率"))
        self.label_10.setText(_translate("Dialog", "营业费用率"))
        self.label_11.setText(_translate("Dialog", "获利能力"))
        self.label_12.setText(_translate("Dialog", "每股收益"))
        self.label_13.setText(_translate("Dialog", "净资产收益率"))
        self.label_14.setText(_translate("Dialog", "速动比率"))
        self.label_15.setText(_translate("Dialog", "流动比率"))
        self.label_16.setText(_translate("Dialog", "债偿能力"))
        self.label_17.setText(_translate("Dialog", "资产负债率"))
        self.label_18.setText(_translate("Dialog", "财务结构"))
        self.label_19.setText(_translate("Dialog", "长期资金占不动产/厂房及设备比率"))
        self.label_20.setText(_translate("Dialog", "存货周转天数"))
        self.label_21.setText(_translate("Dialog", "总资产周转率"))
        self.label_22.setText(_translate("Dialog", "应收账款周转天数"))
        self.label_23.setText(_translate("Dialog", "现金与约当现金比率"))
        self.label_24.setText(_translate("Dialog", "经营能力"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600;\">Notes:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从现金流量破解公司的存活能力</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A11=现金流量比率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A12=现金流量允当比率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A13=现金再投资比率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A21=现金与约当现金占总资产比率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A31=应收账款周天数（越小越好）</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从经营能力破解公司做生意真本事</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">B1=总资产周转率（以1位界，判断轻重资产）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">B1_A2=现金与约当现金占总资产比率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">B21=平均在库天数（越小越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">B31=应收账款周转天数（越小越好）</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从财务结构破解公司的破产危机</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D1=资产负债率（越小越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D2=长期资金占不动产/厂房及设备比率（越大越好）</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从获利能力破解公司做生意真本事</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c1=毛利率（越大越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c2=营业费用率(越小越好)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c3=经营安全边际率(越大越好)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c4=净利率（越大越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c5=每股收益（越大越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c6=净资产收益率(越大越好)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">从偿债能力破解公司还钱本事</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E1=流动比率（越大越好）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E2=速动比率（越大越好）</p></body></html>"))
    def set_intia(self):
        #table1
        item=QtWidgets.QTableWidgetItem("0.1")
        self.tableWidget.setItem(0,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget.setItem(0,1,item)
        item=QtWidgets.QTableWidgetItem("0.1")
        self.tableWidget.setItem(1,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget.setItem(1,1,item)
        item=QtWidgets.QTableWidgetItem("0.1")
        self.tableWidget.setItem(2,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget.setItem(2,1,item)
        item=QtWidgets.QTableWidgetItem("0.1")
        self.tableWidget.setItem(3,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget.setItem(3,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget.setItem(4,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget.setItem(4,1,item)
#         self.tableWidget.setItem()
        #table2
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_2.setItem(0,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_2.setItem(0,1,item)
        item=QtWidgets.QTableWidgetItem("0.025")
        self.tableWidget_2.setItem(1,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_2.setItem(1,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_2.setItem(2,0,item)
        item=QtWidgets.QTableWidgetItem("300")
        self.tableWidget_2.setItem(2,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_2.setItem(3,0,item)
        item=QtWidgets.QTableWidgetItem("150")
        self.tableWidget_2.setItem(3,1,item)
        #table3
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_3.setItem(0,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_3.setItem(0,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_3.setItem(1,0,item)
        item=QtWidgets.QTableWidgetItem("0.1")
        self.tableWidget_3.setItem(1,1,item)
        item=QtWidgets.QTableWidgetItem("0.9")
        self.tableWidget_3.setItem(2,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_3.setItem(2,1,item)
        item=QtWidgets.QTableWidgetItem("0.02")
        self.tableWidget_3.setItem(3,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_3.setItem(3,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_3.setItem(4,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_3.setItem(4,1,item)
        item=QtWidgets.QTableWidgetItem("0.01")
        self.tableWidget_3.setItem(5,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_3.setItem(5,1,item)
        #table4
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_4.setItem(0,0,item)
        item=QtWidgets.QTableWidgetItem("6")
        self.tableWidget_4.setItem(0,1,item)
        item=QtWidgets.QTableWidgetItem("0")
        self.tableWidget_4.setItem(1,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_4.setItem(1,1,item)
        #table5
        item=QtWidgets.QTableWidgetItem("0.3")
        self.tableWidget_5.setItem(0,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_5.setItem(0,1,item)
        item=QtWidgets.QTableWidgetItem("0.15")
        self.tableWidget_5.setItem(1,0,item)
        item=QtWidgets.QTableWidgetItem("100")
        self.tableWidget_5.setItem(1,1,item)
    def get_class(self):
        class_data=[]
        m=self.tableWidget.rowCount()#获取列数
        n=self.tableWidget.columnCount()#获取行数
        for i in range(m):
            a=[0,0]
            for j in range(n):
                a[j]=(float(self.tableWidget.item(i, j).text()))
            class_data.append(a)
        n=self.tableWidget_2.columnCount()#获取列数
        m=self.tableWidget_2.rowCount()#获取行数
        for i in range(m):
            a=[0,0]
            for j in range(n):
                a[j]=(float(self.tableWidget_2.item(i, j).text()))
            class_data.append(a)
        n=self.tableWidget_3.columnCount()#获取列数
        m=self.tableWidget_3.rowCount()#获取行数
        for i in range(m):
            a=[0,0]
            for j in range(n):
                a[j]=(float(self.tableWidget_3.item(i, j).text()))
            class_data.append(a)
        n=self.tableWidget_4.columnCount()#获取列数
        m=self.tableWidget_4.rowCount()#获取行数
        for i in range(m):
            a=[0,0]
            for j in range(n):
                a[j]=(float(self.tableWidget_4.item(i, j).text()))
            class_data.append(a)
        #table5
        n=self.tableWidget_5.columnCount()#获取列数
        m=self.tableWidget_5.rowCount()#获取行数
        for i in range(m):
            a=[0,0]
            for j in range(n):
                a[j]=(float(self.tableWidget_5.item(i, j).text()))
            class_data.append(a)
        self.function(class_data)
    def function(self,ask):
          set_1=set()#现金流量比率
          set_2=set()#现金与约当现金比率
          set_3=set()#现金流量允当比率
          set_4=set()#现金再投资比率
          set_5=set()#应收账款周转
          
          set_6=set()#总资产周转率
          set_7=set()#现金与约当现金比率
          set_8=set()#存货周转天数
          set_9=set()#应收账款周转天数
          
          set_10=set()#毛利率
          set_11=set()#营业费用率
          set_12=set()#经济安全比率
          set_13=set()#净利润率
          set_14=set()#EPS_每股收益
          set_15=set()#净资产收益率
          
          set_16=set()#长期资金占不动产/厂房及设备比率
          set_17=set()#资产负债率
          
          set_18=set()#速动比率
          set_19=set()#流动比率
        
          text = sqlite3.connect(r'db\dataBase.db')
          cursor = text.cursor()
          cursor.execute("SELECT * FROM sqlite_master")
          data = cursor.fetchall()
          stock_company=[]
          for i in data[:-4]:
                stock_company.append(i[1])
          for i in stock_company:
              cursor.execute("SELECT * FROM '%s' WHERE id=='现金流量比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[0][0] and count<ask[0][1]):#当5平均都满足的时候
                set_1.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='现金与约当现金比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[1][0] and count<ask[1][1]):#当5平均都满足的时候
                set_2.add(i)
              
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='现金流量允当比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[2][0] and count<ask[2][1]):#当5平均都满足的时候
                set_3.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='现金再投资比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[3][0] and count<ask[3][1]):#当5平均都满足的时候
                set_4.add(i)
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='应收账款周转天数'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[4][0] and count<ask[4][1]):#当5平均都满足的时候
                set_5.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='总资产周转率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[5][0] and count<ask[5][1]):#当5平均都满足的时候
                set_6.add(i)
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='现金与约当现金比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[6][0] and count<ask[6][1]):#当5平均都满足的时候
                set_7.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='存货周转天数'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[7][0] and count<ask[7][1]):#当5平均都满足的时候
                set_8.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='应收账款周转天数'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[8][0] and count<ask[8][1]):#当5平均都满足的时候
                set_9.add(i)
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='毛利率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[9][0] and count<ask[9][1]):#当5平均都满足的时候
                set_10.add(i)
             
              cursor.execute("SELECT * FROM '%s' WHERE id=='营业费用率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[10][0] and count<ask[10][1]):#当5平均都满足的时候
                set_11.add(i)
                
        #       cursor.execute("SELECT * FROM '%s' WHERE id=='经济安全比率'"%i)
        #       temp=cursor.fetchall()
        #       flag=0
        #       for j in range(1,6):#当5年都满足的时候
        #         if(float(temp[0][j])<ask[11][0] or float(temp[0][j])>ask[11][1]):
        #             flag= 1
        #             break
        #       if(flag==0):#当5年都满足的时候
              set_12.add(i)
               
              cursor.execute("SELECT * FROM '%s' WHERE id=='净利润率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[12][0] and count<ask[12][1]):#当5平均都满足的时候
                set_13.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='EPS_每股收益'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[13][0] and count<ask[13][1]):#当5平均都满足的时候
                set_14.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='净资产收益率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[14][0] and count<ask[14][1]):#当5平均都满足的时候
                set_15.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='长期资金占不动产/厂房及设备比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[15][0] and count<ask[15][1]):#当5平均都满足的时候
                set_16.add(i)
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='资产负债率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[16][0] and count<ask[16][1]):#当5平均都满足的时候
                set_17.add(i)
              
              cursor.execute("SELECT * FROM '%s' WHERE id=='速动比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>ask[17][0] and count<ask[17][1]):#当5平均都满足的时候
                set_18.add(i)
                
              cursor.execute("SELECT * FROM '%s' WHERE id=='流动比率'"%i)
              temp=cursor.fetchall()
              count=0
              for j in range(1,6):#当5年都满足的时候
                count+=float(temp[0][j])
              count=count/5.0
              if(count>=ask[18][0] and count<=ask[18][1]):#当5平均都满足的时候
                set_19.add(i)
          set_result=set_1&set_2&set_3&set_4&set_5&set_6&set_7&set_8&set_9&set_10&set_11&set_12&set_13&set_14&set_15&set_16&set_17&set_18&set_19
          set_result=list(set_result)
          for i in set_result:
              self.textBrowser.append(i)

class query_interface(QDialog):
        def __init__(self):
          super(query_interface, self).__init__()
          self.ui=Ui_Dialog()
          self.ui.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp=query_interface()
    #myapp.setupUi()
    myapp.exec_()
    sys.exit(app.exec_())

