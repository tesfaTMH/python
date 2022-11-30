# simulate unfair coin flip trials 
import random 

def unfair_trial(prob_of_head):
    if random.random() < prob_of_head:
        return "heads"
    else:
        return "tails"

# simulate for unfair numebr of coin flips 

max_num_of_trials = 100_000
prob_of_head = 0.6

head_sum = 0
tail_sum = 0
for num in range(max_num_of_trials):
    result = unfair_trial(prob_of_head=prob_of_head)
    if result == "heads":
        head_sum = head_sum + 1
    else:
        tail_sum = tail_sum + 1

head_ratio = head_sum/max_num_of_trials
tail_ratio = tail_sum/max_num_of_trials

print(f"The chance of wining head within inital {prob_of_head} head and {max_num_of_trials} trials is: {head_ratio:0.3%}")
print(f"The chance of wining tail within inital {prob_of_head} head and {max_num_of_trials} trials is: {tail_ratio:0.3%}")
