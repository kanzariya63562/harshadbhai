# Write a Python program to read last n lines of a file.






n = int(input("Enter n lines :"))
f = open("myfile5.txt","r")
for line in (f.readlines() [-n:]):
    print(line,end="") 
    f.close()