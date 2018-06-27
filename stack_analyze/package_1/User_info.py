# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_info.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sqlite3
class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        QDialog.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(235, 416)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 111, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 111, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 140, 191, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.get_user_info()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "User_psw"))
        self.label_2.setText(_translate("Dialog", "User_name"))
        self.label_3.setText(_translate("Dialog", "User_infor"))
    def get_user_info(self):
        conn = sqlite3.connect(r'db\user_ab.db')
        conn.isolation_level = None
        conn.commit()
        cur = conn.cursor()
#         print(str_1,str_2,str_3)
        try:#判断打开文件是否出错
#                 QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
#             cur.execute("select %s \t from %s \t where id=%s \tand " %(str_3,str_1,str_2)),here id=yeas_2017 
            cur.execute("select * from user_table")
            res = cur.fetchall()
            length=len(res)
            for i in range(length):
                str="\t  ".join(res[i])
                self.textBrowser.append(str)
            cur.close()
            conn.close()
#                 QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        except Exception as err:
#             print("laji")
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

