#program to get a string from a given string where all occurrences of its first char have been changed
# to '$', except the first char itself.
str1 = "RonaRdR"
first_char = str1[0]
result = first_char
for char in str1[1:]:
    if char == first_char:
        result = result + "$"
    else:
        result = result + char
print(result)

