from hangingMan import stages

secret = 'hangman'
wordOut = ["_"] * len(secret)
wordCheck = []
lives = 6
wrongGuessList = []

for i in range(0, len(secret)):
    wordCheck.append(str(secret[i:i+1]))


def nextRound():
    print('\n', '\n')
    print(stages[lives])
    print('\n', '\n')
    print("Lives left: " + str((5 - lives)))
    print(*wordOut)
    print('Guessed:', *wrongGuessList)


def winner():
    print(secret)
    print("Congratulations !!")


def loser():
    print("Sorry, You lose :(")
    print("The Word was: " + secret)


def updateOut(char):
    index = 0
    while index < len(secret):
        index = secret.find(char, index)
        if index == -1:
            break
        wordOut[index] = nextGuess
        index += 1


# check word guesses
def checkWord(match):
    global lives
    if match:
        winner()
        lives = 0
    else:
        lives -= 1
        nextRound()


def checkChar(char):
    global lives
    # correct guess
    if guessChar != -1:
        updateOut(nextGuess)
        if ''.join(wordOut) == secret:
            winner()
            lives = 0
        else:
            nextRound()
    # incorrect guess
    else:
        lives -= 1
        wrongGuessList.append(nextGuess)
        nextRound()

while lives > 0:
    nextGuess = input("Your guess: ")
    guessWord = nextGuess == secret
    guessChar = secret.find(nextGuess)
    if len(nextGuess) > 1:
        checkWord(guessWord)
    else:
        checkChar(guessChar)


print('\n', '\n')
loser()
