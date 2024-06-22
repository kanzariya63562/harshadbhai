# Write a Python program to count the frequency of words in a file.








file = open("myfile9.txt", "r")


data=file.readlines()

print(data)

lc=1

tw=object
for line in data:
    word=line.split()

    print("No. of word in", lc,"line:", len(word))

    
    tw=tw+len(word)
    
    
    
    print("Total number of words in file", tw)
