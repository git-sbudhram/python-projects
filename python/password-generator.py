#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

saved_letters = []
saved_symbols = []
saved_numbers = []

for numbers1 in range(1, nr_numbers + 1):
    random_numbers = random.randint(1, 9)
    saved_numbers.append(numbers[random_numbers]) 

for numbers in range(1, nr_letters + 1):
  random_letters = random.randint(1, 51)
  saved_letters.append(letters[random_letters]) 

for numbers in range(1, nr_symbols + 1):
  random_symbols = random.randint(1, 8)
  saved_symbols.append(symbols[random_symbols]) 

password = saved_letters + saved_numbers + saved_symbols
random.shuffle(password)
combined_password = ''.join(password) 
print(combined_password)
