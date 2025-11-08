#Interactable buttons in Python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        image = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Images\\normal farfetch'd.jpeg"
        self.setWindowIcon(QIcon(image))
        self.setWindowTitle("Graphical User Interface")
        self.setGeometry(200, 150, 1000, 500)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click, if you dare...")

def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()