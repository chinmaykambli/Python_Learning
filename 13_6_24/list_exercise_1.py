list1 = [10, 10, 10, 10, 1, 2, 5]
size = len(list1)
count = 0
for j in range(0, size - 1):
    if list1[j] != list1[j + 1]:
        count = count + 1
print(count)
