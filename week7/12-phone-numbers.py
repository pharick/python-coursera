def unify_number(number):
    result = ""
    for s in number:
        if s != "(" and s != ")" and s != "-" and s != "+":
            result += s

    if len(result) == 7:
        result = "8495" + result
    elif result[0] == "7":
        result = "8" + result[1:]

    return result


new_number = unify_number(input())

for _ in range(3):
    number = unify_number(input())
    if number == new_number:
        print("YES")
    else:
        print("NO")
