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
from gui.home_screen import HomeScreen
from gui.game_screen import GameScreen
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.word_manager = WordManager()
        self.current_word = ""
        self.current_progress = []
        self.progress_to_show = ""
        self.current_state = 0
        self.you_tried = ""

        self.stack_widget = QStackedWidget()
        self.home_screen = HomeScreen()
        self.game_screen = GameScreen()
        self.stack_widget.addWidget(self.home_screen)
        self.stack_widget.addWidget(self.game_screen)

        self.setCentralWidget(self.stack_widget)
        self.stack_widget.setCurrentIndex(0)

        self.home_screen.start_game.clicked.connect(lambda: self.display(1))
        self.game_screen.submit_guess.clicked.connect(self.check_guess)
        self.setStyleSheet("font: 12pt Times New Roman")
        self.setWindowTitle("Hangman")
        self.show()

    def display(self, i):
        self.stack_widget.setCurrentIndex(i)
        if i == 1:
            self.setFixedHeight(200)
            self.start_game()
            self.progress_to_show = "_ " * len(self.current_word)
            self.game_screen.word_to_guess_edit.setText(self.progress_to_show)
            self.current_progress = []
            self.game_screen.your_guess_edit.clear()
            self.game_screen.state_picture.setPixmap(self.game_screen.state1)
            self.current_state = 0
            self.you_tried = ""
            self.game_screen.tried.setText(self.you_tried)
            for s in self.current_word:
                self.current_progress.append("_")
        else:
            self.setFixedHeight(350)

    def start_game(self):
        self.current_word = random.choice(self.word_manager.word_list)
        # print(self.current_word)

    def check_guess(self):
        guess = self.game_screen.your_guess_edit.text()
        self.game_screen.your_guess_edit.clear()
        if len(guess) > 1:
            QMessageBox.about(self, "Error", "You can enter only 1 character!")
        elif guess == "":
            QMessageBox.about(self, "Error", "You cannot submit an empty word!")
        else:
            if guess in self.current_word:
                QMessageBox.about(self, "Message", "Good guess!")
                to_display = ""
                for i in range(len(self.current_word)):
                    current_letter = self.current_word[i]
                    if current_letter == guess:
                        to_display += guess
                        to_display += " "
                        self.current_progress[i] = guess

                    else:
                        to_display += self.current_progress[i]
                        to_display += " "
                self.progress_to_show = to_display
                self.game_screen.word_to_guess_edit.setText(self.progress_to_show)
                if "_" not in self.current_progress:
                    QMessageBox.about(self, "Victory!", "You have won!")
                    self.display(0)


            else:
                QMessageBox.about(self, "Message", "Wrong guess!")
                self.current_state += 1
                self.you_tried += guess
                self.you_tried += " "
                self.game_screen.tried.setText(self.you_tried)
                self.game_screen.state_picture.setPixmap(self.game_screen.states[self.current_state])
                if self.current_state == 6:
                    QMessageBox.about(self, "Defeat", "You have lost!\nThe word was: '" + self.current_word + "'")
                    self.display(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
