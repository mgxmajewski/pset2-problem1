# Paying Debt off in a Year

# This program calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required
# by the credit card company each month.


# Declare initial variables
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
year_months = 12
monthlyInterestRate = annualInterestRate / year_months


for month in range(year_months):
    # Calculate down payment of capital
    monthlyCapitalPayment = balance * monthlyPaymentRate

    # Calculate monthly interests
    unpaidBalance = balance - monthlyCapitalPayment
    monthlyInterestPayment = unpaidBalance * monthlyInterestRate

    # Deducting balance by capital and interest payments
    balance -= monthlyCapitalPayment - monthlyInterestPayment


print("Remaining balance:", round(balance, 2))
