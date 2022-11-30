import random
from random import randint

def coin_flip():
    """Randomly returns heads or tails"""
    if randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

head_sum = 0
tail_sum = 0

number_of_trials = 100_000

for num in range(0, number_of_trials):
    result = coin_flip()
    if result == "heads":
        head_sum = head_sum + 1
    else: 
        tail_sum = tail_sum + 1

chance_of_head_win = (head_sum/number_of_trials) 
chance_of_tail_win = (tail_sum/number_of_trials) 

print(f"The chance of head wins from {number_of_trials:,} is: {chance_of_head_win:0.2%}")
print(f"The chance of tail wins from {number_of_trials:,} is: {chance_of_tail_win:0.2%}")
