# Lesson 14 Task 1

class Counter:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current_count = min

    def add_count(self):

        self.current_count += 1 if self.current_count < self.max \
            else print('Counter on the ceiling value')

    def get_count(self):
        print('Current count is', self.current_count)

counter = Counter(10, 50)
counter.get_count()
counter.add_count()
counter.get_count()
# for _ in range(120):
#     counter.add_count()
#     counter.get_count()
