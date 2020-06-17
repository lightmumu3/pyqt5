import sys
from PyQt5.QtCore import QDate, Qt,QDateTime,QTime
from PyQt5.QtWidgets import QApplication,QDateTimeEdit,QDateEdit,QTimeEdit,\
    QWidget, QCalendarWidget, QLabel, QVBoxLayout


#12.1 日历 QCalendarWidget
EMOTION = {
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́) ✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946, 2, 14))  # 2 设置最小的日期
        self.calendar.setMaximumDate(QDate(2020, 7, 10))  # 3
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
        # self.calendar.setFirstDayOfWeek(Qt.Monday)         # 4 设置周几为周的第一天
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))   # 5 设置当前显示的日期
        self.calendar.setGridVisible(True)  # 6
        self.calendar.clicked.connect(self.show_emotion_func)  # 6 和button 一样 点击就触发

        print(self.calendar.minimumDate())  # 7
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel(self)  # 8
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')  ## 9先获取选中的日期，然后转化为周几
        self.label.setText(EMOTION[weekday])     # 10 显示全局变量中的内容

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):  # 10
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

#12.2   QDateTimeEdit

# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.datetime_1 = QDateTimeEdit(self)                                           # 1
#         self.datetime_1.dateChanged.connect(lambda: print('Date Changed!'))  #触发条件：datechanged
#
#         self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)# 2 传入当前日期
#         self.datetime_2.setDisplayFormat('yyyy--MM---dd HH:mm:ss')   #设置日期显示格式
#         self.datetime_2.timeChanged.connect(lambda: print('Time Changed!')) #触发条件：timechanged
#         # print(self.datetime_2.date())
#         # print(self.datetime_2.time())
#         # print(self.datetime_2.dateTime())
#
#         self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)              # 3
#         self.datetime_3.dateTimeChanged.connect(lambda: print('DateTime Changed!'))
#         self.datetime_3.setCalendarPopup(True)  # 将调节框变成 日历框
#
#         self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)                      # 4
#         self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)
#
#         self.date = QDateEdit(QDate.currentDate(), self)                                # 5
#         self.date.setDisplayFormat('yyyy/MM/dd')
#         print(self.date.date())
#
#         self.time = QTimeEdit(QTime.currentTime(), self)                                # 6
#         self.time.setDisplayFormat('HH:mm:ss')
#         print(self.time.time())
#
#         self.v_layout = QVBoxLayout()
#         self.v_layout.addWidget(self.datetime_1)
#         self.v_layout.addWidget(self.datetime_2)
#         self.v_layout.addWidget(self.datetime_3)
#         self.v_layout.addWidget(self.datetime_4)
#         self.v_layout.addWidget(self.datetime_5)
#         self.v_layout.addWidget(self.date)
#         self.v_layout.addWidget(self.time)
#
#         self.setLayout(self.v_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

# ​12.3 小结
# 1. QCalendarWidget为日历控件，用户可以设置日期范围，可以设置日
# 历初始化时显示的日期(如果没有设置的话，默认为当天日期)；
#
# 2. QDateTimeEdit、QDateEdit以及QTimeEdit这三个控件用法差不多，读者
# 掌握QDateTimeEdit的话其他两种其实也就明白怎么使用了；
#
# 3. 通过setCalendarPopup(True)方法可以让QDateTimeEdit和QDateEdit显示日历。






































