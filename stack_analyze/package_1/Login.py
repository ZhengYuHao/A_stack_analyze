'''
Created on 2018年5月23日

@author: Administrator
'''
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from package_1 import title
# import untitled
class LoginDialog(QDialog):
    def __init__(self, parent=None):
        # self.setObjectName("QDialog")
        self.name=' '
        QDialog.__init__(self, parent)
        
        self.setWindowTitle('登录注册')
        self.setWindowIcon(QtGui.QIcon("MainWindow_1.png"))
        self.resize(478,412)
        self.setStyleSheet("background-color: rgb(72, 91, 97);")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("用户名:")
        self.label.setGeometry(QtCore.QRect(110, 140, 71, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0,0,0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)


        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("密码:")
        self.label_2.setGeometry(QtCore.QRect(110, 210, 71, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0,0,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("大 话 财 报")
        self.label_3.setGeometry(QtCore.QRect(190, 50, 251, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(176, 204, 207);\n"
                                   "font-size:20px")
        # self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.user = QtWidgets.QLineEdit(self)
        # self.user.move(125, 20)
        self.user.setText('orange')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.user.setFont(font)
        self.user.setStyleSheet("color: rgb(176, 204, 207);")
        self.user.setGeometry(QtCore.QRect(180, 140, 180, 35))

        self.pwd = QtWidgets.QLineEdit(self)
        # self.pwd.move(125, 60)
        self.pwd.setText('123')
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setFont(font)
        self.pwd.setStyleSheet("color: rgb(176, 204, 207);")
        self.pwd.setGeometry(QtCore.QRect(180, 210, 180, 35))

        self.loginBtn = QtWidgets.QPushButton('登录', self)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color: rgb(0,0,0);")
        self.loginBtn.setGeometry(QtCore.QRect(100, 300, 120, 40))
        self.loginBtn.clicked.connect(self.login) # 绑定方法判断用户名和密码

        self.signInBtn=QtWidgets.QPushButton('注册', self)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.signInBtn.setFont(font)
        self.signInBtn.setStyleSheet("color: rgb(0,0,0);")
        self.signInBtn.setGeometry(QtCore.QRect(250, 300, 120, 40))
        self.signInBtn.clicked.connect(self.only) # 绑定方法判断用户名和密码

    def signIn(self):
        print("3")
        conn = sqlite3.connect(r'db\user_ab.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        user_name = self.user.text()
        user_pwd = self.pwd.text()
        print("3")
        sql_1="create table if not exists user_table(user_name varchar(128), user_pwd varchar(128))"
        cur.execute(sql_1)
        sql ="INSERT INTO user_table (user_name,user_pwd) VALUES (:d1,:d2)"
        print("3")
        cur.execute(sql,{'d1':user_name,'d2':user_pwd})
        conn.commit()
        cur.close()
        conn.close()

    def login(self):
        conn = sqlite3.connect(r'db\user_ab.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        data=cur.execute("select * from user_table")
        user_name=self.user.text()#获取输入框用户名
        user_pwd=self.pwd.text()
        tell=True
        for i in data:
            if user_name==i[0]:
                if user_name==i[0] and user_pwd==i[1]:
                    self.accept()
                    self.name=user_name
                    QtWidgets.QMessageBox.information(self,"您好","登录成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
                    tell=False
                    break
                elif user_name==i[0] and user_pwd!=i[1]:
                    QtWidgets.QMessageBox.critical(self, '错误', '密码错误')
                    tell=False
                    break
        if tell==True:
            QtWidgets.QMessageBox.critical(self, '错误', '没有该用户')

    def only(self):#函数用于确保注册账户已经存在时的处理
        conn = sqlite3.connect(r'db\user_ab.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        data=cur.execute("select * from user_table")
        user_name=self.user.text()#获取输入框用户名
        user_pwd=self.pwd.text()
        a=[]
        for item in data:
            a.insert(-1,item[0])
        if user_name in a:
            QtWidgets.QMessageBox.critical(self, '错误', '该用户名已经被使用了')
        elif user_name not in a:
            print("1")
            self.signIn()
            print("2")
            QtWidgets.QMessageBox.information(self,"提示","注册成功",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        cur.close()
        conn.close()
#             QtWidgets.QMessageBox.information(self,"提示","注册成功"，QtWidgets.QMessageBox.Yes |QtWidgets.QMessageBox.No)
            
            
            