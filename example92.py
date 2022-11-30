#!/usr/bin/python3

# Q1: create a list of food
food = ["pizza", "bread"]

#Q2: Append broccoli to food
food.append("broccoli")

#Q3: add more foods using extend

food.extend(["rice", "beans"])

#Q4: print part of the food
print(food[0:3])

#Q5: print last item of food
print(food[-1])

#Q6 create a list using split
breakfast = "eggs, fruit, orange, juice".split(", ")
print(breakfast)

# Q7: print the size of the list
print(len(breakfast))

# create another list with length of breakfast items

lengths = []

for num in range(len(breakfast)):
    lengths.append(len(breakfast[num]))

print(lengths)