n = int(input())
keyboard = list(map(int, input().split()))
k = int(input())
presses = list(map(int, input().split()))

for key in presses:
    keyboard[key - 1] -= 1

for key in keyboard:
    print("YES" if key < 0 else "NO")
