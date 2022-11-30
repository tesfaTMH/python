#Q1: round to two decimal points 
num1 = float(input("Enter a decimal number: "))
num2 = round(num1, 2) 

print(f"{num1} is rounded to 2 decimal places is {num2}")
#Q2 absolute value of a number 
num3 = float(input("Enter a number: "))
num4 = abs(num3)
print(f"The absolute of {num3} is {num4}")

# Q3:check if the difference of two numbers is an integer
num5 = float(input("Enter a numebr: "))
num6 = float(input("Enter anothe number: "))
num56 = num5 - num6

print(f"The difference between {num5} and {num6} is {num56} is an integer? {num56.is_integer()}")