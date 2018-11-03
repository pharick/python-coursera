a = int(input())
b = int(input())
c = int(input())

is_one_even = a % 2 == 0 or b % 2 == 0 or c % 2 == 0
is_one_odd = a % 2 == 1 or b % 2 == 1 or c % 2 == 1

if is_one_even and is_one_odd:
    print("YES")
else:
    print("NO")
