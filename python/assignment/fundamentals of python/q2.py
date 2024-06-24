# Write a Python program to get the Factorial number of given number.

number = int(input("Enter a number: "))
fact=1

a=1

while a<=number :
    fact=fact*a
    a=a+1

    print("The factorial of" ,number,"is",fact)