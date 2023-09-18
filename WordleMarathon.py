import random
from WordleGame import WordleGame

class WordleMarathon():
    def __init__(self, words):
        self.words = words

    def Play(self):
        play = 'y'
        while play != 'q' and len(self.words) > 0:
            word = random.choice(self.words)
            self.words.remove(word)
            game = WordleGame(word)
            game.Play()
            play = input("another game? press 'q' to quit")




def TestWordleMarathon():
    words = ['abcde', 'qwert', 'asdfg', 'cvbnm', 'lkjhg']
    wm = WordleMarathon(words)
    wm.Play()


#TestWordleMarathon()