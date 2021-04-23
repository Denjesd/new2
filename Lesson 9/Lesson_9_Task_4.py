# Lesson 9 Task 4

def season(month_number):

    winter = [12, 1, 2]
    spring = [3, 4 ,5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if month_number in winter:
        return 'winter'

    if month_number in spring:
        return 'spring'

    if month_number in summer:
        return 'summer'

    if month_number in autumn:
        return 'autumn'

