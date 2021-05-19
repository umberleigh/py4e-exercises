# Examples of how to use Iteration
###############################################################################

# https://www.py4e.com/html3/05-iterations

# Updating variables
# -----------------------------------------------------------------------------

# variables need initialising before we can perform operations on them
x = 0  # initialisation
x += 1  # now we can do our operation, ie incrementing x


# The while statement
# -----------------------------------------------------------------------------

# while loop example
n = 5
while n > 0:
    print(n)
    n -= 1
print('Blastoff!')


# Infinite loops
# -----------------------------------------------------------------------------

# this is an infinite loop because the while condition is always True and
# there's no break statement
n = 10
while True:
    print(n, end=' ')
    n -= 1
print('Done!')

# in this instance, the loop is not infinite. it will continue looping forever
# until we hit the break clause (ie. input of 'done')
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


# Finishing iterations with continue
# -----------------------------------------------------------------------------

# continue is used to immediately exit the current iteration and jump to the
# next iteration

# print any input that isn't done or beginning with a # character
# if input starts with #, skip to next iteration
# if input is 'done' exit our loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


# Definite loops using for
# -----------------------------------------------------------------------------

# use for loops to iterate over a definite number of items
# ie. a known set of items of a finite size
friends = ['Joana', 'Felix', 'Megan', 'Davie']  # list of strings
for friend in friends:  # iterate over our list, using current item as friend
    print('Happy new year:', friend)
print('Done!')


# Loop patterns
# -----------------------------------------------------------------------------

# loops are often used to look for something in whatever we're iterating over
# eg. the largest or smallest value
# this is dome by:
#   - initialising variables before the loop starts
#   - performing computations on each item in the loop body, changing variables
#   - looking at the result after the loop completes


# Counting and summing loops
# -----------------------------------------------------------------------------

# loop to count number of items in a list, prints 'Count: 6'
# initialise data and counter
list_of_nums = [3, 41, 12, 9, 74, 15]
count = 0
for i in list_of_nums:  # iterate over our list
    count += 1  # increment count of number of items
print('Count: ', count)  # print our total number of items

# loop to add together items in a list and print the total
# prints 'Total: 154'
# initialise data and running total
list_of_nums = [3, 41, 12, 9, 74, 15]
total = 0
for i in list_of_nums:  # iterate over our list
    total += i  # add the value of current item in list to running total
print('Total: ', total)  # print out the total we added up

# in real life, we'd use len() to get the number of items in a list
# we'd use sum() to add all the values in a list together to get the total

# Maximum and minimum loops
# -----------------------------------------------------------------------------

# calculate max value using a loop
largest = None
list_of_nums = [3, 41, 12, 9, 74, 15]
print('Before:', largest)
for i in list_of_nums:
    if largest is None or i > largest:
        largest = i
    print('Loop:', i, largest)
print('Largest:', largest)

# calculate min value using a loop
smallest = None
list_of_nums = [3, 41, 12, 9, 74, 15]
print('Before:', smallest)
for i in list_of_nums:
    if smallest is None or i < smallest:
        smallest = i
    print('Loop:', i, smallest)
print('Smallest:', smallest)

# as in counting and summing, the built-in functions max() and min() make
# writing these exact loops unnecessary

# min as a function
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
