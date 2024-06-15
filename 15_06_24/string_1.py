#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
string1 = str(input("Enter a string :"))
dict1 = {}
for char in string1:
    if char not in dict1:
        dict1[char] = 1
    else:
        dict1[char] += 1
print("Frequencies")
for char,freqn in dict1.items():
    print(f"{char}:{freqn}")

