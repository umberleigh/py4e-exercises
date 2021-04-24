# Examples of how to use variables, expressions and statements
###############################################################################

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
exponentiation = 2 ** 3  # 2 to the power of 3, ie 2 * 2 * 2. Result: 8

# Expressions
# -----------------------------------------------------------------------------

# todo

# Order of operations
# -----------------------------------------------------------------------------

# todo

# Modulus operator
# -----------------------------------------------------------------------------

# todo

# String operations
# -----------------------------------------------------------------------------

# todo

# Asking the user for input
# -----------------------------------------------------------------------------

# todo

# Comments
# -----------------------------------------------------------------------------

# todo

# Choosing mnemonic variable names
# -----------------------------------------------------------------------------

# todo

# Debugging
# -----------------------------------------------------------------------------

# todo
