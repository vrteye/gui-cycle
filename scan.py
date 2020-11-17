import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from lks import *


class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.onButtonClick)  # 建立信号和槽，button_2即为按钮2的objectName，tj为槽也就是自定义的方法
        # self.pushButton_3.clicked.connect(self.close)  # close为内置方法（关闭）
        self.lineEdit1.textChanged.connect(self.textchanged)
        self.radioButton1.
    def onButtonClick(self):
        sender = self.sender()
        print(sender.text() + ' 被按下了')

    def textchanged(self, text):
        print("输入的内容为: " + text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
