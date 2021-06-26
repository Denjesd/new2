# Lesson 9 Task 2 is_year_leap

def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

listu = [1700, 1800, 1900, 2000, 2004, 2100]

for i in range(len(listu)):
    print(is_year_leap(listu[i]))






