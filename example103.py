#!/usr/bin/python3

# Q1: write a class that inherits from Dog class and has default sound 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

# Q2: create a rectangle class that must be instantiated with length and width

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# create a square class that inherits from rectangle class
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

sq = Square(5)
print(f"The area of a square with {sq.length} side length is {sq.area()}")

print(isinstance(sq, Rectangle))