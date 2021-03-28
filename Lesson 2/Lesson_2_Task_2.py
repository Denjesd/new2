# Lesson 2 Task 2

class_1 = int(input('Enter the number of studendts in class 1: '))
class_2 = int(input('Enter the number of studendts in class 2: '))
class_3 = int(input('Enter the number of studendts in class 3: '))

desk_to_class_1 = class_1 // 2 + class_1 % 2
desk_to_class_2 = class_2 // 2 + class_2 % 2
desk_to_class_3 = class_3 // 2 + class_3 % 2

print(f'School has to buy {desk_to_class_1 + desk_to_class_2 + desk_to_class_3} desks.')


