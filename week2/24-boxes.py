l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())

case1 = l1 + l2 <= lc and w1 <= wc and w2 <= wc and h1 <= hc and h2 <= hc
case2 = l1 + w2 <= lc and w1 <= wc and l2 <= wc and h1 <= hc and h2 <= hc
case3 = w1 + l2 <= lc and l1 <= wc and w2 <= wc and h1 <= hc and h2 <= hc
case4 = w1 + w2 <= lc and l1 <= wc and l2 <= wc and h1 <= hc and h2 <= hc

case5 = l1 + l2 <= wc and w1 <= lc and w2 <= lc and h1 <= hc and h2 <= hc
case6 = l1 + w2 <= wc and w1 <= lc and l2 <= lc and h1 <= hc and h2 <= hc
case7 = w1 + l2 <= wc and l1 <= lc and w2 <= lc and h1 <= hc and h2 <= hc
case8 = w1 + w2 <= wc and l1 <= lc and l2 <= lc and h1 <= hc and h2 <= hc

case9 = h1 + h2 <= hc and l1 <= lc and l2 <= lc and w1 <= wc and w2 <= wc
case10 = h1 + h2 <= hc and w1 <= lc and l2 <= lc and l1 <= wc and w2 <= wc
case11 = h1 + h2 <= hc and l1 <= lc and w2 <= lc and w1 <= wc and l2 <= wc
case12 = h1 + h2 <= hc and w1 <= lc and w2 <= lc and l1 <= wc and l2 <= wc

if (case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8 or
   case9 or case10 or case11 or case12):
    print("YES")
else:
    print("NO")
