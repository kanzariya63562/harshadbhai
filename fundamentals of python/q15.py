#Write a Python program to count occurrences of a substring in a string.




string = input("Enter a string :")
substring = input("Enter a substring :")

count = string.count(substring)

print("Substring occurs %d time " % count)