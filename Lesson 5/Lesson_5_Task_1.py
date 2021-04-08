# Lesson 5 Task 1

import random

input_list = [random.randint(0, 100) for _ in range(10)]

print(f'Input list is: {input_list}')
print(f'Match items are: ', end='')

for item in range(1, len(input_list) - 1):
    if input_list[item - 1] < input_list[item] > input_list [item + 1]:
        print(f'{input_list[item]}(index = {item})', end=', ')
print('\b\b.')


