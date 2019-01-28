n = int(input())

all_students = set()
one_student = set()

for i in range(n):
    m = int(input())

    student_langs = set()
    for j in range(m):
        student_langs.add(input())

    if i == 0:
        all_students = student_langs
    else:
        all_students &= student_langs

    one_student |= student_langs

print(len(all_students))
print(*all_students, sep="\n")
print(len(one_student))
print(*one_student, sep="\n")
