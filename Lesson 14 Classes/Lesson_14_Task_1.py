# Lesson 14 Task 1
#
class Counter:

    def __init__(self, floor_border, ceiling_border):
        self.floor_border = floor_border
        self.ceiling_border = ceiling_border
        self.current_count = floor_border

    def add_count(self):
        if self.current_count < self.ceiling_border:
            self.current_count += 1
        else:
            print('Counter on the ceiling value')

    def get_count(self):
        print('Current count is', self.current_count)

counter = Counter(10, 50)
counter.get_count()
counter.add_count()
counter.get_count()