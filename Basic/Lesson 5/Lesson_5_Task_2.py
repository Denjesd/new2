# Lesson 5 Task 1

import random

class_heights = sorted([random.randint(150, 200) for _ in range(10)], reverse=True)
petya_height = random.randint(150, 200)
#class_heights = [197, 196, 185, 175, 175, 175, 167, 167, 163, 154]
#petya_height = 175

print(f'Class heights is: {class_heights}.')
print(f'Petya\'s height is: {petya_height} cm.')
petya_position = 1

if petya_height < min(class_heights):
    class_heights.append(petya_height)
    print('Petya is the shortest in the group, he has to take last position.')
else:
    for item in range(len(class_heights)):
        if petya_height <= class_heights[item]:
            petya_position += 1
            continue
        else:
            class_heights.insert(item, petya_height)
            print(f'Petya has to take {petya_position} place in the raw.')
            break


print(f'New class heights is: {class_heights}')

