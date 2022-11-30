# Q1, 2: changing to lower and upper letters 
string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honey Badger"

print(string1.lower())
print(string1.upper())
print(string2.lower())
print(string2.upper())
print(string3.lower())
print(string3.upper())
print(string4.lower())
print(string4.upper())

#Q3: remove white space 
string1 = "     File document"
string2 = "Smart Dude     "
string3 = "     middle one    "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

#Q4, 5 startswith
string1 = "Beccomes"
string2 = "becomes"
string3 = "BEER"
string4 = "   beauty"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

print(string1.startswith("Be"))
print(string2.startswith("be"))
print(string3.startswith("BE"))
print(string4.startswith("  "))