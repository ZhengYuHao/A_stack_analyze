# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RankingList.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from package_1 import title
# import image_1
# import image_2
# import menu_rc
# import 标题_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 736)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(72, 91, 97);\n"
"")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 170, 342, 521))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(176, 204, 207);\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 341, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(176, 204, 207);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 114, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(37, 112, 141);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(174, 130, 114, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(55, 143, 165);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(288, 130, 114, 39))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(83, 175, 190);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.funtion()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "股 票 排 行"))
        self.label_2.setText(_translate("Dialog", "排名"))
        self.label_3.setText(_translate("Dialog", "公司"))
        self.label_4.setText(_translate("Dialog", "总竞争力"))

    def funtion(self):
        conn = sqlite3.connect(r'db\dataBase.db')
        conn.isolation_level = None  # 这个就是事物隔离级别，默认是需要自己Commit才能修改数据库，置为None则每次自动修改提交
        conn.commit()
        cur = conn.cursor()  # 游标
        cur.execute("SELECT * FROM 绩优股排名表")
        res = cur.fetchall()  # 获取该表的所有数据，返回元组形式
        i=1
        for line in res:
                str_1 ='\t\t'.join(line)  # 将元组形式转化为字符串
                t=str(i)
                t=t+"\t"
                t=t+"  "
                str_1=t+str_1
                self.textBrowser.append(str_1)
                i+=1
        cur.close()
        conn.close()
        
class query_interface(QDialog):
        def __init__(self):
          super(query_interface, self).__init__()
          self.ui=Ui_Dialog()
          self.ui.setupUi(self)