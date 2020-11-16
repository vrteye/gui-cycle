import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *


class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.tj)  # 建立信号和槽，button_2即为按钮2的objectName，tj为槽也就是自定义的方法
        self.pushButton_3.clicked.connect(self.close)  # close为内置方法（关闭）

    def tj(self):
        print('正在点击按钮2')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
