# Write a Python program to change a given string to a new string where the first and last chars exchanged.
str1 = input("Enter a string :")
size = len(str1)
str1 = str1[-1:] + str1[2:-1] + str1[:1]
print(str1)
