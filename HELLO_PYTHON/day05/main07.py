import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("main07.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.le_mine.returnPressed.connect(self.click)
        self.show()

    def click(self):
        me = self.le_mine.text()
        comArr = ['가위', '바위', '보']
        rst = ""
        com = comArr[int(random()*3)]
        
        if (me == "가위" and com == "바위") or (me == "바위" and com == "보") or (me == "보" and com == "가위") :         
            rst = "컴퓨터가 이겼당"
        elif me == com :
            rst = "비겼당"
        else :
            rst = "내가 이겼당"
        
        self.le_com.setText(com)
        self.le_result.setText(rst)
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()