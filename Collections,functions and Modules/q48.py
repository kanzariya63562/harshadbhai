# Write a Python function to calculate the factorial of a number (a nonnegative integer).




def factorial(number):
    product = 1


    while number > 1:

        product = product * number
        number = number - 1
        return product





num = int(input("Enter The Number : "))


if num < 0:
    print("Number is Invalid, Factorial is not Possible ")


else:

        print("Factorial of Number is ", factorial(num))