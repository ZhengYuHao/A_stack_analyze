# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from package_1 import User_Delete,User_info,new_company,Modify_data,Drop_table
class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        QDialog.__init__(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 404)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 170, 141, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        
        self.pushButton.clicked.connect(self.jump_user_infor)
        self.pushButton_2.clicked.connect(self.jump_modify)
        self.pushButton_3.clicked.connect(self.jump_user_Delete)
        self.pushButton_4.clicked.connect(self.jump_new_company)
        self.pushButton_5.clicked.connect(self.jump_Drop_table)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Administrator"))
        self.pushButton.setText(_translate("Dialog", "查看用户信息"))
        self.pushButton_3.setText(_translate("Dialog", "删除用户"))
        self.pushButton_2.setText(_translate("Dialog", "修改数据文件"))
        self.pushButton_4.setText(_translate("Dialog", "增加数据库文件"))
        
        self.pushButton_5.setText(_translate("Dialog", "删除数据库文件"))
        
    def jump_user_infor(self):
        query=User_info.query_interface()
        query.exec_()
    def jump_user_Delete(self):
        query=User_Delete.query_interface()
        query.exec_()
    def jump_new_company(self):
        query=new_company.query_interface()
        query.exec_()
    def jump_modify(self):
        query=Modify_data.query_interface()
        query.exec_()
    def jump_Drop_table(self):
        query=Drop_table.query_interface()
        query.exec_()
    
        
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