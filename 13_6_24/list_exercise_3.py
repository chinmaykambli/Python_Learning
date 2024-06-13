list1 = [10, 20, 10, 10, 50, 20, 60, 20, 20]
size = len(list1)
count = 0
list2 = []
for i in range(0, size - 1):
    if list1[i] == list1[i + 1]:
        count = count + 1
        if count >= 1:
            list2.append(list1[i])
print(list2)




