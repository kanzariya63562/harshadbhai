#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.



def add_ing_ly(string):
    if len(string) < 3:
        return string
    elif string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing'


user_input = input("Enter a string: ")
result = add_ing_ly(user_input)
print("Result:", result)