# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pic.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
# from package_1 import pic_draw
import sqlite3
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sqlite3
from matplotlib.font_manager import FontManager
from pylab import mpl
import subprocess
import os
from package_1 import Login


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        QDialog.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 704)
        Dialog.setToolTipDuration(1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 640, 480))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 10, 218, 168))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        
        self.remove_pic()
        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.set_pic)
        self.pushButton_2.clicked.connect(self.remove_pic)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "公司名"))
        self.comboBox.setItemText(0, _translate("Dialog", "资产负债率"))
        self.comboBox.setItemText(1, _translate("Dialog", "长期资金占不动产/厂房及设备比率"))
        self.comboBox.setItemText(2, _translate("Dialog", "流动比率"))
        self.comboBox.setItemText(3, _translate("Dialog", "速动比率"))
        self.comboBox.setItemText(4, _translate("Dialog", "应收款项周转率"))
        self.comboBox.setItemText(5, _translate("Dialog", "应收账款周转天数"))
        self.comboBox.setItemText(6, _translate("Dialog", "存货周转率"))
        self.comboBox.setItemText(7, _translate("Dialog", "存货周转天数"))
        self.comboBox.setItemText(8, _translate("Dialog", "固定资产周转率"))
        self.comboBox.setItemText(9, _translate("Dialog", "资产收益率"))
        self.comboBox.setItemText(10, _translate("Dialog", "净资产收益率"))
        self.comboBox.setItemText(11, _translate("Dialog", "税前纯益占实收资本比率"))
        self.comboBox.setItemText(12, _translate("Dialog", "生意完整周期"))
        self.comboBox.setItemText(13, _translate("Dialog", "总资产周转率"))
        self.comboBox.setItemText(14, _translate("Dialog", "EPS_每股收益"))
        self.comboBox.setItemText(15, _translate("Dialog", "营收增长率"))
        self.comboBox.setItemText(16, _translate("Dialog", "净利润增长率"))
        self.comboBox.setItemText(17, _translate("Dialog", "净资产增长率"))
        self.comboBox.setItemText(18, _translate("Dialog", "现金流量比率"))
        self.comboBox.setItemText(19, _translate("Dialog", "现金流量允当比率"))
        self.comboBox.setItemText(20, _translate("Dialog", "现金再投资比率"))
        self.comboBox.setItemText(21, _translate("Dialog", "毛利率"))
        self.comboBox.setItemText(22, _translate("Dialog", "营业利润率"))
        self.comboBox.setItemText(23, _translate("Dialog", "净利润率"))
        self.comboBox.setItemText(24, _translate("Dialog", "营业费用率"))
        self.comboBox.setItemText(25, _translate("Dialog", "经营安全边际率 "))
        self.comboBox.setItemText(26, _translate("Dialog", "现金与约当现金比率"))
        self.comboBox.setItemText(27, _translate("Dialog", "应收款项(占总资产%)"))
        self.comboBox.setItemText(28, _translate("Dialog", "存货(占总资产%)"))
        self.comboBox.setItemText(29, _translate("Dialog", "流动资产(占总资产%)"))
        self.comboBox.setItemText(30, _translate("Dialog", "非流动资产"))
        self.comboBox.setItemText(31, _translate("Dialog", "总资产(占总资产%)"))
        self.comboBox.setItemText(32, _translate("Dialog", "应付款项(占总资产%)"))
        self.comboBox.setItemText(33, _translate("Dialog", "流动负债(占总资产%)"))
        self.comboBox.setItemText(34, _translate("Dialog", "非流动负债(占总资产%)"))
        self.comboBox.setItemText(35, _translate("Dialog", "股东权益(占总资产%)"))
        self.comboBox.setItemText(36, _translate("Dialog", "负债和所有者权益(占总资产%)"))
        self.radioButton_2.setText(_translate("Dialog", "散点图"))
        self.radioButton.setText(_translate("Dialog", "坐标图"))
        self.pushButton.setText(_translate("Dialog", "开始绘制"))
        self.pushButton_2.setText(_translate("Dialog", "清初图片"))
        
    def remove_pic(self): 
#         query=Login.LoginDialog()
#         query.exec_()
        pixmap = QtGui.QPixmap ("MainWindow_1.png")
        self.label_2.setPixmap (pixmap)  # 在label上显示图片  
        self.label_2.setScaledContents (True)  # 让图片自适应label大小

    def set_pic(self):
        self.name=self.lineEdit.text()#获取公司名
        self.num=self.comboBox.currentIndex()
        self.tell=0
        if self.radioButton.isChecked():
            self.tell=1
        elif self.radioButton_2.isChecked():
            self.tell=2
        conn = sqlite3.connect(r'db\dataBase.db')
        conn.isolation_level = None
        conn.commit()
        cur = conn.cursor()
        try:#判断打开文件是否出错
        #                 QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
            cur.execute("select * from %s" % self.name)
            res = cur.fetchall()
            row = len(res)  # 数据库表中总行数
            cown = len(res[0])  # 数据库中每行的列i ==35 or
#             a=[]
            i=int(self.num)
            name=res[i][0]
            print(name)
            y=res[i][1:]
            y=list(y)
            for j in range(len(y)):
                y[j]=float(y[j])
#             a.append(y)
            print(y)
            if self.tell==2:
                
                self.graphic_1(y,name,self.name)
            elif self.tell==1:
                self.graphic_2(y,name,self.name)
            elif self.tell==0:
                QtWidgets.QMessageBox.critical(self, '错误', '您没有没有选择任何一种图形绘制或公司')
            cur.close()
            conn.close()
#                         QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        except Exception as err:
            QtWidgets.QMessageBox.critical(self, '错误', '您没有没有选择任何一种图形绘制或公司')
            print(err) 

    def graphic_1(self,y,name,str):
        #设置X轴的文字
    #     set_matplot_zh_font()
        
        plt.figure(num=str)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置  
        plt.rcParams['axes.unicode_minus'] = False
        x=[2013,2014,2015,2016,2017]
        x=np.arange(2013,2018,1.0)
        plt.title(name)
        plt.xlabel("年份")
        #设置Y轴的文字
        plt.ylabel("比率/天数")
#         for i in y:
        y=np.array(y)
        plt.scatter(x,y)
    #     plt.plot(x,yy)
#         self.name=self.name+name
        plt.savefig("image/%s.jpg"%self.name) 
        pixmap = QtGui.QPixmap ("image/%s.jpg"%self.name)
        self.label_2.setPixmap (pixmap)  # 在label上显示图片  
        self.label_2.setScaledContents (True)  # 让图片自适应label大小
        my_file = "image/%s.jpg"%self.name
        if os.path.exists(my_file):
            #删除文件，可使用以下两种方法。
            os.remove(my_file)
#         plt.show()       
    def graphic_2(self,y,name,str):
        #设置X轴的文字
    #     set_matplot_zh_font()
        
        plt.figure(num=str)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置  
        plt.rcParams['axes.unicode_minus'] = False
        x=[2013,2014,2015,2016,2017]
        x=np.arange(2013,2018,1.0)
        plt.title(name)
        plt.xlabel("年份")
        #设置Y轴的文字
        plt.ylabel("比率/天数")
#         for i in y:
        y=np.array(y)
        plt.plot(x,y)
    #     plt.plot(x,yy)
#         self.name=self.name+name
        plt.savefig("image/%s.jpg"%self.name) 
        pixmap = QtGui.QPixmap ("image/%s.jpg"%self.name)
        self.label_2.setPixmap (pixmap)  # 在label上显示图片  
        self.label_2.setScaledContents (True)  # 让图片自适应label大小
#         import os
        my_file = "image/%s.jpg"%self.name
        if os.path.exists(my_file):
            #删除文件，可使用以下两种方法。
            os.remove(my_file)
    #os.unlink(my_file)
#         plt.show()       
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