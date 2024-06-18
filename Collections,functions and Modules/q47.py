# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. Sample string: 'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}.





from collections import Counter

def count_letters(string):
    
    counts = Counter(string)
    return dict(counts)


string = 'w3resource'


result = count_letters(string)

print("Result:", result)