#Write a Python function to insert a string in the middle of a string.







s1 = input("Enter first string :")
s2 = input("Enter second string :")




middle = len(s2)
string = ""


if len(s2) % 2 == 0:
    string = s2[:(middle)] + s1 + s2[-middle:]
  
else:
    string = s2[:(middle+1)] + s1 + s2[-middle:]

    




print("New string is",string)