# program that tracks the growing amount of an investment 

def invest(amount, rate, years):
    """amount: invested amount
    rate: percentage increase in %
    years: numbers of years invested"""
    for num in range(1, years+1):
        amount = amount + amount * rate/100
        print(f"year {num}: {amount:0.2f}")

print("To track the growing amount of your per each year provide")
print("""amount: initial invested amount
    rate: percentage increase in %
    years: numbers of years invested""")
amount = float(input("Enter inital amount invested: "))
rate = float(input("Enter interest rate in %: "))
years = int(input("Enter number of years invested: "))
invest(amount, rate, years)

