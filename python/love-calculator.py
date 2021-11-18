print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
names = name1 + name2
counter1 = 0
counter2 = 0

# TRUE check
if names.count("t") > 0:
  counter1 += names.count("t") 
if names.count("r") > 0:
  counter1 += names.count("r") 
if names.count("u") > 0:
  counter1 += names.count("u") 
if names.count("e") > 0:
  counter1 += names.count("e") 

# LOVE check
if names.count("l") > 0:
  counter2 += names.count("l")
if names.count("o") > 0:
  counter2 += names.count("o")
if names.count("v") > 0:
  counter2 += names.count("u")
if names.count("e") > 0:
  counter2 += names.count("e")

total = str(counter1) + str(counter2)
total = int(total)

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")
