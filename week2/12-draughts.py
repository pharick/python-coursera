start_x = int(input())
start_y = int(input())
finish_x = int(input())
finish_y = int(input())

is_on_diag = ((finish_x % 2 == 1 and finish_y % 2 == 1) or
              (finish_x % 2 == 0 and finish_y % 2 == 0))
is_on_top = (finish_y >= finish_x - (start_x - start_y) and
             finish_y >= (start_x + start_y) - finish_x)

if is_on_diag and is_on_top:
    print("YES")
else:
    print("NO")
