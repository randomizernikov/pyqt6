import sys
from PyQt6.QtWidgets import QApplication,QPushButton,QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,400,400)
        self.btn()
        self.show()

    def btn(self):
        button=QPushButton('full black',self)
        button.clicked.connect(self.color_change)
        button.setStyleSheet(" background-color: black; color: red;  ")


    def color_change(self):
        self.setStyleSheet(" background-color: black ")
        print ('здравствуйте Сергей Валерьевич')


app=QApplication(sys.argv)
window=Window()
window.show()
app.exec()
