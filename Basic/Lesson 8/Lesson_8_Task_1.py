# Lesson 8 Task 1

def show_triangle(triangle):
    for i in triangle:
         print(''.join(i))

def draw_upper_triangle(triangle_height):
    array = []
    for height_step in range(triangle_height - 1 , -1, -1):
        generated_list = [' ' for _ in range(triangle_height * 2 - 1)]
        generated_list[height_step]  = '*'
        generated_list[-height_step - 1] = '*'
        array.append(generated_list)
    else:
        for item in range(len(array[-1])):
            array[triangle_height - 1][item] = '*'

    show_triangle(array)
    return array


def paint_upper_triangle(triangle, triangle_height):
    for i in range(1, triangle_height - 1):
        for j in range(triangle[i].index('*') + 1, len(triangle[i]) - triangle[i].index('*') - 1):
            triangle[i][j] = '*'
    show_triangle(triangle)

def draw_lower_triangle(triangle, triangle_height):

    for height_step in range(1, triangle_height):
        generated_list = [' ' for _ in range(triangle_height * 2 - 1)]
        generated_list[height_step]  = '*'
        generated_list[-height_step-1] = '*'
        triangle.append(generated_list)
    show_triangle(triangle)
    return triangle

def draw_vertical_diagonal(triangle, triangle_height):
    center_index = triangle_height - 1
    for i in range(1, len(triangle) - 1):
        triangle[i][center_index] = '*'
    show_triangle(triangle)


###--------------------MAIN--------------------###


triangle_height = int(input('Enter the height of triangle (height might be %2 = 1): '))
while triangle_height % 2 == 0 or triangle_height < 0:
    if triangle_height < 0:
        triangle_height = int(input('Your value is negative.\n'
                                    'Try another value: 0 < value % 2 == 1:'))
    else:
        triangle_height = int(input('Your value is even.\n'
                                    'Try another value: 0 < value % 2 == 1:'))

print('Case 1: ')
actual_triangle = draw_upper_triangle(triangle_height)
print('Case 2: ')
paint_upper_triangle(actual_triangle, triangle_height)
print('Case 3: ')
actual_triangle = draw_lower_triangle(actual_triangle, triangle_height)
print('Case 4: ')
draw_vertical_diagonal(actual_triangle, triangle_height)


