from collections import namedtuple

Student = namedtuple("Student", "surname name grade score")


def splitStudent(line):
    lst = line.split()
    return Student(lst[0], lst[1], int(lst[2]), int(lst[3]))


fin = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")

students = list(map(splitStudent, fin.readlines()))
students.sort(key=lambda student: student.surname)

for student in students:
    print(student.surname, student.name, student.score, file=fout)
