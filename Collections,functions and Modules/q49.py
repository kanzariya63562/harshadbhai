# Write a Python function to check whether a number is in a given range.


s1 = int(input("Enter s1 Range : "))
s2 = int(input("Enter s2 Range : "))



number = int(input("Enter a number : "))


if s1 <= number <= s2:
    print("Number is in the Range")

else:
        print("Number is not with in the Range ")