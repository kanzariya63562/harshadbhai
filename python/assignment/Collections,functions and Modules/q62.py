# Write a Python program to calculate surface volume and area of a cylinder.




import math


s1 = int(input("Enter the Radius of Top & Bottm of Cylinder: "))
s2 = int(input("Enter the Height of Cylinder: "))



Area = 2*(math.pi*s1**2)+2+math.pi*s1*s2

print("Surface Area of Cy;inder is: ", Area)





