# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from package_1 import main
# from comtypes.test.test_ie import MSG
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 285)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 90, 111, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(Dialog)
#         self.pushButton.setGeometry(QtCore.QRect(100, 150, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.clicked.connect()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "error"))
        self.label.setText(_translate("Dialog", "数据库中没有该公司"))
#         self.pushButton.setText(_translate("Dialog", "返回"))
#     def retur(self):
        
        
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