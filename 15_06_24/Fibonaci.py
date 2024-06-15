num = int(input("Enter the number :"))
a = 0
b = 1
result = 0
for i in range(0,num+1):
    print(f"Fibonacci series : ", result)
    result = a + b
    a = b
    b = result
