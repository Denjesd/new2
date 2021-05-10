# Lesson 13 Task 2

file = open('13_2_file.txt', 'w')

input_text = 0

while input_text != '':
    input_text = input('Enter the line: ')
    file.write(input_text + '\n')

file.close()