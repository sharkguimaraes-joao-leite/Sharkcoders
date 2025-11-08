#G.U.I = Graphical User Interface
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grand Fest")
        image = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Images\\normal farfetch'd.jpeg"
        self.setWindowIcon(QIcon(image))
        self.setGeometry(200, 150, 1000, 500)
        label = QLabel(self)
        label.setGeometry(0, 0, 1000, 500)
        pixmap = QPixmap("c:\\Users\\Aluno EDAH\\Desktop\\João\\Images\\Grand Fest.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()