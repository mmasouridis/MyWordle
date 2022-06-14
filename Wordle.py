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
    words=db.readlines()
    return words


answer='y'
words=import_DB()
#print(word)
while answer=='y':
    tries=6
    word=words[random.randint(0,len(words))].strip('\n')
    print("Tries remaining: ",tries)
    guess=input("Your guess:")
    while True:
        while len(guess)!=5: #or (guess not in words): 
          if len(guess)!=5: print("Input word must have 5 letters.")
          else:print("Your guess is not in the word list.")
          guess=input("Your guess:")
        for letter in guess:
          if letter not in word : print(colorama.Fore.RED + letter,end='')
          else: 
            if guess.index(letter)!=word.index(letter):
                print(colorama.Fore.YELLOW + letter,end='')
            else:
                print(colorama.Fore.GREEN + letter,end='')
        print(colorama.Style.RESET_ALL)
        if guess==word:
          print("YOU WON :D")
          break
        else:
          tries-=1
          print("Tries remaining: ",tries)
          if tries==0:
            print("You Lost :( , The correct word was ",word)
            break
        guess=input("Your guess:")
    answer=input("Do you want to play again[y/n]: ")
    while answer!='y' and answer!='n':answer=input("Do you want to play again[y/n]: ")
    
    


