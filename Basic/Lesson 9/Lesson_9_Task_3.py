# Lesson 9 Task 3
import math

def square(side_value):

    perimetr = side_value * 4
    area = side_value * side_value
    diagonal = round(side_value * math.sqrt(2), 4)

    return  perimetr, area, diagonal

