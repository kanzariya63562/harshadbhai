# Write a Python program to read a file line by line store it into a variable.




f = open("myfile7.txt", "r")


lines = f .readlines()


print(lines)




new_lines = [x.strip() for x in lines]


print(new_lines)
