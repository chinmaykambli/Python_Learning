list1 = [1, 2, 2, 3, 15, 1, 3]
size = len(list1)
list2 = []
new_list = []
product = 1
for i in range(size - 1):
    if list1[i] != list1[i + 1]:
        list2.append(list1[i])
list2.append(list1[-1])
new_list = set(list2)
print(new_list)
for j in new_list:
    product = product * j
print(product)

