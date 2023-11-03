from random import randint

class Game:

    def __init__(self):
        self.words =["python", "programlama", "oyun", "eğlence", "öğrenme"]
        self.word = ""
        self.guessTrueLetter = False
        self.healt = 5
        self.wordlen = 0

    def StartGame(self):
        self.emptyWord = []
        self.PicktheWord()
        self.wordlen = len(self.word)
        for i in range(self.wordlen):
            self.emptyWord.append("_")
        self.emptyWord = "".join(self.emptyWord)
        while True:
            print(self.emptyWord)
            self.WordGuess()
            if self.guessTrueLetter:
                print("Good job...")
                self.guessTrueLetter = False
            else:
                self.healt -= 1
                print(f"Your healt is now : {self.healt}")
            if self.healt == 0:
                self.GameOver()
            if self.Win():
                print("Do you want to continue?")
                isGameEnd = input("If yes type 'yes' if no type 'no'").lower()
                if isGameEnd == "yes":
                    self.StartGame()
                else:
                    exit()
                
    def GameOver(self):
        print("You Lose")
        print(f"Your word was {self.word}")
        isGameEnd = input("If you want to try again please type: 'again' otherwise the game will be shutdown : ").lower()
        if isGameEnd == "again":
            self.StartGame()
        else:
            exit()
    def Win(self):
        if self.emptyWord == self.word:
            print("You Win")
            return True
        else:
            return False
    def PicktheWord(self):
        self.word = self.words[randint(0,(len(self.words)-1))]
        return self.word
    def WordGuess(self):
        print()
        guess = input("Guess a letter: ")
        self.emptyWord = list(self.emptyWord)
        for i in range(self.wordlen):
            if self.word[i] == guess:
                self.emptyWord[i] = guess
                self.guessTrueLetter = True
        self.emptyWord = "".join(self.emptyWord)