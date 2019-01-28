fin = open("input.txt")

customers = dict()

for line in fin:
    name, product, number = line.split()

    if name not in customers:
        customers[name] = dict()

    customers[name][product] = customers[name].get(product, 0) + int(number)

for customer in sorted(customers):
    print(customer + ":")
    for product in sorted(customers[customer]):
        print(product, customers[customer][product])
