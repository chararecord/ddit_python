import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("main08.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.le_l.returnPressed.connect(self.click)
        self.show()

    def click(self):
        first = int(self.le_f.text())
        last = int(self.le_l.text())
        txt = ""
        
        for i in range(first, last+1) :
            for j in range(i) :
                txt += "*"
            txt += "\n"
        print(txt)
                
        self.pte.setPlainText(txt)        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()