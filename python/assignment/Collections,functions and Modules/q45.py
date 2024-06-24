# Write a Python program to find the highest 3 values in a dictionary.


from heapq import nlargest


dict = {'a':500, 'b':5874, 'c':560 ,'d':400, 'e':5874, 'f':200}


three_largest = nlargest(3, dict, key=dict.get)


print(three_largest)


