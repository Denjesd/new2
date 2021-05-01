# Lesson 10 Task 2
import random


matrix_size = (
                int(input('Matrix M*N is requested.\nEnter the M of the matrix (size >= 3): ')),
                int(input('Enter the N of the matrix (size >= 3): '))
              )
while matrix_size[0]  < 3 or matrix_size[1] < 3:
    print('One of the values is < 3.\nEnter another values of size (size >= 3): ')
    matrix_size = [
        int(input('Enter the M of the matrix (size >= 3): ')),
        int(input('Enter the N of the matrix (size >= 3): '))
    ]
matrix = [[random.randint(1, 50) for _ in range(matrix_size[0])] for _ in range(matrix_size[1])]

summ_list = [0 for _ in range(matrix_size[1])]
for row in range(matrix_size[1]):
    for column in range(matrix_size[0]):
        summ_list[row] += matrix[row][column]

for line in range(len(matrix)):
    print(''.join('{item:>4}'.format(item=x) for x in matrix[line]) + '   ' + str(summ_list[line]))

summ_list = [0 for _ in range(matrix_size[0])]
for column in range(matrix_size[0]):
    for row in range(matrix_size[1]):
        summ_list[column] += matrix[row][column]

print(''.join('{item:>4}'.format(item=x) for x in summ_list))

