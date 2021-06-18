# Pay calculator from exercise 02.03 rewritten to give the employee 1.5 times
# the hourly rate for hours worked above 40 hours, now with error handling for input!

# Define constants
MAX_NORMAL_HOURS = 40
OVERTIME_RATE_MULTIPLIER = 1.5

# Prompt user for hours worked and hourly rate of pay. Handle type errors by
# showing an error and exiting the program
try:
    hours = input('Enter Hours: ')
    hours = float(hours)
    rate = input('Enter rate: ')
    normal_rate = float(rate)
except:
    print('Error, please enter numeric input')
    exit(1)  # using non zero exit code to indicate failure

overtime_rate = normal_rate * OVERTIME_RATE_MULTIPLIER

# Separate overtime hours from normal hours
if hours <= MAX_NORMAL_HOURS:
    normal_hours = hours
    overtime_hours = 0
else:
    normal_hours = MAX_NORMAL_HOURS
    overtime_hours = hours - MAX_NORMAL_HOURS

# Calculate pay for normal and overtime hours
normal_pay = normal_hours * normal_rate
overtime_pay = overtime_hours * overtime_rate

# Calculate gross pay
gross_pay = normal_pay + overtime_pay

# Display result to user
print('Pay:', gross_pay)
