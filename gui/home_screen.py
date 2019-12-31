from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from managers.word_manager import WordManager
import sys
import random


class HomeScreen(QWidget):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.picture_label = QLabel()
        self.picture_label.setPixmap(QPixmap("./images/index.png"))

        self.start_game = QPushButton("Start game")
        self.setStyleSheet("font: 12pt Times New Roman")

        v = QVBoxLayout()
        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.picture_label)
        h.addStretch()

        v.addLayout(h)
        v.addWidget(self.start_game)
        self.setLayout(v)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeScreen()
    sys.exit(app.exec_())
