str1 = [10, 20, 30, 40]
print(f"Before Interchange :", str1)
size = len(str1)
temp = str1[0]
str1[0] = str1[size - 1]
str1[size - 1] = temp
print(f"After Interchanged :", str1)


