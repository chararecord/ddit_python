import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("main05.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.show()
        
    def click(self):
        num1 = self.lea.text()
        num2 = self.leb.text()
        rst = int(num1)*int(num2)
        
        print(num1, num2, rst)
        
        self.lec.setText(str(rst))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()