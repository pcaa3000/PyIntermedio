import random
import os
import string

from files.hagman_art import HANGMANPICS

def get_word(pathfile="./files/data.txt"):
    words=[]
    with open(pathfile,"r",encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    word=random.choice(words)
    while '-' in words or ' ' in words:
        word=random.choice(words)
    return word

def game_hagman():
    TOTAL_LIFES=6
    word=get_word()
    letters_of_word=set(word)
    letters_of_user=set()
    list_abc=set(string.ascii_uppercase)
    list_abc.add("Ñ")
    lifes=TOTAL_LIFES
    msg=""
    title="""
    ===============================
        Wellcome to hagman Game
    ===============================
    """
    while lifes>0 and len(letters_of_word)>0:
        os.system("clear")
        print(title)
        msglifes=f"\n\tYou have {lifes} lifes."
        if len(letters_of_user)>0:
            print(f"{msglifes} The words used are: {' '.join(letters_of_user)}.\n\n")
        letters_on_screen=[letters if letters in letters_of_user  else '_' for letters in word ]
        print(f"Word: {' '.join(letters_on_screen)}\n")
        print(HANGMANPICS[TOTAL_LIFES-lifes])
        print(f"\n{msg}")
        letter=input("Choose a letter: ").upper()
        if letter in list_abc-letters_of_user:
            letters_of_user.add(letter)
            if letter in letters_of_word:
                letters_of_word.remove(letter)
                msg=""
            else:
                lifes-=1
                msg=f"Sorry, {letter} is not found in word."
        elif letter in letters_of_user:
            msg=f"Please, choose other letters."
        else:
            msg=f"Letter is not valid."
    if lifes==0:
        os.system("clear")
        print(title)
        print(f"\n Yout Lost, the word is {word}.")
        print(HANGMANPICS[TOTAL_LIFES-lifes])
    else:
        print(f"\n You Win!! ")


if __name__ == '__main__':
    game_hagman()