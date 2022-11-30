# Q1: try exception ValueError
while(True):
    try: 
        num = input("Enter an integer: ")
        print(int(num))
        break
    except ValueError:
        print("Try again")

# Q2: print the character a given index of an input text
string1 = input("Insert a text:")

try:
    index = int(input("Which character you want to display: "))
    print(f"The {index}th character of {string1} is: {string1[index]}")
except ValueError:
    print(f"Insert an integer: ")
except IndexError:
    print(f"Insert an index lessthan {len(string1)}")