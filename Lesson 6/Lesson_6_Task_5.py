# Lesson 6 Task 5

input_list_1 = [1, 1, 1, 2, 2, 2, 3, 3, 4]
input_list_2 = [2, 2, 4, 5, 5, 6, 6, 8, 9, 9]
print(f'Our set is: {set({elem for elem in input_list_1}) ^ set({item for item in input_list_2})}')