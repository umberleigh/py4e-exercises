# Prompt user for hours worked and hourly rate of pay.
# multiply the two together as float and display the result
hours = input('Enter Hours: ')
rate = input('Enter rate: ')
gross_pay = float(hours) * float(rate)
print('Pay:', gross_pay)