import  sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QPushButton,\
    QWidget,QLineEdit,QGridLayout,QHBoxLayout,QVBoxLayout,QLabel,QDialog

USER_PWD= {'light':'password'}    #定义全局变量，作为密码
class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(300,100)
        self.setWindowTitle('周林光的练习_6.15')
        self.label1 = QLabel('username',self)   #添加wight的时候后面没有加self 有时候也没事
        self.label2 = QLabel('password',self)
        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.button1 = QPushButton('log in',self)
        self.button2 = QPushButton('sign in',self)

        self.g_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()       #将布局单独定义为函数调用，便于以后进行维护
        self.button_init()        #初始化button
        self.line_edit_init()       #初始化文字输入栏
        self.sign_in = Sign_in_page()    #实例化第二个类

    def layout_init(self):
        self.g_layout.addWidget(self.label1,0,0,1,1)
        self.g_layout.addWidget(self.edit1,0,1,1,1)
        self.g_layout.addWidget(self.label2,1,0,1,1)
        self.g_layout.addWidget(self.edit2,1,1,1,1)
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.v_layout.addLayout(self.g_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    #输入框功能的完善
    def line_edit_init(self):
        self.edit1.setPlaceholderText('请输入你的用户名')
        self.edit2.setPlaceholderText('请输入你的密码')
        self.edit2.setEchoMode(QLineEdit.Password)       #将文字输入变成密码格式

        self.edit1.textChanged.connect(self.check_input_func)   #有文字输入后调用函数使按钮可用
        self.edit2.textChanged.connect(self.check_input_func)
    #有输入的时候按钮可用
    def check_input_func(self):
        if self.edit1.text() and self.edit2.text():
            self.button1.setEnabled(True)
        else:
            self.button1.setEnabled(False)

    #按钮初始化-不可用&点击触发密码检查
    def button_init(self):
        self.button1.setEnabled(False)
        self.button1.clicked.connect(self.check_login_func)    #点击登录按钮触发检查密码函数
        self.button2.clicked.connect(self.sign_in_page)

    def sign_in_page(self):
        self.sign_in.exec_()                        #让实例化之后的类显示,不用 show()
    #密码检查函数（检查密码，完成检查后清空数值）
    def  check_login_func(self):
###什么意思呢---全局变量
        if USER_PWD.get(self.edit1.text()) == self.edit2.text():
            QMessageBox.information(self,'information','登录成功')
        else:
            QMessageBox.warning(self,'wrong','登录失败')
        self.edit1.clear()
        self.edit2.clear()

class Sign_in_page(QDialog):
    def __init__(self):
        super(Sign_in_page,self).__init__()
        self.sign_label1 = QLabel('注册你的用户名',self)
        self.sign_label2 = QLabel('注册密码',self)
        self.sign_label3 = QLabel('确认密码',self)
        self.sign_edit1 = QLineEdit(self)
        self.sign_edit2 = QLineEdit(self)
        self.sign_edit3 = QLineEdit(self)
        self.sign_button1 = QPushButton('注册',self)
        # self.sign_button2 = QPushButton(self)

        self.sign_g_box = QGridLayout()
        self.sign_h_box = QHBoxLayout()
        self.sign_v_box = QVBoxLayout()

        self.sign_layout_init()
        self.sign_button_init()
        self.sign_edit_init()

    def sign_layout_init(self):
        self.sign_g_box.addWidget(self.sign_label1,0,0,1,1)
        self.sign_g_box.addWidget(self.sign_edit1, 0, 1, 1, 1)
        self.sign_g_box.addWidget(self.sign_label2,1,0,1,1)
        self.sign_g_box.addWidget(self.sign_edit2, 1, 1, 1, 1)
        self.sign_g_box.addWidget(self.sign_label3, 2, 0, 1, 1)
        self.sign_g_box.addWidget(self.sign_edit3, 2, 1, 1, 1)
        self.sign_h_box.addWidget(self.sign_button1)

        self.sign_v_box.addLayout(self.sign_g_box)
        self.sign_v_box.addLayout(self.sign_h_box)
        self.setLayout(self.sign_v_box)

    def sign_edit_init(self):
        self.sign_edit1.setPlaceholderText('请输入用户名')
        self.sign_edit2.setPlaceholderText('输入注册密码')
        self.sign_edit3.setPlaceholderText('确认密码')

        self.sign_edit1.textChanged.connect(self.sign_check_input_func)
        self.sign_edit2.textChanged.connect(self.sign_check_input_func)
        self.sign_edit3.textChanged.connect(self.sign_check_input_func)

    def sign_button_init(self):
        self.sign_button1.setEnabled(False)
        self.sign_button1.clicked.connect(self.sign_check_info)

    def sign_check_input_func(self):
        if self.sign_edit1.text() and self.sign_edit2.text() and self.sign_edit3.text():
            self.sign_button1.setEnabled(True)
        else:
            pass

     ##相对来说最复杂：检查注册信息，通过信息来弹出不同的对话框并除去输入的东西
    def sign_check_info(self):
        if self.sign_edit3.text() != self.sign_edit2.text():
            QMessageBox.critical(self,'wrong','两次输入不同！')
        elif self.sign_edit1.text() in USER_PWD:
            QMessageBox.critical(self,'wrong','用户名已经被注册了！')
        else:
#############这一段是什么意思呢---全局变量
            USER_PWD[self.sign_edit1.text()] = self.sign_edit2.text()
            QMessageBox.information(self,'sucess','注册成功')
        self.sign_edit1.clear()
        self.sign_edit2.clear()
        self.sign_edit3.clear()


if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

# 5.5 小结
# 1. setPlaceholderText()方法用于在输入框显示浅灰色的提示文本；
#
# 2. exec_()方法可以让窗口成为模态窗口，而调用show()方法，窗口是非模态的。模态窗口将程序控制权占据，只有对当前窗口关闭后才能操作其他窗口；
#
# 3. QDialog有exec_()方法，而QWidget没有；
#
# 4. 可以用setEchoMode(QLineEdit.Password)将普通输入框中的文字变成原点







