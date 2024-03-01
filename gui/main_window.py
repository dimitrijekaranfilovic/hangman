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

from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox, QApplication
from managers.word_manager import WordManager
from managers.state_manager import StateManager
from gui.home_screen import HomeScreen
from gui.game_screen import GameScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.word_manager = WordManager()
        self.state_manager = StateManager()

        self.stack_widget = QStackedWidget()
        self.home_screen = HomeScreen()
        self.game_screen = GameScreen(self.state_manager)
        self.stack_widget.addWidget(self.home_screen)
        self.stack_widget.addWidget(self.game_screen)

        self.setCentralWidget(self.stack_widget)
        self.stack_widget.setCurrentIndex(0)

        self.home_screen.start_game.clicked.connect(lambda: self.display(1))
        self.game_screen.submit_guess.clicked.connect(self.check_guess)
        self.setWindowTitle("Hangman")
        self.show()

    def display(self, index: int):
        self.stack_widget.setCurrentIndex(index)
        if index == 1:
            self.setFixedHeight(200)
            self.word_manager.start()
            self.game_screen.word_to_guess_edit.setText(self.word_manager.get_display_progress())
            self.game_screen.your_guess_edit.clear()
            self.game_screen.tried.setText(self.word_manager.get_display_guesses())
        else:
            self.setFixedHeight(350)

    def check_guess(self):
        guess = self.game_screen.your_guess_edit.text()
        self.game_screen.your_guess_edit.clear()
        if len(guess) > 1:
            QMessageBox.about(self, "Error", "You can enter only 1 character!")
        elif guess == "":
            QMessageBox.about(self, "Error", "You cannot submit an empty word!")
        else:
            if self.word_manager.is_already_guessed(guess):
                QMessageBox.about(self, "Message!", f"You have already guessed that.")
            else:
                if self.word_manager.is_guess_correct(guess):
                    QMessageBox.about(self, "Message", "Good guess!")
                    self.word_manager.update_progress(guess)
                    to_display = self.word_manager.get_display_progress()
                    self.game_screen.word_to_guess_edit.setText(to_display)
                    if self.word_manager.is_word_guessed():
                        QMessageBox.about(self, "Victory!", f"You have won! The word was '{self.word_manager.get_word()}'")
                        self.display(0)
                else:
                    QMessageBox.about(self, "Message", "Wrong guess!")
                    self.word_manager.add_guess(guess)
                    self.game_screen.tried.setText(self.word_manager.get_display_guesses())
                    self.state_manager.next_state()
                    self.game_screen.update_image()
                    if self.state_manager.is_final_state():
                        QMessageBox.about(self, "Defeat", f"You have lost!\nThe word was: '{self.word_manager.get_word()}'")
                        self.display(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
