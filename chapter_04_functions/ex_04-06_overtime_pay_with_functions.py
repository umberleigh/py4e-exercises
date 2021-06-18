# exercise 03.02 modified to wrap everything in a function


def computepay(hours, rate):
    # Define pseudo constants
    max_normal_hours = 40
    overtime_rate_multiplier = 1.5

    # Prompt user for hours worked and hourly rate of pay. Handle type errors by
    # showing an error and exiting the program
    try:
        hours = float(hours)
        normal_rate = float(rate)
    except:
        print('Error, please enter numeric input')
        exit(1)  # using non zero exit code to indicate failure

    overtime_rate = normal_rate * overtime_rate_multiplier

    # Separate overtime hours from normal hours
    if hours <= max_normal_hours:
        normal_hours = hours
        overtime_hours = 0
    else:
        normal_hours = max_normal_hours
        overtime_hours = hours - max_normal_hours

    # Calculate pay for normal and overtime hours
    normal_pay = normal_hours * normal_rate
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross pay
    gross_pay = normal_pay + overtime_pay

    # return the result
    return gross_pay


hrs = input('Enter Hours: ')
rte = input('Enter rate: ')
pay = computepay(hrs, rte)
print("Pay", pay)
