# Lesson 2 task 1

apple_number = int(input('Enter the number of apples: '))
students_number = int(input('Enter the number of students: '))

if apple_number < students_number:
      while apple_number < students_number:
            print('\nSorry, some student does not get any apple\n'
                  'Try to input another values\n')
            apple_number = int(input('Enter the number of apples: '))
            students_number = int(input('Enter the number of students: '))

apples_in_hands = apple_number // students_number
rest_apples = apple_number % students_number

print(f'\nEvery student get {apples_in_hands} apples\n'
      f'There are {rest_apples} apple left in the basket')
