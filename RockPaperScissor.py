import random,time
from ascii import *

# ROCK PAPER AND SCISSOR

def start():
    comp = ["Rock","Paper","Scissor"]
    userScore = 0
    compScore = 0
    round = 1


    def compFunc():
        random.shuffle(comp)

    while True:
        newLine(1)
        #User Choice
        user = input("""Choose your option: 
    R/r - Rock
    P/p - Paper
    S/s - Scissor

>>> """)
        #Computer Random Choice
        compFunc()
# ROCK VS ROCK = TIE!
        if user == "R" and comp[0] == "Rock" or user == "r" and comp[0] == "Rock":
            stadium(asci1[0],asci1[0],result[2])
        
# ROCK VS PAPER = PAPER!
        elif user == "R" and comp[0] == "Paper" or user == "r" and comp[0] == "Paper":
            compScore += 1
            stadium(asci1[0],asci1[1],result[1])
# ROCK VS SCISSOR = ROCK!
        elif user == "R" and comp[0] == "Scissor" or user == "r" and comp[0] == "Scissor":
            stadium(asci1[0],asci1[2],result[0]) 
            userScore += 1
# PAPER VS ROCK = PAPER!
        elif user == "P" and comp[0] == "Rock" or user == "p" and comp[0] == "Rock":
            stadium(asci1[1],asci1[0],result[0])
            userScore += 1
# PAPER VS PAPER = TIE!
        elif user == "P" and comp[0] == "Paper" or user == "p" and comp[0] == "Paper":
            stadium(asci1[1],asci1[1],result[2])
# PAPER VS SCISSOR = SCISSOR!
        elif user == "P" and comp[0] == "Scissor" or user == "p" and comp[0] == "Scissor":
            stadium(asci1[1],asci1[2],result[1]) 
            compScore += 1
# SCISSOR VS ROCK = ROCK!
        elif user == "S" and comp[0] == "Rock" or user == "s" and comp[0] == "Rock":
            stadium(asci1[2],asci1[0],result[1]) 
            compScore += 1
# SCISSOR VS PAPER = SCISSOR!
        elif user == "S" and comp[0] == "Paper" or user == "s" and comp[0] == "Paper":
            stadium(asci1[2],asci1[1],result[0]) 
            userScore += 1
# SCISSOR VS SCISSOR = TIE!
        elif user == "S" and comp[0] == "Scissor" or user == "s" and comp[0] == "Scissor":
            stadium(asci1[2],asci1[2],result[2]) 
        else:
            print(asci1[3])
            break

        #STATUS
        print("Round:",round)
        round += 1
        print("userScore:",userScore,"computerScore:",compScore)

        #Winner
        if userScore == 3:
                print("You're The Winner!")
                break
        elif compScore == 3:
                print("Computer Win!")
                break
