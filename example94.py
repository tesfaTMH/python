#!/usr/bin/python3

universties = [
    ["CIT", 2175, 37704],
    ["Har", 19627, 39849],
    ["MIT", 10566, 40732],
    ["Prin", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Std", 19535, 40569],
    ["Yale", 11701, 40500]
]

def enrollment_stats(list_of_uni):
    """Input: Nested list of universities with name, no. of students, tutition
    Output: list with no. of students and tutition"""
    students = []
    tutition = []

    for num in list_of_uni:
        students.append(num[1])
        tutition.append(num[2])

    return students, tutition

def mean_avg(target_list):
    """Input: list
    Output: mean"""

    return sum(target_list)/len(target_list)

def median_avg(target_list):
    target_list.sort()

    if (len(target_list)%2 == 1):
        middle_index = int(len(target_list)/2)
        return target_list[middle_index]
    else:
        middle_left = (len(target_list)-1)/2
        middle_right = (len(target_list)+1)/2
        return (target_list[middle_left] + target_list[middle_right])/2


total_result = enrollment_stats(universties)

print("%%%%" * 10)

print(f"Total number of Students: {sum(total_result[0]):,}")
print(f"Total tutition fee: {sum(total_result[1]):,}")

print(f"Student mean: {mean_avg(total_result[0]):,.0f}")
print(f"Tutition fee mean: {mean_avg(total_result[1]):,.2f}")

print(f"Student meadian: {median_avg(total_result[0]):,.0f}")
print(f"Tutition fee meadian: {median_avg(total_result[0]):,.2f}")


