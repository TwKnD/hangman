from hangingMan import stages

secret = 'hangman'
wordOut = ["_"] * len(secret)
wordCheck = []
lives = 5
wrongGuessList = []
firstRound = True

for i in range(0, len(secret)):
    wordCheck.append(str(secret[i:i+1]))


def nextRound():
    if lives == -1:
        print('\n \n \n')
        loser()
    else:
        print('\n', '\n')
        print(stages[5 - lives])
        print('\n', '\n')
        print("Lives left: " + str((lives)))
        print(*wordOut)
        print('Guessed:', *wrongGuessList)


def winner():
    print('\n \n \n')
    print("Congratulations !!")
    print('The word was:', secret)


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
        lives = -1
        winner()
    else:
        lives -= 1
        nextRound()


def checkChar(char):
    global lives
    # correct guess
    if guessChar != -1:
        updateOut(nextGuess)
        if ''.join(wordOut) == secret:
            lives = -1
            winner()
        else:
            nextRound()
    # incorrect guess
    else:
        lives -= 1
        wrongGuessList.append(nextGuess)
        nextRound()


while lives > -1:
    if firstRound:
        firstRound = False
        nextRound()
    nextGuess = input("Your guess: ")
    guessWord = nextGuess == secret
    guessChar = secret.find(nextGuess)
    if len(nextGuess) > 1:
        checkWord(guessWord)
    else:
        checkChar(guessChar)
