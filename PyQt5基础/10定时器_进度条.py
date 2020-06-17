import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QGridLayout,QLabel,QProgressBar,QVBoxLayout,QPushButton

# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.label = QLabel('0',self)
#         self.label.setAlignment(Qt.AlignCenter)     # 1 将label放在中心，不用addstrench
#
#         self.step = 0                                #2 设置变量
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.timer_func2) ## timeout的作用:定时器每计数一次就调用一次函数
#         self.button = QPushButton('start',self)
#         self.button.clicked.connect(self.timer_func)
#
#         self.layout_v = QVBoxLayout()
#         self.layout_v.addWidget(self.label)
#         self.layout_v.addWidget(self.button)
#         self.setLayout(self.layout_v)
#     def timer_func(self):                   #定时器激活 就是不计数状态
#         if  self.timer.isActive():
#             self.button.setText('Start')
#             self.timer.stop()               #不计数
#         else:
#             self.button.setText('Stop')
#             self.timer.start(500)           #表示500ms 触发一次
#     def timer_func2(self):
#         self.step += 1
#         self.label.setText(str(self.step))
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

# 10.2 进度条 QProgressBar
class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.progross_bar = QProgressBar(self)
        self.button_1 = QPushButton('start',self)
        self.button_1.clicked.connect(self.button_func_1)
        self.button_2 = QPushButton('reset',self)
        self.button_2.clicked.connect(self.button_func_2)
        self.layout_h = QHBoxLayout()
        # self.layout_g.addItem(self.progross_bar,0,0,1,2)
        self.layout_h.addWidget(self.button_1)
        self.layout_h.addWidget(self.button_2)
        self.layout_v = QVBoxLayout()
        self.layout_v.addWidget(self.progross_bar)
        self.layout_v.addLayout(self.layout_h)
        self.setLayout(self.layout_v)

        self.progross_bar.setRange(0,100)
        self.step = 0                           # 定义变量
        self.timer = QTimer(self)               # 定义计时器
        self.timer.timeout.connect(self.JISHU)  #计时 触发
    def JISHU(self):
        self.step += 1
        self.progross_bar.setValue(self.step)           # 这里不能调用str
        if self.step >= 100:                        # 考虑满格的情况
            self.timer.stop()
            self.button_1.setText('start')

    def button_func_1(self):                    #  定时器的启动的暂停
        if self.button_1.text() == 'start':
            self.button_1.setText('stop')
            self.timer.start(100)
        else:
            self.button_1.setText('start')
            self.timer.stop()
    def button_func_2(self):                #定时器的复位
        self.button_1.setText('start')
        self.step = 0
        self.progross_bar.reset()
        self.timer.stop()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

# ​10.3 小结
# 1. QTimer定时器会根据设定的时间不断发出timeout信号并调用连接的槽函数，通过start(int)方法
# 来设置时间并启动定时器，stop()方法用于停止定时器；
#
# 2. 通过isActive()方法来判断定时器是否被激活，setSingleShot()方法可以在触发timeout信号后
# 只调用一次槽函数；
#
# 3. 通过setOrientation(Qt.Vertical)方法可以将进度条设为垂直显示；
#
# 4. setMinimum()和setMaximum()方法用来设置进度条范围(可以用setRange()替代)
# ，setValue()方法用于设置进度条的当前值，reset()方法用于重置进度条。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


















































