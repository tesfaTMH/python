# Q1: write a function for fair rolling of a dice 
from random import randint

def roll():
    result = randint(1, 6)
    if result == 1:
        return "P1"
    elif result == 2:
        return "P2"
    elif result == 3:
        return "P3"
    elif result == 4:
        return "P4"
    elif result == 5:
        return "P5"
    else:
        return "P6"

#Q2: simulate a fair die
num_of_trials = 100_000
sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0
sum_p6 = 0

for num in range(num_of_trials):
    roll1 = roll()
    if roll1 == "P1":
        sum_p1 = sum_p1 + 1
    elif roll1 == "P2":
        sum_p2 = sum_p2 + 1
    elif roll1 == "P3":
        sum_p3 = sum_p3 + 1
    elif roll1 == "P4":
        sum_p4 = sum_p4 + 1
    elif roll1 == "P5":
        sum_p5 = sum_p5 + 1
    else:
        sum_p6 = sum_p6 + 1

print(f"The chance of dice being facing 1 from {num_of_trials} trials is {sum_p1/num_of_trials:0.2%}")