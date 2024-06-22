# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?.




#  Inheritance is one of the pillar concepts of OOPs. In this article, we will take a look at this robust feature and its various types with examples. But before we dig deeper, we must get familiar with some essential coding concepts like Objects and Classes.








class shapes:
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(no_sides)]
 
    def takeSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
 
    def disSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])






# The __init__ method is crucial in object-oriented programming in Python. It is a special method automatically called when an object is created from a class. This method allows us to initialize an object's attributes and perform any necessary setup or initialization tasks.


 
 


 # In Python, a constructor is a special method called when an object is created. Its purpose is to assign values to the data members within the class when an object is initialized. The name of the constructor method is always __init__.






