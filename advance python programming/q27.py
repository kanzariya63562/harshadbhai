# What is used to check whether an object o is an instance of class A?




class s1:
    pass
class s2:
    pass
class s3(s2):
    pass



obj = s3()



print(isinstance(obj,s1))
print(isinstance,(obj,s2))
print(isinstance(obj,s3))