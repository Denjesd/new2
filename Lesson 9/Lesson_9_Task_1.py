# Lesson 9 Task 1 calculator

def arithmetic(num_a, num_b, operator):

    if operator == '+':
        return num_a + num_b
    if operator == '-':
        return num_a - num_b
    if operator == '*':
        return num_a * num_b
    if operator == '/':
        return num_a / num_b

input_value_1 = int(input('Enter the first number: '))
input_value_2 = int(input('Enter the second number: '))
input_operator = input('Enter the opetaror (+, -, *, /) : ')

print(f'Your result is: {arithmetic(input_value_1, input_value_2, input_operator)}')

