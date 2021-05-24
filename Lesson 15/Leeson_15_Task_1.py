# Lesson 15 Task 1

class Group:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.group_list = []

    def show_group(self):
        print('Group', self.__group_name, ':')
        for student in self.group_list:
            student.get_info()

    def add_student_to_group(self, student):
        self.group_list.append(student)

    def delete_student_from_group(self, student):
        self.group_list.remove(student)


class Student:
    def __init__(self, name, surname, *grades):
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
student_1 = Student('John', 'Smith', 1, 2, 3, 4)
student_2 = Student('Albert', 'Smith', 1, 2, 3, 4)
group_A.add_student_to_group(student_1)
group_A.add_student_to_group(student_2)
group_A.show_group()
group_A.delete_student_from_group(student_1)
group_A.show_group()
