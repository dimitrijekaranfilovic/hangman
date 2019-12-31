from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from managers.word_manager import WordManager
import sys
import random


class GameScreen(QWidget):
    def __init__(self):
        super(GameScreen, self).__init__()
        self.state_picture = QLabel()

        self.state1 = QPixmap("./images/stage1.png")
        self.state2 = QPixmap("./images/stage2.png")
        self.state3 = QPixmap("./images/stage3.png")
        self.state4 = QPixmap("./images/stage4.png")
        self.state5 = QPixmap("./images/stage5.png")
        self.state6 = QPixmap("./images/stage6.png")
        self.state7 = QPixmap("./images/stage7.png")

        self.states = [self.state1, self.state2, self.state3, self.state4, self.state5, self.state6, self.state7]

        self.state_picture.setPixmap(self.state1)

        self.word_to_guess_edit = QLineEdit()
        self.word_to_guess_edit.setReadOnly(True)
        self.submit_guess = QPushButton("Submit guess")
        self.tried = QLabel()

        self.your_guess_edit = QLineEdit()

        v = QVBoxLayout()

        h1 = QHBoxLayout()
        h1.addStretch()
        h1.addWidget(self.state_picture)
        h1.addStretch()

        h2 = QHBoxLayout()
        h2.addWidget(QLabel("Current progress"))
        h2.addWidget(self.word_to_guess_edit)

        h3 = QHBoxLayout()
        h3.addWidget(QLabel("Your guess"))
        h3.addWidget(self.your_guess_edit)

        h4 = QHBoxLayout()
        h4.addWidget(QLabel("You tried"))
        h4.addWidget(self.tried)

        v.addLayout(h1)
        v.addLayout(h2)
        v.addLayout(h3)
        v.addLayout(h4)
        v.addWidget(self.submit_guess)
        self.setStyleSheet("font: 12pt Times New Roman")

        self.setLayout(v)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GameScreen()
    sys.exit(app.exec_())
