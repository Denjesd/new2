# Lesson 8 Task 1
from Lesson_8_modules import *

###--------------------MAIN--------------------###
input('''\n
---------------Welcome to drawing machine----------------
---------------Developed by Dolbnia Denis----------------
---------------Size up you terminal window---------------
-----------------Press ENTER to continue-----------------''')
triangle_height = int(input('Enter the height of triangle (height might be %2 = 1): '))
while triangle_height % 2 == 0 or triangle_height < 0:
    if triangle_height < 0:
        triangle_height = int(input('Your value is negative.\n'
                                    'Try another value: 0 < value % 2 == 1:'))
    else:
        triangle_height = int(input('Your value is even.\n'
                                    'Try another value: 0 < value % 2 == 1:'))

command = input('Enter (UT) to draw the first triangle.').lower()
actual_triangle = draw_upper_triangle(triangle_height)
while command != 'q':
    print('Enter (LT) to draw the lower triangle.')
    print('Enter (PUT) to paint the upper triangle.')
    print('Enter (CUT) to clear the upper triangle.')
    print('Enter (PLT) to paint the lower triangle.')
    print('Enter (CLT) to clear the lower triangle.')
    print('Enter (HD) to draw horizontal diagonal.')
    print('Enter (VD) to draw vertical diagonal.')
    print('Enter (CHD) to clear horizontal diagonal.')
    print('Enter (CVD) to clear vertical diagonal.')
    print('Enter (Q) to close the program.')
    command = input().lower()

    if command == 'q':
        print('---------------Have a nice day, see you soon!---------------')
        input('----------Press ENTER to close the drawing machine.---------')
        break
    if command == 'lt':
        actual_triangle = draw_lower_triangle(actual_triangle, triangle_height)
    if command == 'put':
        paint_upper_triangle(actual_triangle,triangle_height)
    if command == 'plt':
        paint_lover_triangle(actual_triangle, triangle_height)
    if command == 'vd':
        draw_vertical_diagonal(actual_triangle, triangle_height)
    if command == 'hd':
        draw_horizontal_diagonal(actual_triangle)
    if command == 'cut':
        clear_upper_triangle(actual_triangle, triangle_height)
    if command == 'clt':
        clear_lower_triangle(actual_triangle)
    if command == 'cvd':
        clear_vertical_diagonal(actual_triangle, triangle_height)
    if command == 'chd':
        clear_horizontal_diagonal(actual_triangle)




