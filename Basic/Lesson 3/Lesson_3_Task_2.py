# Lesson 3 Task 2

input_number = int(input('Enter positive number, n > 0: '))
while input_number <= 0:
    print('\nYour number is negative or Zero, '
          'please enter another number.\n')
    input_number = int(input('Enter positive number, n > 0: '))

current_value = 1
print('Your powers raw is:', end=' ')
while current_value * current_value <= input_number:
    print(current_value * current_value, end=' ')
    current_value += 1


