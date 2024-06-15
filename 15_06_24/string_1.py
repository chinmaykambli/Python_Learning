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

