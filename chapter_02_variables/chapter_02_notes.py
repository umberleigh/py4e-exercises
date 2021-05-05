# Examples of how to use variables, expressions and statements
###############################################################################

# https://www.py4e.com/html3/02-variables

# Values and types
# -----------------------------------------------------------------------------

# print a constant int
print(4)

# getting the type of constants
type('Hello, World!')  # str
type(17)  # int
type(3.2)  # float
type('22')  # str
type('92.6')  # str

# Variables
# -----------------------------------------------------------------------------

# variable assignment
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

# getting the type of variables
type(message)  # str
type(n)  # int
type(pi)  # float

# Variable names and keywords
# -----------------------------------------------------------------------------

# variable names should be snake cased, ie. some_variable_name
# they should start with letters. starting with an underscore is permitted but
# not conventional
# Variables must start with a letter or underscore and only letters, numbers
# and underscores are permitted characters
valid_var_name = 'valid'
_also_valid_but_not_recommended = 'valid'
ValidButNotRecommended = 'valid'
# 76trombones = 'not valid'
# chicken-counter 'not valid'

# Statements
# -----------------------------------------------------------------------------

# these are 3 statements. whitespace is significant in Python, statements seem
# to be delimited by newlines
print(1)
x = 2
print(x)

# Operators and operands
# -----------------------------------------------------------------------------

hour = 3
# spaces between operators are optional but i find them easier to  read
addition = 20 + 32
subtraction = hour - 1
multiplication = 24 * hour
division = 22 / 5  # Python3 always returns a float from division. Result: 4.4
floored_division = 22//5  # divides and gets the floor. Result: 4 (int)
float_floored_division = 22 // 5.1  # Result: 4.0 (float)
modulus = 22 % 5  # gets the remainder of a division. Result: 2
exponentiation = 2 ** 3  # 2 to the power of 3, ie 2 * 2 * 2. Result: 8

# Expressions
# -----------------------------------------------------------------------------

# assuming x has been assigned, these are all expressions. they are evaluated
# in the interpreter, but don't do anything by themselves in scripts
# 17
# x
# x + 17

# Order of operations
# -----------------------------------------------------------------------------

# Follows the PEMDAS rule, aka. BODMAS
# operations are evaluated in the following order of precedence:
# Parentheses eg. (3-1), aka Brackets
# Exponentiation eg. 2**3 - 2 to the power of 3, aka. Orders
# Multiplication and Division
# Addition and Subtraction

# operators with the same precedence are evaluated left to right

# Modulus operator
# -----------------------------------------------------------------------------

# Gets the remainder of a division. ie. 22 / 5 = 4, remainder 2. returns 2
print (22 % 5)

# String operations
# -----------------------------------------------------------------------------

# the + operator concatenates strings
word1 = 'monty'
word2 = 'Python'
print(word1 + word2)  # Result: montyPython

# the * operator multiplies the content of a string
print(word2 * 3)  # Result: PythonPythonPython
word3 = '2'
print(word3 * 3)  # multiplies the string, not the number. Result: 222

# Asking the user for input
# -----------------------------------------------------------------------------

# input() gets user input from the keyboard. passing a string as parameter
# displays a prompt to the user
name = input('What is your name?\n')
print(name)  # prints user's input string to stdout

# we can cast the user's input to an int or float
prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
int(speed)  # valid if the user types an int like 17

# Comments
# -----------------------------------------------------------------------------

# this is a single line comment

# multi line comments
# are usually done
# with a '#' at the start of each line
# as there's no explicit syntax for multiline comments

v = 5  # end of line comments should be preceded by 2 spaces

# Choosing mnemonic variable names
# -----------------------------------------------------------------------------

# obvious advice to use variable names that make sense and don't obfuscate
# the code is obvious. also you can't use reserved keywords as variable names.
# obviously.

# Debugging
# -----------------------------------------------------------------------------

# says obvious things about naming your variable properly to avoid syntax
# errors and using PEMDAS to avoid semantic errors
