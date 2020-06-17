import  sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt5.QtCore import pyqtSignal

#2.1基础的槽操作
class Demo1(QWidget):
    def __init__(self):                                                     #1. 初始化继承
        super(Demo1,self).__init__()                                        #2. 自身初始化
        self.button = QPushButton('start',self)                             #3. 实例化button，不要忘记self
        self.button.clicked.connect(self.change_text)                       #4. 点击之后调用函数

    def change_text(self):                                                  #5. 自定义函数
        print('change text')
        self.button.setText('stop')
        self.button.clicked.disconnect(self.change_text)                    #6. 点击之后断开连接

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo1 = Demo1()
    demo1.show()
    sys.exit(app.exec_())



#2.2多个信号连接一个槽（将clicked 改为 pressed 和released)
class Demo2(QWidget):
    def __init__(self):
        super(Demo2,self).__init__()
        self.button = QPushButton('start',self)
        self.button.pressed.connect(self.change_text)                      #1. 将时间触发条件由clicked改为 pressed
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'start':
            self.button.setText('stop')
        else:
            self.button.setText('start')

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo2 = Demo2()
    demo2.show()
    sys.exit(app.exec_())
#


#2.3信号之间的连接:实现和2.2一样的功能
class Demo3(QWidget):
    def __init__(self):
        super(Demo3,self).__init__()
        self.button = QPushButton('start',self)
        self.button.pressed.connect(self.button.released)               #1. 信号传递
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text()=='start':
            self.button.setText('stop')
        else:
            self.button.setText('start')
if __name__=='__main__':
    app = QApplication(sys.argv)
    demo3=Demo3()
    demo3.show()
    sys.exit(app.exec_())



#2.4一个信号连接多个槽
class Demo4(QWidget):
    def __init__(self):
        super(Demo4,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('初始的')
        self.button = QPushButton('start',self)
        self.button.clicked.connect(self.func1)
        self.button.clicked.connect(self.func2)
        self.button.clicked.connect(self.func3)
    def func1(self):
        self.button.setText('stop')
        self.button.clicked.disconnect(self.func1)
    def func2(self):
        self.setWindowTitle('变化了')
        self.button.clicked.disconnect(self.func2)
    def func3(self):
        self.resize(400,400)
        self.button.clicked.disconnect(self.func3)
if __name__=='__main__':
    app = QApplication(sys.argv)
    demo4=Demo4()
    demo4.show()
    sys.exit(app.exec_())


#2.5自定义信号
class Demo5(QWidget):
    mysignal = pyqtSignal()                                      #1. 自定义信号的全局变量
    def __init__(self):
        super(Demo5,self).__init__()
        self.label =QLabel('hello',self)
        self.mysignal.connect(self.func)                        #2.1 信号的槽的设置
    def func(self):                                             #2.2 槽函数
        if self.label.text()=='hello':
            self.label.setText('world')
        else:
            self.label.setText('hello')
    def mousePressEvent(self, QMouseEvent):                     #注意这个def是系统中的，大小写不能写错
        self.mysignal.emit()                                    #2.3 信号触发机制 函数
if __name__=='__main__':
    app = QApplication(sys.argv)
    demo5 = Demo5()
    demo5.show()
    sys.exit(app.exec_())

# 2.6 小结
# 1. 可以将信号和槽视作裁片鸣枪与选手开跑，信号发出，则相应连接的槽函数启动；
# 2. 单个信号可以连接单个槽；单个信号可以连接多个槽；多个信号可以连接单个槽；
# 信号可以与信号连接；也可以自定义信号；
# 3. mousePressEvent()方法是许多控件自带的方法，用来监测鼠标是否被按下。




