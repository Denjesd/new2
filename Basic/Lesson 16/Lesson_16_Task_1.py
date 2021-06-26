# Lesson 16 Task 1

class Buffer:
    def __init__(self):
        self.values_list = []
        self.sums_list = []
    # конструктор без аргументов

    def add(self, *a):
        for item in a:
            self.values_list.append(item)
    # добавить следующую часть последовательности

    def get_current_part(self):
        while len(self.values_list) >= 5:
            items_sum = sum(self.values_list[:5])
            self.sums_list.append(items_sum)
            print(items_sum, end=' ')
            del self.values_list[:5]
        print()

    def get_general_sums_list(self):
        print(self.sums_list)

    # вернуть сумму пяти сохраненных элементов последовательности

buffer = Buffer()
buffer.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
buffer.get_current_part()
buffer.add(6, 7, 8)
buffer.get_current_part()
buffer.get_general_sums_list()
