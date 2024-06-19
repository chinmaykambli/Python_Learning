# Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def addition(string1):
    sub_string = string1[-2:]
    return sub_string * 4


print(addition("Python"))
