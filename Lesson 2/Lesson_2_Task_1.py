# Lesson 2 task 1

apple_number = int(input('Enter the number of apples: '))
students_number = int(input('Enter the number of students: '))

apples_in_hands = apple_number // students_number
rest_apples = apple_number % students_number

print(f'Every student get {apples_in_hands} apples\n'
      f'There are {rest_apples} apple left in the basket')
