# Write a Python function that checks whether a passed string is palindrome or not.




s1 = input("Enter String : ")


s2=s1[-1::-1]

if(s1==s2):
    print("Palindrome")

else:
     print("Not Palindrome")