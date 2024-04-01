#What are negative indexes and why are they used?





#Negative indexes in Python are used to access elements from the end of a sequence, such as a string, list, or tuple. In Python, indexing starts from 0 for the first element, 1 for the second element, and so on. Negative indexing allows you to access elements from the end of the sequence, starting from -1 for the last element, -2 for the second-to-last element, and so forth.

#Here's a quick example to illustrate negative indexing:

my_list = [10, 20, 30, 40, 50]

print(my_list[0])   
print(my_list[1])   


print(my_list[-1])  
print(my_list[-2])  
#Negative indexes are particularly useful when you want to access elements relative to the end of a sequence without knowing its length or when you want to access elements in reverse order. For example, when iterating over a list in reverse:


my_list = [10, 20, 30, 40, 50]


for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])
#In this example, we're using range(len(my_list) - 1, -1, -1) to iterate over the indices of my_list in reverse order. However, a more concise and Pythonic way to achieve the same result would be to use negative indexing:


my_list = [10, 20, 30, 40, 50]


for i in range(-1, -len(my_list) - 1, -1):
    print(my_list[i])
#Negative indexing simplifies code and makes it more readable when dealing with sequences, especially when working with elements from the end of the sequence.