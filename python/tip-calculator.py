print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

sum = round(((bill / people) * (percentage / 100) + (bill / people)), 2)
total = "{:.2f}".format(sum)
print(f"Each person should pay: ${total}")
