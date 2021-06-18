# Repeatedly read in numbers until the user enters “done”. Once “done” is
# entered, print out the total, count, and average of the numbers. If the user
# enters anything other than a number, detect their mistake using try and
# except and print an error message and skip to the next number

def calc_total(values):
    total = 0
    for value in values:
        total += value
    return total


def calc_count(values):
    count = 0
    for value in values:
        count += 1
    return count


def calc_average(values):
    tot = calc_total(values)
    cnt = calc_count(values)

    avg = tot / cnt
    return avg


value = None
values = []
while value != 'done':
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        value = float(value)
        values.append(value)
    except:
        print('Invalid input')
    value = None

total = calc_total(values)
count = calc_count(values)
average = calc_average(values)

if total.is_integer():
    total = int(total)

print(total, count, average)
