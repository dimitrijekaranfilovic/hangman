"""
    Game of Hangman written in Python.
    Copyright (C) 2019  Dimitrije Karanfilović
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

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap


class HomeScreen(QWidget):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.picture_label = QLabel()
        self.picture_label.setPixmap(QPixmap("./images/index2.png"))

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
    import sys
    app = QApplication(sys.argv)
    w = HomeScreen()
    sys.exit(app.exec_())
