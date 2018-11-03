a = int(input())
b = int(input())
c = int(input())

equals = 0

if a == b or b == c or a == c:
    equals = 2
if a == b == c:
    equals = 3

print(equals)
