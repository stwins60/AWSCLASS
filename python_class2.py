
# STRING

name = "John"
age = 23 # => "23"

# print(name + " " +age) => can only concatenate a string

# CASTING
# Casting is a method of convert one data type to another
# To convert a string to integer, you use int()
# To convert a string to float, you use float()
# To convert an integer or float to a string, you str()

# print(name + " " +str(age))

#FORMAT

#Using the format function
# print("The name is {}, and he is {} year old".format(name, age))

# using an f string
# print(f"The name is {name} and he is {age} year old")


# INPUT Function
# to use an input, you use the input()
# The default return value for the input is always a string

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"The name is {name} and he is {age} year old")

color = "Green"

# To print the value of a data type position, you use the index of that position and the square bracket

# print(color[2])

# print(color[4])

# Slicing

# Slicing is when you want to get a value from one index to another index. The slicing uses the colon ":"

# print(color[0:4])

# print(color[::])

# print(color[:-2])

# print(color[::-1])

word = "python is a beautiful language to learn."

print(word.find("p"))

# LIST, TUPLE, SET, DICTIONARY, CONDITIONAL STATEMENTS

# Given a list of numbers, return True if the first and last element of the list is greater than or equal to 200
# [110, 99, 65, 75, 20, 199, 250]

# [209, 100, 75, 15, 65, 50, 200]