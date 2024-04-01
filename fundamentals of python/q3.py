#Write a Python program to get the Fibonacci series of given range.
def fibonacci(n):
    fibonacci_series = [0, 1]  # Initialize Fibonacci series with first two numbers
    while fibonacci_series[-1] + fibonacci_series[-2] <= n:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series


range_limit = int(input("Enter the range limit: "))
fib_series = fibonacci(range_limit)
print("Fibonacci series up to", range_limit, "is:", fib_series)