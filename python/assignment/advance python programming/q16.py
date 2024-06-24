# Can one block of except statements handle multiple exception?.





try:
    
    s1 = int(input("Enter number :"))
    s2 = int(input("Enter number :"))
    s3 = s1/s2
    print("division",s3)
except Zerodivisionerror:
    print("Zero not allowed ")
except Valueerror:
    print("Only integer value") 
    print("Outside try.. except ")  