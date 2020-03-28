from hangingMan import stages

secret = 'hangman'
wordOut = ["_"] * len(secret)
wordCheck = []
wrongGuessNum = 0
wrongGuessList = []

for i in range(0, len(secret)):
    wordCheck.append(str(secret[i:i+1]))


def nextRound():
    print(stages[wrongGuessNum])
    print('\n')
    print("Lives left: " + str((5 - wrongGuessNum)))
    print(*wordOut)


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


while wrongGuessNum < 5:
    print('\n', '\n')
    nextGuess = input("Your guess: ")[:1]
    check = secret.find(nextGuess)
    # correct guess
    if check != -1:
        updateOut(nextGuess)
        if ''.join(wordOut) == secret:
            winner()
            break
        else:
            nextRound()
    # incorrect guess
    else:
        wrongGuessNum += 1
        wrongGuessList.append(nextGuess)
        nextRound()

print('\n', '\n')
loser()
