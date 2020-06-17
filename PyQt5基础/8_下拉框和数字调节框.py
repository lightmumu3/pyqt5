import  sys
from PyQt5.QtWidgets import QApplication,QSpinBox,QDoubleSpinBox,QWidget,QComboBox,QMessageBox,QFontComboBox,QLineEdit,QVBoxLayout

#8.1 下拉框
# class Demo(QWidget):
#     choice = 'a'                                  #1 设置全局变量，list 传参
#     choice_list = ['b','c','d','e']
#
#
#     def __init__(self):
#         super(Demo,self).__init__()
#
#         self.combox_1 = QComboBox(self)
#         self.combox_2 = QFontComboBox(self)
#         self.line_edit = QLineEdit(self)
#         self.v_layout   = QVBoxLayout()
#
#
#         self.layout_init()
#         self.combox_init()
#
#     def layout_init(self):
#         self.v_layout.addWidget(self.combox_1)
#         self.v_layout.addWidget(self.combox_2)
#         self.v_layout.addWidget(self.line_edit)
#         self.setLayout(self.v_layout)
#
#     def combox_init(self):
#         self.combox_1.addItem(self.choice)   #2 传入默认参数
#         self.combox_1.addItems(self.choice_list)        #3 下拉列表的参数设置
#         self.combox_1.currentIndexChanged.connect(lambda : self.combox_func(self.combox_1))
#       #4 下拉框的参数变化触发currentindexchanged 条件
#         self.combox_2.currentFontChanged.connect(lambda: self.combox_func(self.combox_2))
#       ##5 字体变化触发currentfontchanged    ???为什么不能改变字体呢
#     def combox_func(self,combox):
#         if combox == self.combox_1:
#             QMessageBox.information(self,'combox_1','{}0000{}'.format(combox.currentIndex(),combox.currentText()))
#         else:
#             self.line_edit.setText(combox.currentFont())        ##6 设置框的字体为下拉框的当前字体
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

#8.2数字调节框   Qspinbox  Qdoublespinbox

class Demo2(QWidget):
    def __init__(self):
        super(Demo2,self).__init__()

        self.spinbox_1 = QSpinBox(self)    #1实例化
        self.spinbox_2 = QDoubleSpinBox(self)       #实例化
        self.spinbox_init()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.spinbox_1)
        self.v_layout.addWidget(self.spinbox_2)
        self.setLayout(self.v_layout)
    def spinbox_init(self):
        self.spinbox_1.setRange(0,100)     #2   范围
        self.spinbox_1.setSingleStep(1)     #3   步长
        self.spinbox_1.setValue(50)       #4    初始值
        #数字发生变化触发valuechange信号
        self.spinbox_1.valueChanged.connect(self.spinbox_func)  #5调用函数self.func 不能加（）

        self.spinbox_2.setRange(0,100)
        self.spinbox_2.setSingleStep(0.001)     #6  小数默认两位
        self.spinbox_2.setDecimals(3)       #7  设置小数位数
        self.spinbox_2.setValue(50)

    def spinbox_func(self):
        decimal = self.spinbox_2.value()-int(self.spinbox_2.value())
        self.spinbox_2.setValue(self.spinbox_1.value() + decimal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo2()
    demo.show()
    sys.exit(app.exec_())

# 8.3 小结
# 1. 下拉框介绍了QComboBox和QFontComboBox，后者是从前者继承并专门用来给用户选择字体的控件。
#
# 2. 添加选项内容方法为addItem()和addItems()，后者添加可循环对象；
#
# 3. 当下拉框当前选项发生改变的时候，会触发currentIndexChanged和currentTextChanged信号；
#
# 4. setFont()方法可以用来设置一些控件的字体；
#
# 5. 数字调节框介绍了QSpinBox和QDoubleSpinBox，前者调节整型数字，后者调节浮点型数字；
#
# 6. 当调节框数字发生改变时，会触发valueChanged信号；
#
# 7. setRange()方法用来设置范围，setSingleStep()方法用来设置步长，setValue()方法用来设置初始值。​




















