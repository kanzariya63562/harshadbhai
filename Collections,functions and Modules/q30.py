# Write a Python program to convert a list of tuples into a dictionary.





list = [("x",1), ("x",2), ("x",3), ("x",1), ("y",1),("y",2), ("z",1)]



d = {}



for a, b  in  list:



    d.setdefault(a, []).append(b)





    print(d)

