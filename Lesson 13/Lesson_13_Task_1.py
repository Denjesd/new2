# Lesson 13 Task 1

from pprint import pprint

file = open('13_1_file')
new_file = open('13_1_new_file.txt', 'w')
class_book = [item.split() for item in file.read().strip().split('\n')]
new = [line.append(sum(int(x) for x in line[2:])) for line in class_book]
#pprint(class_book, width=100)

print('Students, who have AVG < 5:')
class_avg = 0
for line in class_book:
    avg = round(line[-1] / len(line[2:-1]), 2)
    new_file.write('{name:<20}{avg:>4}\n'.format(
        name=line[1] + ' ' + line[0][0].upper() + '.',
        avg=avg
    ))
    if avg < 5:
        print('{name:<20}{avg:>4}'.format(
            name=line[1] + ' ' + line[0][0].upper() + '.',
            avg=avg
        ))
    class_avg += avg
else:
    print(f'Class average mark is: {round(class_avg / len(class_book) , 2)}')

file.close()
new_file.close()