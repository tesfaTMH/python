# Q1, 2 creating a string containing an integer
var1 = "55"
var2 = int(var1) * 2
print(f"The double of {var1} is {var2}")

var3 = float(var1) * 2
print(f"The double of {var1} is {var3}")

#Q3 displaying string and integer together
integer1 = 43
string1 = "is an integer"

print(str(integer1) + " " + string1)

#Q4: double users inputs 
num1 = input("Enter a number: ")
num2 = input("Enter the second number: ")

print(f"The product of {num1} and {num2} is {int(num1) * int(num2)}")