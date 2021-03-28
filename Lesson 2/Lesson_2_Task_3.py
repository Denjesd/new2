# Lesson 2 Task 3

first_number = int(input('Enter the first number: '))   # будем представлять число как 100*a + 10*b + c
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

def reverse(number):
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10

    new_number = third_digit * 100 + second_digit * 10 + first_digit
    return new_number


print(reverse(first_number), reverse(second_number), reverse(third_number))