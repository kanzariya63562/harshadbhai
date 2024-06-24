#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.





first = input("Enter first string : ")
second = input("Enter second string : ")



output_string = second[:2] + first[:2] + " " + first[:2] + second[:2]


print(f"output string is : {output_string}")