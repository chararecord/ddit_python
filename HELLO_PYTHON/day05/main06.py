import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("main06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.show()
        
    def click(self):
        dan = int(self.le.text())
        rst = ""
        
        for i in range(1,10) :
            rst += "{}*{}={}\n".format(dan,i,dan*i) 
                    
        print(rst)
        self.te.setText(rst)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()