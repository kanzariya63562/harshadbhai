# Write a Python program to read a random line from a file.





import random

s1 = open ("quotes.txt", "r")


lines = s1.readlines()

print(random.choice(lines))


s1.close()