
#Write python program that swap two number with temp variable and without temp variable.



def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


num1 = 10
num2 = 20
print("Before swapping - num1:", num1, "num2:", num2)
num1, num2 = swap_without_temp(num1, num2)
print("After swapping - num1:", num1, "num2:", num2)
