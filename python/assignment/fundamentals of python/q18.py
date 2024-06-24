#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.




# def adding(my_string):
#     return my_string + "ing"








# text = input("Entert a string : ")
# new_string = adding(text)





# print("new string is :", new_string)








s = "st"
if len(s) > 2:
    if s.endswith("ing"):
    
     s += "ly"
    else:
        s += "ing"




print(s)
    