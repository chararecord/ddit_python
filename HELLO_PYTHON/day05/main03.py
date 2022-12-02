import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("main03.ui")[0]

lotto = list(range(1,46))
for i in range(1000) :
    rnd = int(random()*45)
    a = lotto[0]
    b = lotto[rnd]
    lotto[0] = b
    lotto[rnd] = a

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.show()
        
    def click(self):
        self.le1.setText(str(lotto[0]))
        self.le2.setText(str(lotto[1]))
        self.le3.setText(str(lotto[2]))
        self.le4.setText(str(lotto[3]))
        self.le5.setText(str(lotto[4]))
        self.le6.setText(str(lotto[5]))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass()
    app.exec_()