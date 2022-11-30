#!/usr/bin/python3

cats = {}

# Initailly all the 100 cats does not have hats 
for i in range(1, 101):
    cats[i] = False

# loop around loop 100 times
for i in range(1, 101):
    # visit each cat on each loop 
    for cat_num, hat in cats.items():
        # determines whether cat is visited or not  
        if cat_num % i == 0:
            # check if cats has hat and if not put hat
            if cats[cat_num]:
                cats[cat_num] = False
            else:
                cats[cat_num] = True

# List the cats with hat
for cat_num, hat in cats.items():
    if cats[cat_num]:
        print(f"{cat_num} has hat")