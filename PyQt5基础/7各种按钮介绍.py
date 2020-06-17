import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QPushButton,QLabel,QToolButton,QRadioButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

# class Demo(QWidget):
#     def __init__(self):
#         super(Demo ,self).__init__()
#         self.button = QPushButton('确定',self)
#         self.button.setCheckable(True)           # 将按钮设置为一个可标记的按钮
#         self.button.setIcon(QIcon('金色icon.jpg'))   #给按钮添加背景
#         self.button.toggled.connect(self.button_state_func)   #按钮标记状态变化会发出toggle信号
#     def button_state_func(self):
#         print(self.button.isChecked())
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

#Qtoolbutton 一般只是一个按钮没有文本
# class Demo2(QWidget):
#     def __init__(self):
#         super(Demo2,self).__init__()
#         self.button = QToolButton(self)
#         self.button.setCheckable(True)
#         self.button.setIcon(QIcon('金色icon.jpg'))
#         self.button.toggled.connect(self.button_state_func)
#     def button_state_func(self):
#         print(self.button.isChecked())
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo2 = Demo2()
#     demo2.show()
#     sys.exit(app.exec_())


#7.3 radiobutton 单选按钮
class Demo3(QWidget):
    def __init__(self):
        super(Demo3,self).__init__()
        self.resize(300,300)           #为什么不起作用呢
        self.button1 = QRadioButton('11',self)
        self.button2 = QRadioButton('22',self)
        self.label = QLabel(self)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        # self.label.setPixmap(QPixmap('111.jpg'))


        self.layout_init()
        self.button_init()
        self.label_init()
    def label_init(self):
        self.label.setPixmap(QPixmap('images/111.jpg'))
    def button_init(self):
        self.button1.setCheckable(True)
        self.button1.toggled.connect(self.button_click_func)   #一个被选中那么另一个一定不选
    def button_click_func(self):
        if self.button1.isChecked():

            self.label.setPixmap(QPixmap('images/222.jpg'))
        else:
            self.label.setPixmap(QPixmap('images/111.jpg'))

    def layout_init(self):
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
if __name__=='__main__':
    app = QApplication(sys.argv)
    demo3 = Demo3()
    demo3.show()
    sys.exit(app.exec_())

#7.4 checkbox
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.checkbox1 = QCheckBox('Checkbox 1', self)
#         self.checkbox2 = QCheckBox('Checkbox 2', self)
#         self.checkbox3 = QCheckBox('Checkbox 3', self)
#
#         self.v_layout = QVBoxLayout()
#
#         self.checkbox_init()
#         self.layout_init()
#
#     def layout_init(self):
#         self.v_layout.addWidget(self.checkbox1)
#         self.v_layout.addWidget(self.checkbox2)
#         self.v_layout.addWidget(self.checkbox3)
#
#         self.setLayout(self.v_layout)
#
#     def checkbox_init(self):
#         self.checkbox1.setChecked(True)                                                             # 1
#         # self.checkbox1.setCheckState(Qt.Checked)                                                  # 2
#         self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))      # 3
#
#         self.checkbox2.setChecked(False)
#         # self.checkbox2.setCheckState(Qt.Unchecked)
#         self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))
#
#         self.checkbox3.setTristate(True)        #让按钮有三种状态                                                       # 4
#         # self.checkbox3.setCheckState(Qt.PartiallyChecked)                                           # 5
#         self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))
# #因为槽函数带有参数，因此connect中加入lambda 表达式
#     def on_state_change_func(self, checkbox):                                                       # 6
#         print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

# 7.5 小结
# 1. QPushButton和QToolButton非常相似，不过QToolButton更多是与QToolBar搭配使用，用来显示工具图片；
#
# 2. 可以通过setIcon()方法来给按钮设置图标；可以用setPixmap()方法给QLabel控件设置图片；
#
# 3. toogled信号在按钮状态发生改变时发出；stateChanged也是，不过该信号用于QCheckBox；
#
# 4. QRadioButton单选按钮只能进行多选一操作，即每次只会有一个单选按钮被选中；
#
# 5. 如果要让QCheckBox拥有三种状态的话，则需要通过setTristate(True)方法来设置；
#
# 6. 若要连接带有参数的自定义槽函数，可以通过lambda表达式来完成























