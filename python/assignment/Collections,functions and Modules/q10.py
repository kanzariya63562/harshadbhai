# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.



ist = []


for i in range(1,30):
    ist.append(i*i)

    print(ist)
    print("first five element :" ,ist[0:5])
    print("last five element :" , ist[-5:])