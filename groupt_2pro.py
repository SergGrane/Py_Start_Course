from student_2pro import Student

class Group:
    """
    Students of University
    """
    group_size=10
    def __init__(self, student: Student, group_number: str):
        self.__student = [student]
        self.group_number = group_number

    def __str__(self):
        res = '\n'.join(map(str, self.__student))
        return f'Group_number: {self.group_number} \n{res} {len(self.__student)}'

    def add_student(self, value: Student):
        if isinstance(value, Student) and len(self.__student) < self.group_size and value not in self.__student:
            self.__student.append(value)
        return

    def del_student(self, value:Student):
        if isinstance(value, Student) and value in self.__student:
            self.__student.remove(value)
        return

    def find_student(self, value:str):
        for item in self.__student:
            if value == item.surname:
                return 'Search completed: \n' + str(item)




