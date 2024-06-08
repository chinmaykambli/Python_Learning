# find count occurrence of number
list1 = [10, 20, 30, 40, 30, 30, 10, 20]
print(f"List : ", list1)
num = int(input("Enter the Number : "))
count = 0
for i in list1:
    if num == i:
        count = count + 1
print(f"Count of {num} is {count}")
