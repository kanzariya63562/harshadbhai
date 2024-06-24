# Write a Python script to sort (ascending and descending) a dictionary by value.






d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Origional dictionary : ',d)
sorted_d = sorted(d.item())
print('Dictionary in ascending order : ',sorted_d)
sorted_d_reverse = sorted(d.items(),reverse=True)
print('Dictionary in descending order : ' ,sorted_d_reverse)