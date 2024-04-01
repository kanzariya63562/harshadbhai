# Write a Python program to get the Factorial number of given number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial of", number, "is", result)