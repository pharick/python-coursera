n = int(input()) % 86400

h = n // 3600
n %= 3600

m = n // 60
n %= 60

s = n

print(h, ":",
      m // 10, m % 10, ":",
      s // 10, s % 10,
      sep="")
