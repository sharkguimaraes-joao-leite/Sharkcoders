#G.U.I = Graphical User Interface
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphical User Interface")
        self.setGeometry(200, 150, 1000, 500)
        image = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Images\\normal farfetch'd.jpeg"
        self.setWindowIcon(QIcon(image))
        label = QLabel("Hello Loser!", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(370, 150, 300, 150)
        label.setStyleSheet("color: aqua;"
                            "font-weight: bold;"
                            "font-style: italic;")
        label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        
def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()