list_1 = [1, 5, 8, 4, 10, 6, 2, 3, 9, 51]
list_2 = []
for i in list_1:
    if i%2 == 0:
        list_2.append(i)

print("list_1 = {}\nlist_2 = {}".format(list_1, list_2))

sum_1 = sum(list_2)
print(sum_1)

list_1.reverse()
print(list_1)
