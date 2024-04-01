#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.



def sum_three_unique_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_three_unique_numbers(num1, num2, num3)
print("The sum of the three numbers is:", result)