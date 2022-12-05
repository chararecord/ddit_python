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
        # self.com = "123" -- 멤버변수
        
        self.setComRandom()
        self.pb.clicked.connect(self.myclick)
        
    def setComRandom(self):
        arr9 = [1,2,3,4,5,6,7,8,9]
        
        for i in range(0,1000) :
            rnd = int(random()*9)
            a = arr9[0]
            b = arr9[rnd]
            arr9[0] = b
            arr9[rnd] = a
        
        self.com =  str(arr9[0])+""+str(arr9[1])+""+str(arr9[2])

    def myclick(self):
        mine = self.le.text()
        s = self.getStrike(mine, self.com)
        b = self.getBall(mine, self.com)
        
        str_old = self.te.toPlainText()
        str_new = mine+" "+str(s)+"S "+str(b)+"B\n"
        
        self.te.setText(str_old+str_new)
        self.le.setText("")
        
        if s==3 :
            QMessageBox.question(None, '야구게임', self.com+" 정답입니다~!", QMessageBox.Yes, QMessageBox.NoButton)
            
    def getStrike(self, mine, com):
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if c1 == m1 : ret += 1
        if c2 == m2 : ret += 1
        if c3 == m3 : ret += 1
        
        return ret
            
    def getBall(self, mine, com):
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if c1 == m2 or c1 == m3 : ret += 1
        if c2 == m1 or c2 == m3 : ret += 1
        if c3 == m1 or c3 == m2 : ret += 1
        
        return ret
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()