# Prompt for a score between 0.0 and 1.0. If the score is out of range, print
# an error message. If the score is between 0.0 and 1.0, print a grade using
# the following table:
#    Score   Grade
#    >= 0.9     A
#    >= 0.8     B
#    >= 0.7     C
#    >= 0.6     D
#    < 0.6      F

ERROR_MESSAGE = 'Bad score'
MIN_SCORE = 0.0
MAX_SCORE = 1.0
# Get input
try:
    score = input('Enter a Score between ' + str(MIN_SCORE) + ' and ' + str(MAX_SCORE) + ': ')
    score = float(score)
except:
    print(ERROR_MESSAGE)
    exit(1)

# Handle score out of range
if score < MIN_SCORE or score > MAX_SCORE:
    print(ERROR_MESSAGE)
    exit(2)

# Select grade
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score < 0.6:
    grade = 'F'
else:
    print(ERROR_MESSAGE)
    exit(3)

# Show the user their grade
print(grade)
