# Lesson 5 Task 1

import random

class_heights = sorted([random.randint(150, 200) for _ in range(10)], reverse=True)
petya_height = random.randint(150, 200)

print(f'Class heights is: {class_heights}.')
print(f'Petya\'s height is: {petya_height} cm.')

if petya_height < min(class_heights):
    class_heights.append(petya_height)
    print('Petya is the shortest in the group.')
else:
    for item in range(len(class_heights)):
        if petya_height <= class_heights[item]:
            continue
        else:
            class_heights.insert(item, petya_height)
            break

print(f'New class heights is: {class_heights}')
