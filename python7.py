# print(1/0)

# try:
#     print(1/0)
# except:
#     print("This is impossible")

# print("Hello")
# import module_does_not_exist


# try:
#     import module_does_not_exist
# except ImportError:
#     print("Import not found")
# finally:
#     import random

# print("Hello")

# try:
#     def func():
#         print(ans)

#     func()
# except NameError:
#     print("Variable has not be declared")


# print("Hello")

# demo = open("demo.txt", "w", encoding='utf-8')
# demo.writelines("""
# My name is Idris, I love writing codes.
# """)
# demo.writelines("""
# My name is Idris, I love writing codes.
# """)
# demo.writelines("""
# My name is Idris, I love writing codes.
# """)

# demo = open("demo.txt", "w", encoding='utf-8')
# demo.writelines("""My name is Idris, I love writing codes.""")
# demo.writelines(['Python is good', ' over and out'])

# demo = open("demo.txt", "r", encoding='utf-8')

# print(demo.readline())

# demo = open("state_zip.json", "r")



# demo.close()

# print(demo.readlines())

# with open("state_zip.json", "r") as demo:
#     print(demo.read())

class Student:
    # name = "Idris"
    # age = 50
    # email = "example@example.com"

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def studentInfo(self):
        print(f"{self.name} {self.age} {self.email}")

# student1 = Student("Idris", 50, "example@example.com")
# print(student1.name)
# print(student1.age)
# print(student1.email)
# student1.studentInfo()
# student2 = Student("Ola", 23, "example1@example.com")
# print(student2.name)
# print(student2.age)
# print(student2.email)
# student2.studentInfo()


class Professor(Student):
    def __init__(self, name, age, email, professor):
        super().__init__(name, age, email)
        self.professor = professor

    def professorInfo(self):
        print(f"The professor that teaches {self.name} is {self.professor}")


student1 = Professor("Idris", 50, "example@example.com", "Mark Oliver")
student1.professorInfo()