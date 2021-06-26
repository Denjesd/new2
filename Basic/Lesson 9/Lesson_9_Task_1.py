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
    else:
        return 'Неизвестная оперция'


