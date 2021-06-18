# modified from exercise 03.03 to use a function

# Prompt for a score between 0.0 and 1.0. If the score is out of range, print
# an error message. If the score is between 0.0 and 1.0, print a grade using
# the following table:
#    Score   Grade
#    >= 0.9     A
#    >= 0.8     B
#    >= 0.7     C
#    >= 0.6     D
#    < 0.6      F

def computegrade(score):
    error_message = 'Bad score'
    min_score = 0.0
    max_score = 1.0
    # Get input
    try:
        score = float(score)
    except:
        print(error_message)
        exit(1)

    # Handle score out of range
    if score < min_score or score > max_score:
        print(error_message)
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
        print(error_message)
        exit(3)

    # return the grade
    return grade


my_score = input('Enter a Score between 0.0 and 1.0: ')
grade = computegrade(my_score)
print(grade)
