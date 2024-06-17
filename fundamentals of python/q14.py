#What are negative indexes and why are they used?





#Negative indexes in Python are used to access elements from the end of a sequence, such as a string, list, or tuple. In Python, indexing starts from 0 for the first element, 1 for the second element, and so on. Negative indexing allows you to access elements from the end of the sequence, starting from -1 for the last element, -2 for the second-to-last element, and so forth.

#Here's a quick example to illustrate negative indexing:



list = [0,1,2,3]

list[0]


print(list[0])
print(list[len(list) - 1])

print(my_list[-1])


list = [1, "string", [1,2,3,4]]

string = list[1]
print(string[0])

print(list[1][0])


list[2][0] = 1000

list[0] = "string2"
print(list)