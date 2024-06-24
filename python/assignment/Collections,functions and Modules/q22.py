# Write a Python program to check whether an element exists within a tuple.






def tuple(element, tup):
    if element in tup:
        return True
    else:
         return False

    

tuple1 = (1, 2, 3, 4, 5)
element_to_check = 3

if tuple(element_to_check, tuple1):
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")