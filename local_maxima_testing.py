list = [1,2,3,2,3,4,2,3,2]

order = 2

for i in range(order, len(list) - order):

    for x in range(order):

        if not list[i - x] <= list[i] <= list[i + x]:
            print(list[i])