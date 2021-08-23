data = open("CupcakeInvoices.csv")

# for line in data:
#     print(line)


# for line in data:
#     for type in line:
#         list = line.split(',')
#     print(list[2])

total_list = []

for line in data:
    for type in line:
        list = line.split(',')
    qnt = float(list[3])
    price = float(list[4])
    total = round(qnt * price, 2)
    print(total)
    total_list.append(total)

print(round(sum(total_list), 2))


data.close()