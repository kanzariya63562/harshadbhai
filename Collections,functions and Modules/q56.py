# How will you set the starting value in generating random numbers?



from random import randint, seed


seed(123)

for i in range(10):
 print(randint(0,10))


 