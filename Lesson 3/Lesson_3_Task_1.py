# Lesson 3 Task 1

input_number = int(input('Enter positive number, n > 0: '))
while input_number <= 0:
    print('\nYour number is negative or Zero, '
          'please enter another number.\n')
    input_number = int(input('Enter positive number, n > 0: '))

power_of_two = 0
current_value = 1
while (current_value * 2) < input_number:
    power_of_two += 1
    current_value *= 2

print(f'The max power of two is {power_of_two}\n'
      f'The max value is {current_value}')
