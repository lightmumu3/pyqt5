'''
https://zhuanlan.zhihu.com/p/75673557
'''
import  sys
from  PyQt5.QtWidgets import QApplication ,QLabel

if __name__=='__main__':
    app = QApplication(sys.argv)   # 实例化Qapplication,传入sys.argv参数
    # label = QLabel('学习第一课6.15')  #实例化控件，也可以后面传递参数
    label = QLabel()
    label.setText('<font color = "red">Hello</font> <h1>World</h1>')
    label.show()                        #默认控件隐藏，这里让他显示
    sys.exit(app.exec())           #参数是执行应用让他循环,sys.exit()是退出



