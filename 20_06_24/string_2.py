# Write a  Python function to reverse a string if its length is a multiple of 4.
def reverse_fun(string1):
    size = len(string1)
    if size % 4 == 0:
        reversed_string1 = ""
        for i in range(size - 1, -1, -1):
            reversed_string1 = reversed_string1 + string1[i]
        return reversed_string1
    return string1


print(reverse_fun("hell"))
print(reverse_fun("hello"))
