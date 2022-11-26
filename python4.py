# LOOPS

# for loop
# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string). 
# This is less like the *for* keyword in other programming languages, 
# and works more like an iterator method as found in other object-orientated programming languages. 
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# for i in range(1,4):
#     print(i)
#     # if i % 2 == 0:
#     #     print(f"even: {i}")
#     # else:
#     #     print(f"odd: {i}")

# WHILE LOOP
# A while loop statement in Python programming language repeatedly executes 
# a target statement as long as a given condition is true. We use the keyword *while*

# i = 1
# while i < 6:
#     print(i)
#     i = i + 1 # i+=1

# i = 10
# while i < 20:
#     print(i)
#     if i == 12:
#         break
    

# FUNCTION
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python a function is defined using the *def* keyword:
# We have two types of function: Built-in function and User-defined function
# A function can take any number of arguments and can return any number of arguments

# USER-DEFINED FUNCTION
# def hello():
#     print("Hello")

# ca
# hello()

# BUILT-IN FUNCTION
# sum(), abs(), list(), str(), int(), float(), random()
# e.g print(sum([1,2,3])), print(str(9)), print(random.choice([1, 2]))


# def hello(name):
#     for i in name:
#      print(f"Hello {i}")


# name = ["Mark", "Dan", "Yemi"]
# hello(name)

# def MaxMinVALUE(num):
#     maxVal, minVal = num[0], num[0]

#     for i in num:
#         if i > maxVal:
#             maxVal = i
        
#         if i < minVal:
#             minVal = i

#     print(maxVal, minVal)

# l1 = [1,2,3,4,5,6]
# MaxMinVALUE(l1)


# def MinVALUE(num):
#     minVal = num[0]

#     for i in num:
#         if i < minVal:
#             minVal = i

#     return minVal


# print(MinVALUE([1,2,3,4,5,6])) 


def randomNum(n):
    return [x for x in range(1,n+1)]