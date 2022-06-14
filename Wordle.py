import os
import random
import colorama



#Reset the Game
def New_Game():
    print("Welcome to Marios' Worlde game!!!")
    os.system("cls")
    
def import_DB():
    words=[]
    db=open("DB.txt","r")
    for word in db:
        words.append(db.read())
    print(words)
    return words


def Main():
    tries=6
    words=import_DB()
    word=words[random.randint(0,len(words))]
    print(word)
    New_Game()
    guess=input("Your guess:")
    while True:
        while len(guess)!=5: 
            print("Input word must have 5 letters.")
            guess=input("Your guess:")
        for letter in guess:
            if letter not in word : print(colorama.Fore.RED + letter)
            else: print(colorama.Fore.GREEN + letter)
        if guess==word:
            print("YOU WON :D")
            break
        else:
            tries-=1
            if tries==0:
                print("You Lost :( , The correct word was %s",word)
                break

import_DB()
Main()
