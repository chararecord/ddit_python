import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("main04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.show()

    def click(self):
        me = self.leMine.text()
        com = ""
        rst = ""
        
        print(me)
        
        ran = random()
        if ran > 0.5 :
            com = "홀"
        else :
            com = "짝"
        
        print(com)
        
        if me == com :
            rst = "이김"
        else :
            rst = "짐"
        
        self.leCom.setText(com)
        self.leResult.setText(rst)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()