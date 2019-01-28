fin = open("input.txt", "r", encoding="utf-8")
a_num, b_num = map(int, fin.readline().split())

a_set = set()
b_set = set()

for i in range(a_num):
    a_set.add(int(fin.readline()))
for i in range(b_num):
    b_set.add(int(fin.readline()))


in_both = sorted(a_set & b_set)
print(len(in_both))
print(*in_both)

only_a = sorted(a_set - b_set)
print(len(only_a))
print(*only_a)

only_b = sorted(b_set - a_set)
print(len(only_b))
print(*only_b)
