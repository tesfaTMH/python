#!/usr/bin/python3

# Q1: create an empty list
captains = {}

# Q2: Insert data to the dictionary
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# Q3: Check if "Enterprise" and "Discovery" are with in the in the list if not assign it to "unknown"
if "Enterprise" in captains:
    print(captains["Enterprise"])
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    print(captains["Discovery"])
else:
    captains["Discovery"] = "unknown"

# Q4: write a for loop to print the ship name and the captain name
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

# Q5: delete "Discovery"  from the list
del captains["Discovery"]
print(captains)

# Q6: create dictionary using dict()
captains2 = dict(
    [
        ("Enterprise", "Picar"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko")
    ]
)

print(captains2)