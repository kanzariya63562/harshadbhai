# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd.




d = {"a":["a","b","c"],"b":["c","d","e"]}

l = list(d.values())



for comb in l[1:]:
    for i in l[0]:
        for j in comb:
          print(i+j) 

