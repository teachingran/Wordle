import string
from LetterStatus import LetterStatus
from PrintFormatter import PrintFormatter

class WordleGame():
    def __init__(self, wordle):
        self.wordle = wordle
        self.size=len(wordle)
        self.letters = dict.fromkeys(string.ascii_lowercase, LetterStatus.NOT_PICKED_YET)
        self.hits=[LetterStatus.NOT_PICKED_YET]*self.size


    def Play(self):
        self.gameOver = False
        turn=0
        while self.gameOver != True and turn < 6:
            turn+=1
            print("turn num ", str(turn))
            word = input("your word is:")
            self.PlayTurn(word)
#            self.PrintLettersStatus()
            self.Print(word)
            
        
        self.PrintGameOver(turn)


    
    def PlayTurn(self, word):
        if len(word) != self.size:
            print (str(self.size), " letter words only!")
            return
        gameOver = True
        for i in range(self.size):
            if word[i] == self.wordle[i]:
                self.letters[word[i]]=LetterStatus.MATCH
                self.hits[i]=LetterStatus.MATCH
            else:
                gameOver = False
                if self.wordle.find(word[i])!= -1:
                    self.letters[word[i]]=LetterStatus.EXIST_WRONG_LOCATION
                    self.hits[i]=LetterStatus.EXIST_WRONG_LOCATION
                else:
                    self.letters[word[i]]=LetterStatus.NOT_EXIST
                    self.hits[i]=LetterStatus.NOT_EXIST
        self.gameOver = gameOver

        
    def PrintLettersStatus(self, letter=None):
        pf = PrintFormatter()
        pf.PrinPrintLettersStatus()


    def Print(self, word, printAllLetters=True, printByType = False):
        pf = PrintFormatter()
        for letter in word:
            pf.Append (letter, self.letters[letter])
        pf.Print()
        if printAllLetters:
            pf.PrintLettersStatus(self.letters)
        if printByType:
            pf.PrintAllLettersByType(self.letters)

    def PrintGameOver(self, turns):
        pf = PrintFormatter()
        if (self.gameOver):
            pf.PrintMessege("Great, you won in {} turns".format(turns))
        else:
            pf.PrintMessege("Game is now OVER, Nevermind, you can try again")



def TestSingleWordleGame():
    game = WordleGame("abcdefg")
    #game.PrintLettersStatus()
    game.Play()

        
    

#TestSingleWordleGame()


        



