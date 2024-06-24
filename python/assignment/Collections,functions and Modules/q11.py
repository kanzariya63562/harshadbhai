# Write a Python function that takes a list and returns a new list with unique elements of the first list.






def hello(i_list):
    seen = set()
    u_list = []
    for item in i_list:
        if item not in seen:
            seen.add(item)
            u_list.append(item)
    return u_list

# Example usage
o_list = [1, 2, 2, 3, 4, 4, 5, 6, 1]
u_list =hello(o_list)
print(f"Olist: {o_list}")
print(f"List with unique elements: {u_list}")
