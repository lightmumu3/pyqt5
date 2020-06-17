import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,\
    QVBoxLayout,QHBoxLayout,QSlider,QDial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

#9.1 滑动条QSlider     ##程序会自动崩溃
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo,self).__init__()
#         self.slider_1 = QSlider(Qt.Vertical,self)      # 0.1 设置滑动条为垂直的
#         self.slider_2 = QSlider(Qt.Horizontal,self)
#         self.widgets_init()
#         self.label = QLabel(self)
#         self.label.setText('0')  # 也可以直接放到定义中
#         self.label.setFont(QFont('Arial Black',22))  #1 给label 设置字体格式 Qfont包
#         self.layout_h = QHBoxLayout()
#         self.layout_v = QVBoxLayout()
#         self.layout_init()
#     def widgets_init(self):
#         # self.label.setText('0')
#         # self.label.setFont(QFont('Arial Black', 22))   ##1.2 为什么label不能放到这里呢
#         self.slider_1.setRange(0,120)
#         self.slider_2.setRange(0,120)
#         self.slider_1.valueChanged.connect(lambda : self.slider_func(self.slider_1))
#         ##2 传递参数， 为什么connect变色
#         self.slider_2.valueChanged.connect(lambda : self.slider_func(self.slider_2))
#     def slider_func(self,slider):
#         if slider == self.slider_1:
#             self.slider_2.setValue(self.slider_1.value())
#             self.label.setText(self.slider_1.value())
#         else:
#             self.slider_1.setValue(str(self.slider_2.value()))   # 3 str
#             self.label.setText(str(self.slider_2.value()))
#     def layout_init(self):
#         self.layout_h.addWidget(self.slider_1)
#         self.layout_h.addStretch(1)         #4 间距设置
#         self.layout_h.addWidget(self.label)
#         self.layout_h.addStretch(1)
#         self.layout_v.addWidget(self.slider_2 )
#         self.layout_v.addLayout(self.layout_h )
#         self.setLayout(self.layout_v)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())


# 9.2 表盘 Qdial

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle('QDial')                            # 1

        self.dial = QDial(self)
        self.dial.setFixedSize(100, 100)                        # 2 设定表盘的大小
        self.dial.setRange(0, 120)                              # 3   设定表盘的范围
        self.dial.setNotchesVisible(True)                       # 4   设定表盘的刻度
        self.dial.valueChanged.connect(self.on_change_func)     # 5   信号和槽

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
#
# ​9.3 小结
# 1. 可以看出QSlider和QDial用法都差不多；
#
# 2. Qt.QHorizontal和Qt.Vertical分别用来实现水平的滑动条和垂直的滑动条；
#
# 3. setWindowTitle()可以设置窗口标题，setFixedSize()可以固定窗口或控件大小。




























