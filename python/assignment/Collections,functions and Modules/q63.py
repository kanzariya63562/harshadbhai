# Write a Python program to returns sum of all divisors of a number.





def totaldiv(no):
    div=[l]
    for i in range(2,no):
        if(no % i)==0:
            div.append(i)
            return sum(div)
            print("Sum of all divisors 14 is :", totaldiv(14))
            print("Sum of all divisors 18 is :", totaldiv(18))
            print("Sum of all divisors 24 is:", totaldiv(24))
            print("Sum of all divisors 34 is :", totaldiv(34))