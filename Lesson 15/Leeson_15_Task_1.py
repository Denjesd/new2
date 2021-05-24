# Lesson 15 Task 1

class Group:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.group_list = []

    def show_group(self):
        print('Group', self.__group_name, ':')
        for student in self.group_list:
            student.get_info()


    pass
class Student:
    def __init__(self, group, name, surname, *grades):
        group.group_list.append(self)
        self.__name = name
        self.__surname = surname
        self.grades = list(grades)

    def get_info(self):
        print(self.__name, self.__surname, self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def edit_grade(self, mark_index, new_grade):
        if mark_index > len(self.grades):
            print('There is no such mark.')
        else:
            self.grades[mark_index] = new_grade


group_A = Group('A')
student_1 = Student(group_A, 'John', 'Smith', 1, 2, 3, 4)
student_2 = Student(group_A, 'Albert', 'Smith', 1, 2, 3, 4)
student_1.get_info()
student_1.add_grade(5)
student_1.get_info()
group_A.show_group()
