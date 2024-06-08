num1 = int(input("Enter the first range :"))
flag = 0
for i in range(2,num1):
    if num1 % i == 0:
        flag = 1
        break
if num1 > 1 and flag == 0:
    print(num1, "is an prime number")
else:
    print(num1, "is not an prime number")


