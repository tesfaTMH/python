# A function that converts C to F
def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return round(F, 2)

# F to C
def convert_far_to_cel(F):
    C = (F-32) * 5/9
    return round(C, 2)

cel = float(input("Enter a temp. in C: "))
far = convert_cel_to_far(cel)
print(f"The temp. in F equivalent to {cel} C is {far} F")

far = float(input("Enter a temp. in F: "))
cel = convert_far_to_cel(far)
print(f"The temp. in C equivalent to {far} F is {cel} C")
