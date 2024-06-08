# Find second large number from list.

list1 = [10, 50, 5, 400, 1000, 900,10000]
large = 0
sl = 0
for num in list1:
    if num > large:
        sl = large
        large = num

    elif num > sl and num < large:
        sl = num

print(f"large Number : ",large)
print(f"Second Large :",sl)

