a_s = int(input())
b_s = int(input())
c_s = int(input())
a_n = int(input())
b_n = int(input())
c_n = int(input())

case1 = (a_s // a_n) * (b_s // b_n) * (c_s // c_n)
case2 = (a_s // b_n) * (b_s // a_n) * (c_s // c_n)
case3 = (a_s // b_n) * (b_s // c_n) * (c_s // a_n)
case4 = (a_s // a_n) * (b_s // c_n) * (c_s // b_n)
case5 = (a_s // c_n) * (b_s // a_n) * (c_s // b_n)
case6 = (a_s // c_n) * (b_s // b_n) * (c_s // a_n)

print(max(case1, case2, case3, case4, case5, case6))
