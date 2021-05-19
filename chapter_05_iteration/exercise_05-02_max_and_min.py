# Repeatedly prompt a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a
# try/except and put out an appropriate message and ignore the number

def calc_max(values):
    largest = None
    for value in values:
        if largest is None or value > largest:
            largest = value
    return largest


def calc_min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


value = None
values = []
while value != 'done':
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        value = int(value)
        values.append(value)
    except:
        print('Invalid input')
    value = None


max_val = calc_max(values)
min_val = calc_min(values)

print('Maximum is', max_val)
print('Minimum is', min_val)
