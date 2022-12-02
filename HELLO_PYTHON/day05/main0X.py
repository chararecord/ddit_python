import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("main0X.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.click)
        num = self.le.text()
        arr = [1,2,3,4,5,6,7,8,9]
        global com
        
        for i in range(0,100) :
            rnd = int(random()*9)
            a = arr[0]
            b = arr[rnd]
            arr[0] = b
            arr[rnd] = a
        
        com =  str(arr[0])+""+str(arr[1])+""+str(arr[2])

    def click(self):
        mine = self.le.text()
        s = self.strike(mine, com)
        b = self.ball(mine, com)
        ss = str(s)
        bb = str(b)
        
        str_new = mine+" "+ss+"S "+bb+"B"
        self.te.append(str_new)
        self.le.setText("")
        
        if int(s)==3 :
            result = "정답입니다~"
            QMessageBox.question(None, 'WOW', result, QMessageBox.Yes, QMessageBox.NoButton)
            
    def strike(self, mine, com):
        ret = 0
        mine = self.le.text()
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if c1 == m1 :
            ret += 1
        if c2 == m2 :
            ret += 1
        if c3 == m3 :
            ret += 1
        
        return ret
            
    def ball(self, mine, com):
        ret = 0
        mine = self.le.text()
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if (c1 == m2) or (c1 == m3) :
            ret += 1
        if (c2 == m1) or (c2 == m3) :
            ret += 1
        if (c3 == m1) or (c3 == m2) :
            ret += 1
        
        return ret
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()