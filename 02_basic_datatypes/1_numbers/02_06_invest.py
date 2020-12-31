'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

p_values = float(input("How much would you like to invest: "))
inv_values = float(input("what's your interest rate: "))
duration = float(input('For how long: '))
interest = float(inv_values / 100)
future_value = float(p_values * (1 + interest) ** duration)
print(future_value)
