import random

names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")

counter = len(names)
roll = random.randint(0, counter -1)
print(f"{names[roll]} is going to buy the meal today!")
