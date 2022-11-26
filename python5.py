# def hello():
#     # print("Hello World")

#     return "Hello World"

# hello()
# print(hello())


# BUILT-IN FUNCTIONS

# NUM = list((1,2,3,4,5))

# print(NUM)

# NUM2 = tuple([1,2,3,4,5])
# print(NUM2)

# name = "Idris"

# print(list(name))
# print("".join(list(name)))

# print(len(name))

# name = input("Enter the name: ")
# print(name)

def printPython():
    return "Hello Python"

import random


# random.choice
# random.randint
# random.sample
# random.shuffle


rand_int = random.randint(1,101)

trial = 5

while True:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess == rand_int:
        print("You guessed right")
        break
    elif guess > rand_int:
        print("Guess is too high")
        trial = trial-1
        print(f"You have {trial} trials left")
    elif guess < rand_int:
        print("Guess is too low")
        trial = trial-1
        print(f"You have {trial} trials left")
    else:
        print("Invalid input")
    if trial == 0:
        print("You have exhausted your trial")
        break
