# Write a Python program to read a file line by line and store it into a list.





with open("myfile6.txt") as file:

    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


    print(lines)



