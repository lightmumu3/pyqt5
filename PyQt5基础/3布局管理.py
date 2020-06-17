import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QGridLayout,QFormLayout,QWidget,QLabel,QLayout,QVBoxLayout,QHBoxLayout,QLineEdit


#3.1 垂直布局QVBoxLayout
# class Demo1(QWidget):
#     def __init__(self):
#         super(Demo1,self).__init__()
#         self.label1 = QLabel('开始',self)
#         self.label2 = QLabel('结束',self)
#         self.label3 = QLabel('重开',self)
#
#         self.v_layout = QVBoxLayout()
#         self.v_layout.addWidget(self.label1)
#         self.v_layout.addWidget(self.label2)
#         self.v_layout.addWidget(self.label3)
#
#         self.setLayout(self.v_layout)
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo1 = Demo1()
#     demo1.show()
#     sys.exit(app.exec_())


#3.2 水平布局QHBoxLayout
# class Demo2(QWidget):
#     def __init__(self):
#         super(Demo2,self).__init__()
#         self.line_edit = QLineEdit()
#         self.label = QLabel('请输入文字')
#         self.hboxlayout = QHBoxLayout()
#         self.hboxlayout.addWidget(self.label)
#         self.hboxlayout.addWidget(self.line_edit)
#
#         self.setLayout(self.hboxlayout)
# #
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo2 = Demo2()
#     demo2.show()
#     sys.exit(app.exec_())


#​3.3 混合使用QVBoxLayout和QHBoxLayout
# class Demo3(QWidget):
#     def __init__(self):
#         super(Demo3,self).__init__()
#         self.label1 = QLabel('Username',self)
#         self.label2 = QLabel('Password',self)
#         self.button1 = QPushButton('log in',self)
#         self.button2 = QPushButton('sign in',self)
#         self.edit1 = QLineEdit()
#         self.edit2 = QLineEdit()
#         self.hbox1 = QHBoxLayout()
#         self.hbox2 = QHBoxLayout()
#         self.hbox3 = QHBoxLayout()
#         self.vbox = QVBoxLayout()
#
#         self.hbox1.addWidget(self.label1)
#         self.hbox1.addWidget(self.edit1)
#         self.hbox2.addWidget(self.label2)
#         self.hbox2.addWidget(self.edit2)
#         self.hbox3.addWidget(self.button1)
#         self.hbox3.addWidget(self.button2)
#         self.vbox.addLayout(self.hbox1)
#         self.vbox.addLayout(self.hbox2)
#         self.vbox.addLayout(self.hbox3)
#
#         self.setLayout(self.vbox)
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo3=Demo3()
#     demo3.show()
#     sys.exit(app.exec_())

#3.4 表单布局 QFormLayout
# class Demo4(QWidget):
#     def __init__(self):
#         super(Demo4,self).__init__()
#         self.label1 = QLabel('Username',self)
#         self.label2 = QLabel('Password',self)
#         self.button1 = QPushButton('log in',self)
#         self.button2 = QPushButton('sign in',self)
#         self.edit1 = QLineEdit()
#         self.edit2 = QLineEdit()
#
#         self.flayout = QFormLayout()
#         self.hbox = QHBoxLayout()
#         self.vbox = QVBoxLayout()
#
#         self.flayout.addRow(self.label1,self.edit1)
#         self.flayout.addRow(self.label2,self.edit2)
#         self.hbox.addWidget(self.button1)
#         self.hbox.addWidget(self.button2)
#         self.vbox.addLayout(self.flayout)
#         self.vbox.addLayout(self.hbox)
#         self.setLayout(self.vbox)
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo4=Demo4()
#     demo4.show()
#     sys.exit(app.exec_())



#3.5网格布局
class Demo5(QWidget):
    def __init__(self):
        super(Demo5,self).__init__()
        self.label1 = QLabel('Username',self)
        self.label2 = QLabel('Password',self)
        self.button1 = QPushButton('log in',self)
        self.button2 = QPushButton('sign in',self)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()

        self.glayout = QGridLayout()
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.glayout.addWidget(self.label1,0,0)
        self.glayout.addWidget(self.edit1, 0, 1)
        self.glayout.addWidget(self.label2, 1, 0)
        self.glayout.addWidget(self.edit2, 1, 1)
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.button2)
        self.vbox.addLayout(self.glayout)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
if __name__=='__main__':
    app = QApplication(sys.argv)
    demo5=Demo5()
    demo5.show()
    sys.exit(app.exec_())

# 3.6 小结
# 1. QLineEdit控件为单行文本输入框；
#
# 2.. 了解四种布局方式：垂直布局QVBoxLayout、水平布局QHBoxLayout、
# 表单布局QFormLayout和网格布局QGridLayout；
#
# 3. addWidget()方法用来添加控件，addLayout()方法用来添加布局；
#
# 4. 请记住QGridLayout的addWidget()语法形式：
#
# addWidget(widget, row, column, rowSpan, columnSpan)























