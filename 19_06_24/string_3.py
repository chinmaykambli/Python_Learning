# Function to get a string made of the first three characters of a specified string. If the length of
# the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt

def specified_string(string1):
    size = len(string1)
    if size >= 3:
        string2 = string1[0:3]
        return string2
    else:
        return string1


print(specified_string("Python"))
