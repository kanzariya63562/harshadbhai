# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.




class rectangle:


    def __init__(self):
        self.length = float(input("Enter rectanglr length :"))
        self.width = float(input("Enter rectangle  width :"))


   
    def compute_area(self):
       area = self.length * self.width
       print("Are of rectangle is : %.2f" %area)




rectangle_obj = rectangle()
rectangle_obj.compute_area()