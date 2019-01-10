from collections import namedtuple
Student = namedtuple("Student", "surname name grade score")


def splitStudent(line):
    lst = line.split()
    return Student(lst[0], lst[1], int(lst[2]), int(lst[3]))


fin = open("input.txt", "r", encoding="utf-8")
students = list(map(splitStudent, fin.readlines()))

maxScore9 = maxScore10 = maxScore11 = 0
for student in students:
    if student.grade == 9 and student.score > maxScore9:
        maxScore9 = student.score
    elif student.grade == 10 and student.score > maxScore10:
        maxScore10 = student.score
    elif student.grade == 11 and student.score > maxScore11:
        maxScore11 = student.score

print(maxScore9, maxScore10, maxScore11)
