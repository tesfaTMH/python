#Q1: for loop for printing numbers 2 through 10
for num in range(2, 11):
    print(num)

#Q2: using while loop to print 2 through 10
num = 2
while(num <= 10):
    print(num)
    num = num + 1

#Q3: function that doubles a number

num = int(input("Enter a number: "))

def doubles(num):
    return 2*num

for i in range(1,4):
    num = doubles(num)
    print(num)