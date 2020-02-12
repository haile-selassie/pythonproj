import time
import random

place = ["  ","  ","  ","  ","  ","  ","  ","  ","  "]
content = ["X","O"]
coin = [0, 0]
pieces = {"user":" ","bot":" "}          #pieces[0] is user, pieces[1] is bot

def template():
    print("1 | 2 | 3")
    print("-"*10)
    print("4 | 5 | 6")
    print("-"*10)
    print("7 | 8 | 9\n") 
    
def board():
    print(place[0]+" | "+place[1]+" | "+place[2])
    print("-"*10)
    print(place[3]+" | "+place[4]+" | "+place[5])
    print("-"*10)
    print(place[6]+" | "+place[7]+" | "+place[8]+"\n")

def validatePlace(q):
    while True:
        try:
            x = int(input(q))
            while True:
                if x in range(1,10):
                    return x
                else:
                    break
        except:
            print("Please input a valid number.")

def validateXO(q):
    global content
    while True:
        x = input(q)
        if x.upper() in content:
            return x
        else:
            print("Invalid input.\n")

def userMove():
    while True:
        placechoice = (validatePlace("Where would you like to mark?\n~$ ")-1)
        if place[placechoice] == "  ":
            place[placechoice] = pieces["user"]
            break
        else:
            print("Place already taken.\n")
    moveBuffer("user")

def botMove():
    print("AI is deciding", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".\n")
    while True:
        placechoice = random.randint(0,8)
        if place[placechoice] == "  ":
            place[placechoice] = pieces["bot"]
            break
    moveBuffer("bot")

def moveBuffer(last):
    board()
    checkWin(last)
    if last == "user":
        botMove()
    elif last == "bot":
        userMove()
    	
def checkWin(player):
    global place
    global pieces
    comb = [place[0]+place[1]+place[2], place[3]+place[4]+place[5], place[6]+place[7]+place[8], place[0]+place[3]+place[6], place[1]+place[4]+place[7], place[2]+place[5]+place[8], place[0]+place[4]+place[8], place[2]+place[4]+place[6]]
    for x in comb:
        if x == str(pieces[player]*3):
            if player == "user":
                print("You have won!")
                resolve()
            elif player == "bot":
                print("The AI has won.")
                resolve()                 

def resolve():
    bin = ["yes", "no", "y", "n"]
    while True:
        ask = input("Would you like to play again? [Y/n]\n~$ ")
        ask = ask.lower()
        if ask == "yes" or ask == "y":
            initialize()
        elif ask == "no" or ask == "n":
            print("Thanks for playing!\n")
            time.sleep(1)
            exit()
        else:
            print("Invalid input.\n")

def initialize():
    global pieces
    global coin
    global place
    place = ["  ","  ","  ","  ","  ","  ","  ","  ","  "]
    choice = validateXO("\nWould you like to be X's or O's?\n~$ ")
    choice = choice.upper()
    if choice == "X":
        pieces["user"] = "X"
        pieces["bot"] = "O"
        print("Piece chosen: X\nAI piece: O\n")
    elif choice == "O":
        pieces["user"] = "O"
        pieces["bot"] = "X"
        print("Piece chosen: O\nAI piece: X\n")
    print("Flipping coin", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    x = random.randint(0,1)
    if x == 0:
        coin = [0, 1]
        print("You will go first.\n")
        template()
        userMove()
    elif x == 1:
        coin = [1, 0]
        print("The AI will go first.\n")
        template()
        botMove()
    
while True:
    initialize()
    
    


    
                
    