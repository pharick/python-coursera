a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

case1 = (a1 == a2) and (b1 == b2) and (c1 == c2)
case2 = (a1 == b2) and (b1 == a2) and (c1 == c2)
case3 = (a1 == b2) and (b1 == c2) and (c1 == a2)
case4 = (a1 == a2) and (b1 == c2) and (c1 == b2)
case5 = (a1 == c2) and (b1 == a2) and (c1 == b2)
case6 = (a1 == c2) and (b1 == b2) and (c1 == a2)

if case1 or case2 or case3 or case4 or case5 or case6:
    print("Boxes are equal")
else:
    case1 = (a1 >= a2) and (b1 >= b2) and (c1 >= c2)
    case2 = (a1 >= b2) and (b1 >= a2) and (c1 >= c2)
    case3 = (a1 >= b2) and (b1 >= c2) and (c1 >= a2)
    case4 = (a1 >= a2) and (b1 >= c2) and (c1 >= b2)
    case5 = (a1 >= c2) and (b1 >= a2) and (c1 >= b2)
    case6 = (a1 >= c2) and (b1 >= b2) and (c1 >= a2)

    if case1 or case2 or case3 or case4 or case5 or case6:
        print("The first box is larger than the second one")
    else:
        case1 = (a1 <= a2) and (b1 <= b2) and (c1 <= c2)
        case2 = (a1 <= b2) and (b1 <= a2) and (c1 <= c2)
        case3 = (a1 <= b2) and (b1 <= c2) and (c1 <= a2)
        case4 = (a1 <= a2) and (b1 <= c2) and (c1 <= b2)
        case5 = (a1 <= c2) and (b1 <= a2) and (c1 <= b2)
        case6 = (a1 <= c2) and (b1 <= b2) and (c1 <= a2)

        if case1 or case2 or case3 or case4 or case5 or case6:
            print("The first box is smaller than the second one")
        else:
            print("Boxes are incomparable")
