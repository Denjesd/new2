# Lesson 3 Task 3

input_value = ''
counter = 0
values_sum = 0
min_value = ''
max_value = ''
even_counter = 0
odd_counter = 0

while input_value != 0:

    input_value = int(input(f'Enter the number (index = {counter}): '))

    if input_value == 0:
        continue
    elif counter == 0:
        min_value = input_value
        max_value = input_value

    counter += 1
    values_sum += input_value

    if input_value < min_value:
        min_value = input_value

    if input_value > max_value:
        max_value = input_value

    if input_value % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f'\nThe number of inputs is {counter}.')
print(f'The summ of values is {values_sum}.')
print(f'An Average number is {values_sum / counter}.')
print(f'The minimal value is {min_value}.')
print(f'The maximal value is {max_value}.')
print(f'The number of even numbers is {even_counter}.')
print(f'The number of odd numbers is {odd_counter}.')

