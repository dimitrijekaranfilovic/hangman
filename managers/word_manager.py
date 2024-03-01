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
from random import choice

class WordManager:
    def __init__(self):
        self.__word_list: list[str] = []
        lines = []
        with open("./database/words.txt") as file:
            lines = file.readlines()
        self.__word_list = [line.strip().lower() for line in lines]
        self.__current_word: str | None = None
        self.__progress: list[str] = []
        self.__gueses: list[str] = []

    def get_word(self) -> str:
        return self.__current_word

    def start(self) -> None:
        self.__current_word = choice(self.__word_list)
        self.__progress = ["_"] * len(self.__current_word)
        self.__gueses = []

    def is_guess_correct(self, guess: str) -> bool:
        return guess in self.__current_word if self.__current_word is not None else False

    def add_guess(self, guess: str) -> None:
        self.__gueses.append(guess)

    def update_progress(self, guess: str) -> None:
        for index, char in enumerate(self.__current_word):
            if char == guess:
                self.__progress[index] = char

    def get_display_progress(self) -> str:
        return '  '.join(self.__progress)
    
    def get_display_guesses(self) -> str:
        return '  '.join(self.__gueses)

    def is_word_guessed(self) -> bool:
        return ''.join(self.__progress) == self.__current_word
    
    def is_already_guessed(self, guess: str) -> bool:
        return guess in self.__gueses