#Question:
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
#which contains every number.Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:

list1 = input("Enter the numbers :")
str1 = list1.split(",")
tup = tuple(str1)
print(tup)
print(str1)





