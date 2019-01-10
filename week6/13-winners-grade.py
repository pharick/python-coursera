from collections import namedtuple
Student = namedtuple("Student", "surname name grade score")


def splitStudent(line):
    lst = line.split()
    return Student(lst[0], lst[1], int(lst[2]), int(lst[3]))


fin = open("input.txt", "r", encoding="utf-8")
students = list(map(splitStudent, fin.readlines()))

maxScore9 = maxScoreCount9 = 0
maxScore10 = maxScoreCount10 = 0
maxScore11 = maxScoreCount11 = 0

for student in students:
    if student.grade == 9:
        if student.score > maxScore9:
            maxScore9 = student.score
            maxScoreCount9 = 1
        elif student.score == maxScore9:
            maxScoreCount9 += 1
    if student.grade == 10:
        if student.score > maxScore10:
            maxScore10 = student.score
            maxScoreCount10 = 1
        elif student.score == maxScore10:
            maxScoreCount10 += 1
    if student.grade == 11:
        if student.score > maxScore11:
            maxScore11 = student.score
            maxScoreCount11 = 1
        elif student.score == maxScore11:
            maxScoreCount11 += 1

print(maxScoreCount9, maxScoreCount10, maxScoreCount11)
