#PyQt5 Layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        image = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Images\\normal farfetch'd.jpeg"
        self.setWindowIcon(QIcon(image))
        self.setWindowTitle("Graphical User Interface")
        self.setGeometry(200, 150, 1000, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("You")
        label2 = QLabel("Are")
        label3 = QLabel("A")
        label4 = QLabel("Dumb")
        label5 = QLabel("Asshole")
        label1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label4.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label5.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label1.setFont(QFont("Sans", 20))
        label2.setFont(QFont("Sans", 20))
        label3.setFont(QFont("Sans", 20))
        label4.setFont(QFont("Sans", 20))
        label5.setFont(QFont("Sans", 20))
        label1.setStyleSheet("background-color: green")
        label2.setStyleSheet("background-color: aqua")
        label3.setStyleSheet("background-color: red")
        label4.setStyleSheet("background-color: yellow")
        label5.setStyleSheet("background-color: pink")
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        central_widget.setLayout(vbox)



def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()