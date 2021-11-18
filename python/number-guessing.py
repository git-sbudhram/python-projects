import random

print("Hello and welcome to guess the number \n")
randomNum = random.randint(0, 101)
print("\nThe range of numbers you're guessing is from", 1, "to", 100)
print(randomNum)

count = 0
while count != 7:
    count += 1
    
    userGuess = int(input("\nGuess the number: "))

    if randomNum == userGuess:
        print("Congratulations, you got it!")
    elif randomNum < userGuess:
        print("You guessed too high!")
    elif randomNum > userGuess:
        print("You guessed too low!")
    
    if count == 7:
        print("You guessed 7 times, game over")
