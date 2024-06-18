# Write a Python function to get the largest number, smallest num and sum of all from a list.
def get_largest_smallest_sum(numbers):
    if not numbers:
        return None, None, 0 
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum


my_list = [10, 20, 30, 40, 50]
largest, smallest, total_sum = get_largest_smallest_sum(my_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total_sum)