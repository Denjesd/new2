# Lesson 9 Task 2 is_year_leap
import random

def is_year_leap(year):

    return True if year % 4 == 0 else False

for i in range(30):
    print(is_year_leap(random.randint(0, 2100)))



