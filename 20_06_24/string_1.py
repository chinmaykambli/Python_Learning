# Write a  Python function to reverse a string if its length is a multiple of 4.
def reverse_fun(string1):
    size = len(string1)
    if size % 4 == 0:
        return string1[::-1]
    return string1


print(reverse_fun("hell"))
print(reverse_fun("hello"))
