'''
Hangman terminal game.
Author: TwKnD
'''
import os
from numpy import random
from gallows import STAGES
from words import SECRET_LIST

secret = random.choice(SECRET_LIST)
secret_reveal = ["_"] * len(secret)
secret_check = []
lives = 5
incorrect_list = []
first_round = True

for i in range(0, len(secret)):
    secret_check.append(str(secret[i:i+1]))


def next_round():
    '''
    Prints gallows, lives, guesses, etc
    '''
    if lives == -1:
        os.system('clear')
        loser()
    else:
        # print('\n \n')
        os.system('clear')
        print("Lives left: " + str((lives)))
        print('\n')
        print(STAGES[5 - lives])
        print('\n \n')
        print(*secret_reveal)
        print('Guessed:', *incorrect_list)


def winner():
    '''
    Prints on win condition
    '''
    os.system('clear')
    print(STAGES[7])
    print("Congratulations !!")
    print('The word was:', secret)


def loser():
    '''
    Prints on lose condition
    '''
    # print('\n \n \n')
    os.system('clear')
    print(STAGES[6])
    print("Sorry, You lose :(")
    print("The Word was: " + secret)


def update_reveal(char):
    '''
    Reveals character in list if correct
    '''
    index = 0
    while index < len(secret):
        index = secret.find(char, index)
        if index == -1:
            break
        secret_reveal[index] = player_guess
        index += 1


def check_word(match):
    '''
    Checks multi character guesses
    '''
    global lives
    if match:
        lives = -1
        winner()
    else:
        lives -= 1
        next_round()


def check_char(char):
    '''
    checks single letter guesses
    '''
    global lives

    if char != -1:
        # correct guess
        update_reveal(player_guess)
        if ''.join(secret_reveal) == secret:
            lives = -1
            winner()
        else:
            next_round()

    else:
    # incorrect guess
        lives -= 1
        incorrect_list.append(player_guess)
        next_round()


# Main Game Loop
while lives > -1:
    if first_round:
        first_round = False
        next_round()
    player_guess = input("Your guess: ")
    guessed_word = player_guess == secret
    guessed_char = secret.find(player_guess)
    if len(player_guess) > 1:
        check_word(guessed_word)
    else:
        check_char(guessed_char)
