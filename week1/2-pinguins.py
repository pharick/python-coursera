def pinguin(number):
  lines = number // 10
  last_line = number % 10

  for _ in range(lines):
    print("   _~_    " * 10)
    print("  (o o)   " * 10)
    print(" /  V  \\  " * 10)
    print("/(  _  )\\ " * 10)
    print("  ^^ ^^   " * 10)

  if last_line > 0:
    print("   _~_    " * last_line)
    print("  (o o)   " * last_line)
    print(" /  V  \\  " * last_line)
    print("/(  _  )\\ " * last_line)
    print("  ^^ ^^   " * last_line)

number = int(input())
pinguin(number)