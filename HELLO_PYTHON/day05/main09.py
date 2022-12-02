import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("main09.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb0.clicked.connect(self.click)
        self.pb1.clicked.connect(self.click)
        self.pb2.clicked.connect(self.click)
        self.pb3.clicked.connect(self.click)
        self.pb4.clicked.connect(self.click)
        self.pb5.clicked.connect(self.click)
        self.pb6.clicked.connect(self.click)
        self.pb7.clicked.connect(self.click)
        self.pb8.clicked.connect(self.click)
        self.pb9.clicked.connect(self.click)
        self.pbCall.clicked.connect(self.myCall)

    def myCall(self):
        str_tel = self.le.text()
        QMessageBox.question(None, 'calling', str_tel, QMessageBox.Yes, QMessageBox.NoButton)
    
    def click(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old+str_new)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()