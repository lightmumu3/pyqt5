import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QMessageBox,QPushButton
# 4.1 建立消息框
class demo1(QWidget):
    def __init__(self):
        super(demo1,self).__init__()
        self.button = QPushButton('information',self)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        choice = QMessageBox.critical(self,'Title','content',QMessageBox.Save | QMessageBox.Cancel)
            #QMessageBox.Ok,QMessageBox.Yes,QMessageBox.No,QMessageBox.Close,QMessageBox.Cancel
            # QMessage.Open,QMessage.Save
        #.information/ .question / .warning / .critical / .about

        # 4.2与消息框进行交互
        if choice == QMessageBox.Cancel:
            self.button.setText('取消')
        else:
            self.button.setText('保存')


if __name__=="__main__":
    app = QApplication(sys.argv)
    Demo1 = demo1()
    Demo1.show()
    sys.exit(app.exec_())

#4.3 小结
# 1. 消息框的种类有：
#
# information 信息框；question 问答框； warning 警告框； critical 错误框；
# about 关于框( 其实还有一个aboutQt框，是专门用来展示Qt软件信息的，这里不再讲述)。
#
# 2. 语法形式(buttons可以不用指定)：
#
# QMessageBox.information(QWidget, 'Title', 'Content', buttons)
# 3. 在与消息框交互的时候，可以用一个变量来保存消息框返回的按钮信息，接下来再用判断语句来作出不同的反应。​

