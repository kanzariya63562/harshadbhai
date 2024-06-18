# Write a Python program to remove an empty tuple(s) from a list of tuples.




list = [(), (), ("",), ('a','b'), ('a', 'b', 'c'), ('d')]

list = {tuple for tuple in list if tuple}


print(list)