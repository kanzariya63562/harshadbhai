# Write a python program to find the longest words.





str1 = input("Enter the line:")




max=0



for i in str1.split():
    

    if(len(i)>max and i.isalpha()):
        max=len(i)
        w=i
        print(w)

