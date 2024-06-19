# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words
# in sorted form (alphanumerically).
string1 = input("Enter the strings: ")
words = [word for word in string1.split(",")]
print(",".join(sorted(list(set(words)))))
