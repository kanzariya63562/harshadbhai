# Write a Python program to get unique values from a list.





list = [1,4,5,3,2,3,4,5,4]


unique_list=[]

for a in list:
    if a not in unique_list:
        unique_list.append(a)
        

        print(unique_list)