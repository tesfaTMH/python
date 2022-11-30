#Q1: ask for user input and quit when q is pressed 

while(True):
    var1 = input("Enter something: ")
    print(f"You input is: {var1}")
    if (var1.lower() == "q"):
        break

# Q2: print multiples of 3 for numbers b/n 1 and 50
for num in range(1, 50):
    if num % 3 == 0:
        print(f"{num} is multiples of 3")
    else:
        continue