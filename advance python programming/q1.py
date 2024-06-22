# What is File function in python? What is keywords to create and write file.


# The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file: "r" - Read - Default value. Opens a file for reading, error if the file does not exist.












file = open("myfile.txt", "w")
file.write("data inside file.")
file.close()


with open("myfile.txt", "w") as file:


    file.write("data inside file.")