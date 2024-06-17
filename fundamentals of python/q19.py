#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.




string1 = input("Enter a string1 :")
string2 = input("Enter a string2 :")


count = string1.count(string2)



print("string2 occurs %d tims" % count)
