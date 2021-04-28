import random


def startGuessingGame():
    """Printing begin of the game"""
    print("")
    print("".center(50, '-'))
    print(" Guessing game between 1 and 10 ".center(50, '-'))
    print("".center(50, '-'))
    print("")


# Dice function requiring: min and max
def randomNumber():
    """Returns random number between 1 and 10"""
    value = random.randint(1, 10)
    return value


def numberGuess():
    """User input"""
    value = int(input("What number is it (max 10): "))
    if type(value) == int:
        return value


def correctGuess(value):
    """Printing ending of the game"""
    print("")
    print("".center(50, '-'))
    print(" Wohooo you guessed right ".center(50, '-'))
    print(f" The number was {value} ".center(50, '-'))
    print("".center(50, '-'))
    print("")


# Initializing variables
guessing = True
# Setting random number
randomNumber = randomNumber()
# Printing initial game start
startGuessingGame()


while guessing:
    # while guessing doing a guess
    guess = numberGuess()
    # Check if guess is correct or not
    if randomNumber != guess:
        print("Guess is wrong. Try again", end="\n\n")
        continue
    else:
        # Breaks the infinite loop
        correctGuess(randomNumber)
        guessing = False
