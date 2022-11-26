

# name = "IDRIS"

# print(name)

# name = input("Enter your name: ")

# print(name)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum_of_num = num1 + num2

# print(sum_of_num)

# DATA TYPES -> LIST, TUPLE, SET, DICTIONARY

# LIST
# A list is an array ordered collection of data. In simple explanation, It can be defined as a group of items.
# It uses the square bracket and it is mutable.

color = ["Green", "Blue", "Blue", "Red", "Yellow"]

#To check the variable data type
# print(type(color))


# print(color)

# To get the an item in a list
# print(color[4])

# color.append("Green")

# print(color[4])

# color.clear()
# color.append("Green")
# print(color)

# new_color = color.copy()

# print(new_color)


# new_color.remove("Blue")

# print(new_color)

# color.reverse() or # print(color[::-1])

# color.reverse()
# print(color)

# color.sort()

# print(color)

# color.sort()
# print(color)

# color.pop()

# print(color)


# TUPLE
# A tuple is an array ordered collection of data. In simple explanation, It can be defined as a group of items.
# It uses the parenthesis and it is immutable(you can't change the original form).

# car = ('BMW', 'VOLVO', 'TOYOTA', "BMW")

# car.append('TESLA')

# print(car.index("BMW"))

# print(car.count("BMW"))

# print(car[1])

#SET
# Set is an unordered collection of data. It is mutable and does not contain duplicate.
# Set use curly bracket and it can contain all data types

subject = {"Math", "English", "Biology", "Computer", "Math", "PHE"}



subject.add("Python")

# print(subject)

# subject.clear()
# print(subject)

# new_subject = subject.copy()
# print(new_subject)


# subject.remove("Math")

# new_subject.add("Devops")
# print(new_subject)
# print(new_subject.intersection(subject))

# subject.pop()

# print(subject)


# DICTIONARY
# Dictionary is an unordered collection of data value. It uses key value pair. A key is separated by a color. It is uses curly bracket

student = {
    "name": "Idris",
    "age": 23,
    "course": "Python"
}

# print(student)

# print(student["name"])

# student["email"] = "example@example.com"

# print(student)

# student.clear()
# print(student)

# new_student = student.copy()
# print(student)

# student.pop("course")

# print(student)

# print(student.values())

# print(student.keys())


#CONDITIONAL STATEMENT

# it uses the if and else clause

# age = 28

# # if age < 18:
# #     print("Too young to drive")
# # else:
# #     print("can drive")

# if age <= 18 or age == 18:
#     print("You are a teen")

# elif age <=25:
#     print("You are an adult")

# else:
#     print("You are a senior")

# color = ["Green", "Blue", "Blue", "Green", "Red", "Yellow"]


# if color[0] == 'Green' or color[4] == 'Green':
#     print("The color in position 0 or 4 is Green")
# else:
#     print("Only one color is found in one position")

# # from AWSCLASS.python4 import additon
# import python4


# print(python4.additon(4,4))

# python4.hello()