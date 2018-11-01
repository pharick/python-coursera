a = int(input())
b = int(input())
n = int(input())

cost = 100 * a + b
sum = cost * n

print(sum // 100, sum % 100)
