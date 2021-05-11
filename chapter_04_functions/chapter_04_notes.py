# Examples of how to use functions
###############################################################################

# https://www.py4e.com/html3/04-functions

# Function calls
# -----------------------------------------------------------------------------

# function calls are in the format function_name(param1, param2, another_param)
# eg:
type(32)


# Built-in functions
# -----------------------------------------------------------------------------

# Treat built in functions as if they were reserved words - avoid giving
# variables the same name as them.

# max and min give the largest and smallest values in a list
max('Hello world')  # returns w, highest char value, uppercase first
min('Hello world')  # returns a space, lowest char value

len('Hello world')  # returns length of object. For string it is number of chars

# These functions are not limited to strings, they can operate on any set of values

# Type conversion functions
# -----------------------------------------------------------------------------

# int() converts values to integers
int('32')  # converting the string '32' into an integer
int(3.9999999999)  # returns 3, chops off the decimal, rather than rounding
int(-2.3)  # returns 2

# float() converts integers and strings to floating point numbers
float(32)  # returns 32.0
float('3.14159')  # converts string to float of 3.14159

# str() converts to a string
str(32)  # returns '32'
str(3.14159)  # returns '3.14159'

# Math functions
# -----------------------------------------------------------------------------

# importing the math module
import math
# using dot notation, ie. module.function()
radians = 0.7
height = math.sin(radians)

# getting the value of pi
print(math.pi)

# Random numbers
# -----------------------------------------------------------------------------

# random returns a pseudorandom float between 0.0 and 1.0
import random

# print 10 random numbers up to but not including 1.0
for i in range(10):
    x = random.random()
    print(x)

# return a random integer between 5 and 10, including both
random.randint(5, 10)

# choice chooses an element from a sequence at random
t = [1, 2, 3]
random.choice(t)

# The random module also provides functions to generate random values from
# continuous distributions including Gaussian, exponential, gamma, and a few more

# Adding new functions
# -----------------------------------------------------------------------------

# PEP 8 style guide calls for 2 blank lines before and after function definitions


# using def to define a new function.
def print_lyrics():
    print('Never gonna give you up.')
    print('Never gonna let you down.')
    print('Never gonna run around and desert you.')


# calling our new function
print_lyrics()


# calling our function inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# Definitions and uses
# -----------------------------------------------------------------------------

# functions must be defined before they can be used
# it seems functions can be defined in any order
# see exercises 04.02 and 04.03

# Flow of execution
# -----------------------------------------------------------------------------

# execution starts at the first statement, one statement of a time, top to bottom
# statements inside function definitions aren't executed until called
# callstack obviousness is obvious

# Parameters and arguments
# -----------------------------------------------------------------------------

# defining a function with an argument/parameter
def print_twice(param1):  # first argument is assigned to parameter named param1
    print(param1)
    print(param1)

# calling our function, supplying an argument
print_twice('Spam')
print_twice(17)
import math
print_twice(math.pi)

# using expressions as the argument
# expression is evaluated before passing it in to the function as an argument
print_twice('Spam ' * 4)  # prints spam 8 times on 2 lines
print_twice(math.cos(math.pi))

# using a variable as the argument
michael = 'Eric, the half a bee.'
print_twice(michael)

# Fruitful functions and void functions
# -----------------------------------------------------------------------------

# a function can be described as 'fruitful' if it returns something
# you almost always want to do something with the returned value, such as
# assigning it to a variable or using it in an expression, eg.
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

# in python's interactive mode, the result of function calls are displayed

# void functions have no return value, but might display something on screen,
# or have some other effect such as mutating state
# void functions return the special value `None` (like null in PHP i think)
result = print_twice('Bing')
print(result)
print(type(result))  # <class 'NoneType'>


# returning a result from a function
def add_two(a, b):
    added = a + b
    return added


x = add_two(3, 5)
print(x)  # prints 8

# Why functions?
# -----------------------------------------------------------------------------

# name a group of statements, making it easier to debug
# functions make the program smaller by keeping it DRY
# dividing a program up in to functions let you debug one part at a time
# functions can be reused in other programs
