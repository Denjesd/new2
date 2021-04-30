# Lesson 10 Task 1
import random


def show_matrix(matrix, column_sum_list):
    for line in matrix:
          print(''.join('{item:>4}'.format(item=x) for x in line))
    print(''.join('{item:>4}'.format(item=x) for x in column_sum_list))

def show_matrix_easy(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def matrix_sort(array, column_sum_list):                                #Columns sort block
    for i in range(len(column_sum_list)):
        flag = True
        for j in range(len(column_sum_list)-1-i):
            if column_sum_list[j] > column_sum_list[j+1]:
                column_sum_list[j], column_sum_list[j+1] = column_sum_list[j+1], column_sum_list[j]
                for k in range(len(array)):
                    array[k][j], array[k][j + 1] = array[k][j + 1], array[k][j]

                flag = False
        if flag:
            break


    for j in range(len(array)):
        flag = True                                                                     # Inside-columns sort block
        if j % 2 == 0:
            for k in range(len(array) - 1):
                for i in range(len(array) - 1 - k):
                    if array[i][j] < array[i+1][j]:
                        array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
                        flag = False
                if flag:
                    break

        else:
            for k in range(len(array) - 1):
                for i in range(len(array) - 1 - k):
                    if array[i][j] > array[i+1][j]:
                        array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
                        flag = False
                if flag:
                    break


matrix_size = int(input('Enter the size of the matrix (size >= 5): '))
while matrix_size < 5:
    matrix_size = int(input('Value is < 5.\nEnter another size of the matrix (size >= 5: '))
matrix = [[random.randint(1, 50) for _ in range(matrix_size)] for _ in range(matrix_size)]


# matrix = [
#     [10, 50, 10, 50, 10],
#     [20, 40, 20, 40, 20],
#     [30, 30, 30, 30, 30],
#     [40, 20, 40, 20, 40],
#     [50, 10, 50, 10, 50]
#     ]
column_sum_list = [0 for _ in range(matrix_size)]
for row in range(len(matrix)):
    for column in range(len(matrix)):
        column_sum_list[row] += matrix[column][row]

print('\nUnsorted matrix:')
show_matrix(matrix, column_sum_list)
matrix_sort(matrix, column_sum_list)
print('\nSorted matrix:')
show_matrix(matrix,column_sum_list)

