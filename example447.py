# printing float using string concatenation
weight = 0.2
animal = "newt"

print(str(weight) + " is the weight of the " + animal)

# Q2: display using .format()w
print("{} is the weight of the {}".format(weight, animal))

# Q3: display using f-string
print(f"{weight} is the weight of the {animal}")