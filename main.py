from PyQt5 import QtGui
from design import Ui_Form
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
import sys
from PyQt5.QtCore import Qt


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.turn = 'X'
                       
def app():
    app = QApplication(sys.argv)
    win = Game()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()