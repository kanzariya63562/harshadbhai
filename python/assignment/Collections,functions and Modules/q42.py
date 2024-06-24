# Write a Python program to print all unique values in a dictionary.



l = [{"v":"s001"}, {"v":"s002"},{"v":"s009"},{"v":"s007"}]


print("original list ",l)

u_value = set(val for dic in l for val in dic.values())


print("Unique values: ",u_value)