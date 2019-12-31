"""
    Game of Hangman written in Python.
    Copyright (C) 2019  Dimitrije Karanfilović
    This file is part of pso.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""




from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from managers.word_manager import WordManager
import sys
import random


class GameScreen(QWidget):
    def __init__(self):
        super(GameScreen, self).__init__()
        self.state_picture = QLabel()

        self.state1 = QPixmap("./images/stage12.png")
        self.state2 = QPixmap("./images/stage22.png")
        self.state3 = QPixmap("./images/stage32.png")
        self.state4 = QPixmap("./images/stage42.png")
        self.state5 = QPixmap("./images/stage52.png")
        self.state6 = QPixmap("./images/stage62.png")
        self.state7 = QPixmap("./images/stage72.png")

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
