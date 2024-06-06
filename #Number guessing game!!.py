#Number guessing game!!
import random
num = random.randrange(10, 30)
attempts = 5
while attempts > 0:
    number = int(input("Please, input your guess"))
    if number > 30:
      print("Number is too high")
    elif number < 30:
        print("Number is too low")
    else:
        print("Accurate Guess")
        break
    attempts -= 1

    if attempts > 0:
        print(f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left")
    else:
        print(f"You have used up your attempts, the number is {num}")

    