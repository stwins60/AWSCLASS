#The concept of Object Oriented Programming

# class Student:
#     age = 26
#     name = "Idris"


# student1 = Student()

# print(f"{student1.name} {student1.age}")

class Car:
    # milage = 500
    # make = "Toyota"
    # color = "black"
    # year = 2024

    def __init__(self,milage, make, color, year):
        self.milage = milage
        self.make = make
        self.color = color
        self.year = year

    def myCar(self):
        print(f"The name of my car is {self.make}. It is a {self.color} car")
        print(f"It was made in the year {self.year}")


# car1 = Car(500, "Toyota", "Black", 2024)

# car1.myCar()

# car2 = Car(1000, "Tesla", "Red", 2024)
# car2.myCar()


# milage = input("Enter the milage of your car: ")
# make = input("Enter the make of your car: ")
# color = input("Enter the color of your car: ")
# year = input("Enter the year of your car: ")


# car3 = Car(milage, make, color, year)
# car3.myCar()
# print(f"{car3.make} {car3.color} {car3.year} {car3.milage}")


class ToyotaCorolla(Car):
    def __init__(self, milage, make, color, year, model):
        super().__init__(milage, make, color, year)
        self.model = model

    def myCar(self):
        print(f"The name of my car is {self.make}. It is a {self.color} car")
        print(f"It was made in the year {self.year}")
        print(f"It is a {self.model} model")

car4 = ToyotaCorolla(500, "Toyota", "Black", 2024, "Corolla")
car4.myCar()


class carPrice(ToyotaCorolla):
    def __init__(self, milage, make, color, year, model, price):
        super().__init__(milage, make, color, year, model)
        self.price = price

    def myCar(self):
        print(f"The name of my car is {self.make}. It is a {self.color} car")
        print(f"It was made in the year {self.year}")
        print(f"It is a {self.model} model")
        print(f"It costs ${self.price}")

car5 = carPrice(500, "Toyota", "Black", 2024, "Corolla", 20000)
car5.myCar()

car_param = [50001, "Tesla", "Red", 2024, "Model X", 50000]

car6 = carPrice(*car_param)
car6.myCar()