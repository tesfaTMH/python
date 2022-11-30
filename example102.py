#!/usr/bin/python3

# Q1: create a dog class with name, age and coat color attributes 
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, speak):
        return f"{self.name} says {self.speak}"

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}")

# Q2: create a car class with color and milage instances attributes 
class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, miles_added):
        self.mileage = self.mileage + miles_added

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

print(f"The {blue_car.color} has a mileage of {blue_car.mileage}")
print(f"The {red_car.color} has a mileage of {red_car.mileage}")

gray_car = Car("gray", 0)
gray_car.drive(100)

print(f"The {gray_car.color} has an added milage of {gray_car.mileage}")