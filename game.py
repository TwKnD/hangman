from numpy import random
from gallows import stages
from words import secret_list

secret = random.choice(secret_list)
secret_reveal = ["_"] * len(secret)
secret_check = []
lives = 5
incorrect_list = []
first_round = True

for i in range(0, len(secret)):
    secret_check.append(str(secret[i:i+1]))


def next_round():
    if lives == -1:
        print('\n \n \n')
        loser()
    else:
        print('\n \n')
        print("Lives left: " + str((lives)))
        print('\n')
        print(stages[5 - lives])
        print('\n \n')
        print(*secret_reveal)
        print('Guessed:', *incorrect_list)


def winner():
    print('\n \n \n')
    print(stages[7])
    print("Congratulations !!")
    print('The word was:', secret)


def loser():
    print('\n \n \n')
    print(stages[6])
    print("Sorry, You lose :(")
    print("The Word was: " + secret)


def update_reveal(char):
    index = 0
    while index < len(secret):
        index = secret.find(char, index)
        if index == -1:
            break
        secret_reveal[index] = player_guess
        index += 1


# check word guesses
def check_word(match):
    global lives
    if match:
        lives = -1
        winner()
    else:
        lives -= 1
        next_round()


def check_char(char):
    global lives
    # correct guess
    if guessed_char != -1:
        update_reveal(player_guess)
        if ''.join(secret_reveal) == secret:
            lives = -1
            winner()
        else:
            next_round()
    # incorrect guess
    else:
        lives -= 1
        incorrect_list.append(player_guess)
        next_round()


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
