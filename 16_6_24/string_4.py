# Write a Python program to remove characters that have odd index values in a given string.
str1 = input("Enter the string :")
result = ""
for i in range(len(str1)):
    if i % 2 == 0:
        result = result + str1[i]
print(result)