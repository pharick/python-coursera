from collections import namedtuple

Student = namedtuple("Student", "name surname grade score")


def splitStudent(line):
    lst = line.split()
    return Student(lst[0], lst[1], int(lst[2]), int(lst[3]))


fin = open("input.txt", "r", encoding="utf-8")
students = list(map(splitStudent, fin.readlines()))

count9 = count10 = count11 = 0
aver9 = aver10 = aver11 = 0

for student in students:
    if student.grade == 9:
        count9 += 1
        aver9 += student.score
    elif student.grade == 10:
        count10 += 1
        aver10 += student.score
    elif student.grade == 11:
        count11 += 1
        aver11 += student.score

print(aver9 / count9, aver10 / count10, aver11 / count11)
