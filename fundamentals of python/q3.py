#Write a Python program to get the Fibonacci series of given range.
num = int(input("Enter any number :"))

n1,n2 = 0,1
sum=0
if num<=0:
    print("Please enter number greater then 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        n1=sum
        sum=n1+n2