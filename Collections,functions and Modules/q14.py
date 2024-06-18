# Write a Python program to find the second smallest number in a list.




nums = [1,2,3,4,5,6,7,5,4,3,2,2,1]

sm= float('inf')
ssm = float('inf')



for num in nums:
    if num <= sm:
        sm,ssm = num,sm
    elif num < ssm:
        ssm = num

print(ssm)

print(sm)

