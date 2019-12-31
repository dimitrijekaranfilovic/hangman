class WordManager:
    def __init__(self):
        self.word_list = []
        f = open("./database/words.txt")
        lines = f.readlines()
        for line in lines:
            self.word_list.append(line.strip().lower())

