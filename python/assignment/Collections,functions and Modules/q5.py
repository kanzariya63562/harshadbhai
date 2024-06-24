# How will you compare two lists?





list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not equal")




list1 = [1, 2, 3, 4]
list2 = [1, 2, 5, 4]

comparison = [a == b for a, b in zip(list1, list2)]
print(comparison)  