# Write a Python program to copy the contents of a file to another file.





s1 = open("readdata12.txt", 'r')



s2 = open("writedata12.txt" , 'w')



# print(s1.readlines())


for line in s1:


    s2.write(line)


s1.close()
s2.close()











