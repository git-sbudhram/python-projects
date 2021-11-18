# When the number is divisible by 3 then instead of printing the number it prints "Fizz".` 

# When the number is divisible by 5, then instead of printing the number it prints "Buzz".` 

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it prints "FizzBuzz"`

total = 0
for numbers in range(1, 101):
  if numbers % 3 == 0 and numbers % 5 == 0:
    print("fizzbuzz")
  elif numbers % 5 == 0:
    print("buzz")
  elif numbers % 3 == 0: 
    print("fizz")
  else:
    print(numbers)
