import random
num = random.randint(1, 100)
user_input = input("Enter a number between 1 and 100: ")
if user_input == num:
    print("You guessed it right!")

elif user_input < num:
        print("Too low!")
else:
        print("Too high!")

