# Examples of how to use conditional execution
###############################################################################

# https://www.py4e.com/html3/03-conditional

# Boolean expressions
# -----------------------------------------------------------------------------

# use == to compare two operands, true if they're equal, false if they're not
5 == 5  # True
5 == 6  # False

x = 1
y = 2

# other boolean operators
x != y  # x is not equal to y
x > y  # x is greater than y
x < y  # x is less than y
x >= y  # x is greater than or equal to y
x <= y  # x is less than or equal to y
x is y  # x is the same as y
x is not y  # x is not the same as y

# Logical operators
# -----------------------------------------------------------------------------

# there are 3 logical operators: and or not
# Any nonzero number is interpreted as “true.”

# Conditional execution
# -----------------------------------------------------------------------------

# note that block statements like if, for etc. use 4 spaces of indentation
# to denote what's inside the block. deindent to exit the block

# if statement
if x > 0:
    print('x is positive')

# pass does nothing. can be useful to have a body with no statements as a placeholder
if x < 0:
    pass

# Alternative execution
# -----------------------------------------------------------------------------

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

# Chained conditionals
# -----------------------------------------------------------------------------

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


# Nested conditionals
# -----------------------------------------------------------------------------

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# nesting conditionals gets hard to read quickly, take this code:
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

# the above can be simplified by using the and operator
if 0 < x and x < 10:
    print('x is a positive single-digit number.')

# Catching exceptions using try and except
# -----------------------------------------------------------------------------

# wrap code that may cause problems (exceptions) in a try block.
# except: handle the error / exception in this block
input_temp = input('Enter Fahrenheit Temperature:')
try:
    fahr_temp = float(input_temp)  # cast to float
    celcius_temp = (fahr_temp - 32.0) * 5.0 / 9.0  # convert temp
    print(celcius_temp)
except:
    print('Please enter a number')


# Short-circuit evaluation of logical expressions
# -----------------------------------------------------------------------------

# logical expressions are evaluated left to right
# eg. in the following expression, if x is less than 2, only x >= 2
# is evaluated. this is called 'short circuiting'
x >= 2 and (x/y) > 2

# this can be used to implement the 'guard pattern' - ie. putting a guard
# evaluation first to check for things that can cause errors like division by zero
x = 6
y = 0
# because the check for y not being 0 comes before the division, `y != 0 stops
# the division being executed if y is 0 - it guards against an error.
x >= 2 and y != 0 and (x/y) > 2


# Debugging
# -----------------------------------------------------------------------------

# Tracebacks show what kind of error occurred and where
# Whitespace errors can be tricky as the actual error may be earlier in the
# code, sometimes on a previous line
