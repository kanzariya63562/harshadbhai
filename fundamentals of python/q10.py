#Write a Python program that will return true if the two given integervalues are equal or their sum or difference is 5. 



def check_condition(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = check_condition(num1, num2)
print("Result:", result)