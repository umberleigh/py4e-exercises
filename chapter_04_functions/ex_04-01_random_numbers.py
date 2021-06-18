# run this program multiple times to show that it produces different output
# each time

import random
# random returns a pseudorandom float between 0.0 and 1.0
# print 10 random numbers up to but not including 1.0
for i in range(10):
    x = random.random()
    print(x)
