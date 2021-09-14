# Huu Hung Nguyen
# 09/13/2021
# Nguyen_HuuHung_payment.py
# The program prompts the user for the amount of the loan,
# the annual percentage rate, and the number of years of the loan.
# It then calculates monthly payments on a loan and prints the result.


# Prompt user for principal
p = float(input('Enter amount of loan: $'))

# Prompt user for annual interest rate as a percent 
annual_rate = float(input('Enter annual interest rate as a percent: '))

# Prompt user for number of years for the loan
years = int(input('Enter number of years for the loan: '))

# Calculate monthly interest rate
r = annual_rate / 12

# Calculate number of months of the loan
n = years * 12

# Calculate monthly payment on the loan
payment = p * r/100 * (1 + r/100)**n / ((1+r/100)**n - 1)

# Print result
print('Your monthly payment is ${:.2f}.'.format(payment))