#Number guessing game!!
import random
number = random.randrange(10, 30)
user_input = input("Please, input your guess")
attempts = 0
while attempts <= 5:
    attempts += 1
    if number > 30:
      print("Number is too high")
    elif number < 30:
        print("Number is too low")
    else:
        print("Accurate Guess")

    