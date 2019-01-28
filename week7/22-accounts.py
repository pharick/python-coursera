def check_client(accounts, name):
    if name not in accounts:
        accounts[name] = 0


fin = open("input.txt")

accounts = dict()

for line in fin:
    line_list = line.split()
    operation = line_list[0]

    if operation == "INCOME":
        p = int(line_list[1])

        for account in accounts:
            if accounts[account] > 0:
                accounts[account] += int(accounts[account] / 100 * p)
    elif operation == "TRANSFER":
        name1 = line_list[1]
        name2 = line_list[2]
        amount = int(line_list[3])

        check_client(accounts, name1)
        check_client(accounts, name2)

        accounts[name1] -= amount
        accounts[name2] += amount
    elif operation == "DEPOSIT":
        name = line_list[1]
        amount = int(line_list[2])

        check_client(accounts, name)

        accounts[name] += amount
    elif operation == "WITHDRAW":
        name = line_list[1]
        amount = int(line_list[2])

        check_client(accounts, name)

        accounts[name] -= amount
    elif operation == "BALANCE":
        name = line_list[1]

        if name not in accounts:
            print("ERROR")
        else:
            print(accounts[name])
