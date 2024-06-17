 #Write a Python function to reverses a string if its length is a multiple of 4.





def string(data):
   if len(data) % 4 == 0:
      return data[::-1]
      return data




text =    input("Enter string :")
result  = string(text)
print("string is :",result)
