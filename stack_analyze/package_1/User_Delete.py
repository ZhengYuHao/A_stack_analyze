# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_Delete.ui'
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
        Dialog.resize(224, 412)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 80, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 61, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 210, 181, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.delete_user)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Delete User"))
        self.label_2.setText(_translate("Dialog", "user_name:"))
        self.pushButton.setText(_translate("Dialog", "confirm to Delete"))
    def delete_user(self):
        conn = sqlite3.connect(r'db\user_ab.db')
        conn.isolation_level = None
        conn.commit()
        cur = conn.cursor()
#         print(str_1,str_2,str_3)
        user_name=self.lineEdit.text()#要删除的用户名
        try:#判断打开文件是否出错
#                 QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
#             cur.execute("select %s \t from %s \t where id=%s \tand " %(str_3,str_1,str_2)),here id=yeas_2017 
            cur.execute("delete  from user_table where user_name='%s'"%user_name)#DELETE FROM 表名称 WHERE 列名称 = 值
            
            cur.close()
            conn.close()
            QtWidgets.QMessageBox.information(self,"提示","删除成功")
        except Exception as err:
#             print("laji")
            QtWidgets.QMessageBox.information(self,"提示",'遇到一些错误，请您重试')
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


