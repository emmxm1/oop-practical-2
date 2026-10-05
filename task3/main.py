income = float(input())

if income < 10000:
    tax = 0
elif income < 50000:
    tax = income * 0.10
elif income < 100000:
     tax = income * 0.20
else:
    tax = income * 0.30

print(tax)               