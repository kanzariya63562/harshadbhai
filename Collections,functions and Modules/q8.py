# Write a Python program to check a list is empty or not.





def list_empty(input_list):
    if not input_list:
        return True
    else:
        return False


list1 = []
list2 = [1, 2, 3]

print(f"Is list1 empty? {list_empty(list1)}")  
print(f"Is list2 empty? {list_empty(list2)}") 