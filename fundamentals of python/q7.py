#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.


def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


number = int(input("Enter a number: "))
check_even_odd(number)