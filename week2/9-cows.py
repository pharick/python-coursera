n = int(input())

ld = n % 10

if 11 <= n <= 19 or ld == 0 or 5 <= ld <= 9:
    text = "korov"
elif ld == 1:
    text = "korova"
else:
    text = "korovy"

print(n, text)
