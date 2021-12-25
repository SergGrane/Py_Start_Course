from student_2pro import Student


class Group:
    """
    Students of University
    """
    GROUP_SIZE = 10
    def __init__(self, student: Student, group_number: str):
        self.__student = [student]
        self.group_number = group_number

    def __str__(self):
        res = '\n'.join(map(str, self.__student))
        return f'Group_number: {self.group_number} \n{res} {len(self.__student)}'

    def add_student(self, value: Student):
        try:
            if len(self.__student) == self.GROUP_SIZE:
                raise UserError("excess of the group size")
            elif not isinstance(value, Student):
                raise UserError("Student is not valid")
            elif value in self.__student:
                raise UserError("Student is already present")
        except UserError as err:
            print(err)
            return
        self.__student.append(value)
        return None

    def del_student(self, value:Student):
        if isinstance(value, Student) and value in self.__student:
            self.__student.remove(value)
        return

    def find_student(self, value:str):
        for item in self.__student:
            if value == item.surname:
                return 'Search completed: \n' + str(item)

class UserError(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return(self.message)



