#Write a Python program to count the occurrences of each word in a given sentence




text = input("Enter a string :")
char = input("Enter a character : ")
count = 0


for i in text:
    if char  == i:
        count = count + 1


        print("The number of occurrnces of character in a string is : ", count)