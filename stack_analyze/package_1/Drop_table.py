# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Drop_table.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sqlite3
class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        QDialog.__init__(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 384)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(33, 141, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 140, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.drop_data)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Delete company data"))
        self.label_2.setText(_translate("Dialog", "name "))
        self.pushButton.setText(_translate("Dialog", "confirm to delete"))
    def drop_data(self):
        try:
            conn = sqlite3.connect(r'db\dataBase.db')
            conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
            conn.commit()
            cur = conn.cursor()
            name=self.lineEdit.text()
            data=cur.execute("drop table %s"%name)
            QtWidgets.QMessageBox.information(self,"info","删除table"+name+"成功")
            conn.commit()
            cur.close()
            conn.close()
        except Exception as err:
#             print("laji")
            QtWidgets.QMessageBox.information(self,"info","数据库无此文件")
            print(err)
class query_interface(QDialog):
#     print("hah")
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

