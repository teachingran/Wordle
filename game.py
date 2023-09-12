import string
from LetterStatus import LetterStatus

class Wordle():
    def __init__(self):
        self.letters = dict.fromkeys(string.ascii_lowercase, LetterStatus.NOT_PICKED_YET)
    
    def print(self):
        print(self.letters)

    def print(self, letter):
        print(self.letters[letter])



game = Wordle()
game.print('r')


        



