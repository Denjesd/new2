# Lesson 5 Task 3

import random

input_list = [random.randint(1, 100) for _ in range(15)]

print(f'Input list is: {input_list}.')
print(f'Lenght of the list is {len(input_list)}.')

index_to_delete = int(input(f'Enter index (start = 0, end = {len(input_list) - 1}) to delete: '))

while index_to_delete < 0 or index_to_delete > len(input_list) - 1:
    index_to_delete = int(input(f'Enter index in range [0;{len(input_list) - 1}] to delete: '))

for item in range(index_to_delete, (len(input_list) - 1)):
    input_list[item] = input_list[item + 1]
input_list.pop()
print(f'New list is: {input_list}.')



