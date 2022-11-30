#!/usr/bin/python3

# Q1: create tuple literal containing "first", "second", "third"

cardinal_numbers = ("first", "second", "third")

# Q2: print the second element of the tuple
print(cardinal_numbers[1])

# Q3 unpack the created to three new strings 
pos1, pos2, pos3 = ("first", "second", "third")

print(pos1)
print(pos2)
print(pos3)

# Q4: create tuple 
my_name = tuple("Michael")

# Q5: check the character c if it in the created tuple

print("c" in my_name)

# Q6: create a new tuple using slicing 

my_name_part = my_name[0:3]
print(my_name_part[:])
