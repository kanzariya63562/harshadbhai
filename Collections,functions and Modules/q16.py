# Write a Python program to check whether a list contains a sub list.




list = [1,2,3,4,4,5,5,6,7,7,7,8]


size = len(list)



for ele in range(size-2):
    if list[ele] == list[ele+1] and list[ele+1] == list[ele+1] :
        print(line[ele])
