#6.1 同步显示文本
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QTextBrowser,QTextEdit,QLabel,QHBoxLayout,QVBoxLayout
class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.label1 = QLabel('QtextEdit',self)
        self.label2 = QLabel('QTextBrowser',self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)
        self.v_layout_1 = QVBoxLayout()
        self.v_layout_2 = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()   ###
    def layout_init(self):
        self.v_layout_1.addWidget(self.label1)
        self.v_layout_1.addWidget(self.text_edit)
        self.v_layout_2.addWidget(self.label2)
        self.v_layout_2.addWidget(self.text_browser)
        self.h_layout.addLayout(self.v_layout_1)
        self.h_layout.addLayout(self.v_layout_2)

        self.setLayout(self.h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.text_browser_func)

        ####为什么定义的函数找不到呢
        #因为这是类的方法，所以要冠之类名 self.



    def text_browser_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())
# 程序非常简单。通过实例化两个QLabel、一个QTextEdit以及一个QTextBrowser再通过垂直布局和水平布局就
# 可以完成整个界面。关键点是在信号和槽的连接上。

# 1. 将self.text_edit的textChanged信号连接到自定义的槽函数上。也就是说当self.text_edit中的
# 文本发生改变的时候，就会发出textChanged信号，然后调用show_text_func()槽函数。
# 2. 在槽函数中我们通过setText()方法将self.text_browser的文本设为self.text_edit的文本，
# 而self.text_edit的文本通过toPlainText()获取，而不是text().

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

# 6.2 小结
# 1. 顾名思义，QTextEdit为用来编辑文本，而QTextBrowser用来显示文本；
#
# 2. setText()用来设置文本，toPlainText()用来获取文本，这两个控件都有这些方法；
#
# 3. 浏览框会执行Html代码。











