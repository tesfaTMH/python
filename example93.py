#!/usr/bin/python3

#Q1: create a nested tuple

data = ((1, 2), (3, 4))

# Q2: use for-loop to add all elements
data_sum = 0

for i in range(len(data)):
    data_sum = data_sum + sum(data[i])
print(data_sum)

# Q3: create a list
numbers = [4, 3, 2, 1]

# Q4: sort the list
numbers.sort()
print(numbers)

# Q5: create a copy using slice notation

numbers_copy = numbers[:]

numbers_copy.sort()

print(numbers_copy)
