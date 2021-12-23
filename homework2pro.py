from people_2pro import People
from student_2pro import Student
from groupt_2pro import Group

if __name__ == '__main__':

    people1 = People('Vasja', 'Pupkin', '12.21')
    print(people1)

    student1 = Student('Vasja', 'Ivanov', '12.21', 'power stations')
    student2 = Student('Vasja', 'Petrov', '12.21', 'power stations')
    student3 = Student('Vasja', 'Pupkin', '12.21', 'power stations')
    print(student1)

    group1=Group( [student1, student2], '112-1')
    group1.add_student(student2)
    group1.add_student(student3)
    group1.del_student(student1)
    print(group1)
    print(group1.find_student('Pupkin'))




