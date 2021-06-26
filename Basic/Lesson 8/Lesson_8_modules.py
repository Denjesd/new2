

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

def draw_lower_triangle(triangle, triangle_height):

    for height_step in range(1, triangle_height):
        generated_list = [' ' for _ in range(triangle_height * 2 - 1)]
        generated_list[height_step]  = '*'
        generated_list[-height_step-1] = '*'
        triangle.append(generated_list)
    show_triangle(triangle)
    return triangle

def paint_upper_triangle(triangle, triangle_height):
    for i in range(1, triangle_height - 1):
        for j in range(triangle[i].index('*') + 1, len(triangle[i]) - triangle[i].index('*') - 1):
            triangle[i][j] = '*'
    show_triangle(triangle)

def paint_lover_triangle(triangle, triangle_height):
    if len(triangle) < triangle_height * 2 - 1:
        print('There is no lower tringle.')
    else:
        for i in range(triangle_height, triangle_height * 2 - 1):
            for j in range(triangle[i].index('*') + 1, len(triangle[i]) - triangle[i].index('*') - 1):
                triangle[i][j] = '*'
        show_triangle(triangle)

def draw_vertical_diagonal(triangle, triangle_height):
    center_index = triangle_height - 1
    for i in range(1, len(triangle) - 1):
        triangle[i][center_index] = '*'
    show_triangle(triangle)

def draw_horizontal_diagonal(triangle):
    center_index = len(triangle) // 2
    for i in range(len(triangle)):
        triangle[center_index][i] = '*'
    show_triangle(triangle)

def clear_upper_triangle(triangle, triangle_height):
    for i in range(1, triangle_height - 1):
        for j in range(triangle[i].index('*') + 1, len(triangle[i]) - triangle[i].index('*') - 1):
                triangle[i][j] = ' '
    show_triangle(triangle)

def clear_lower_triangle(triangle, triangle_height):

    if len(triangle) < triangle_height * 2 - 1:
        print('There is no lower tringle.')
    else:
        for i in range(triangle_height, triangle_height * 2 - 1):
            for j in range(triangle[i].index('*') + 1, len(triangle[i]) - triangle[i].index('*') - 1):
                triangle[i][j] = ' '
        show_triangle(triangle)

def clear_vertical_diagonal(triangle, triangle_height):
    center_index = triangle_height - 1

    for i in range(1, len(triangle) - 1):
        if i != center_index:
            triangle[i][center_index] = ' '
        elif triangle[i][center_index - 1] == '*':
            continue
        else:
            triangle[i][center_index] = ' '

            continue
    show_triangle(triangle)

def clear_horizontal_diagonal(triangle):
    center_index = len(triangle) // 2

    for i in range(1, len(triangle) - 1):
        if i != center_index:
            triangle[center_index][i] = ' '
        elif triangle[center_index - 1][i] == '*' and triangle[center_index + 1][i] == '*':
            continue
        else:
            triangle[center_index][i] = ' '
    show_triangle(triangle)
