import string
from LetterStatus import LetterStatus
from rich import print as rprint

class PrintFormatter():
    def __init__(self):
        self.colors = self.__InitColors()
        self.myString = ""

    def __InitColors(self):
        colors = { LetterStatus.MATCH:"[bold green]",
                        LetterStatus.EXIST_WRONG_LOCATION:"[italic yellow]",
                        LetterStatus.NOT_EXIST: "[red]",
                        LetterStatus.NOT_PICKED_YET:"[grey0]"}
        return colors;


    def Reset(self):
        self.myString = ""

    ########## construct a word to print in colors, add letter -> call Print() when finished ##############
    def Append(self, letter, letterStatus):
        addition = self.colors[letterStatus] + letter
        self.myString += addition

    def Print(self):
        rprint (self.myString)

    ########## Print all letters coloured alphabetical order ##############
    def PrintLettersStatus(self, allLetters):
        lettersPrint=""
        for letter in allLetters:
            letterStatus = allLetters[letter]
            addition = self.colors[letterStatus] + letter
            lettersPrint += addition
        rprint(lettersPrint)

    ########## Print all letters coloured ordered by letter status ##############
    def PrintAllLettersByType(self, lettersDict):
        self.__FormatPrintLettersStatus(lettersDict, LetterStatus.MATCH)
        self.__FormatPrintLettersStatus(lettersDict, LetterStatus.EXIST_WRONG_LOCATION)
        self.__FormatPrintLettersStatus(lettersDict, LetterStatus.NOT_EXIST)
        self.__FormatPrintLettersStatus(lettersDict, LetterStatus.NOT_PICKED_YET)

    def __FormatPrintLettersStatus(self, lettersDict, status):
        color = self.colors[status]
        rprint (color + str(status),":")
        selecteds = {k: v for k, v in lettersDict.items() if v == status}
        rprint(color + str(list(selecteds.keys())))

    ########## Print naive messege ##############
    def PrintMessege(self, messege):
        rprint("[blue3]" + messege)








def TestPrintFormatter():
    TestPrintWord()
    #TestPrintLettersStatus()
    #TestPrintAllLettersByType()

def TestPrintAllLettersByType():
    allLetters = dict.fromkeys(string.ascii_lowercase, LetterStatus.NOT_PICKED_YET)
    allLetters["a"] = allLetters["c"] = allLetters["t"] = LetterStatus.MATCH
    allLetters["b"] = allLetters["r"] = allLetters["s"] = LetterStatus.EXIST_WRONG_LOCATION
    allLetters["f"] = allLetters["g"] = allLetters["i"] = LetterStatus.NOT_EXIST
    formatter = PrintFormatter()
    formatter.PrintAllLettersByType(allLetters)


def TestPrintLettersStatus():
    allLetters = dict.fromkeys(string.ascii_lowercase, LetterStatus.NOT_PICKED_YET)
    allLetters["a"] = allLetters["c"] = allLetters["t"] = LetterStatus.MATCH
    allLetters["b"] = allLetters["r"] = allLetters["s"] = LetterStatus.EXIST_WRONG_LOCATION
    allLetters["f"] = allLetters["g"] = allLetters["i"] = LetterStatus.NOT_EXIST
    formatter = PrintFormatter()
    formatter.PrintLettersStatus(allLetters)


def TestPrintWord():
    formatter = PrintFormatter()
    formatter.Append("a", LetterStatus.MATCH)
    formatter.Append("b", LetterStatus.EXIST_WRONG_LOCATION)
    formatter.Append("c", LetterStatus.NOT_EXIST)
    formatter.Append("b", LetterStatus.NOT_PICKED_YET)
    formatter.Append("e", LetterStatus.MATCH)
    formatter.Print()


    
#TestPrintFormatter()

