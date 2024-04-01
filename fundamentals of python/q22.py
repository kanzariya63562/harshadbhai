#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

inputString = ".kjvchjbh"
 

newString = "{}{}".format(inputString[0:2], inputString[-2:])
 

print("Input string = " + inputString)
print("New String = " + newString)