# Paying Debt off in a Year

# This program calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required
# by the credit card company each month.


# Declare initial variables
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
year = 12
monthlyInterestRate = annualInterestRate / year
monthlyPayment = balance * monthlyPaymentRate


for month in range(year):
    monthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - monthlyPayment
    monthlyPaymentAfterInterest = monthlyPayment - unpaidBalance * monthlyInterestRate
    balance -= monthlyPaymentAfterInterest


print("Remaining balance:", round(balance, 2))
