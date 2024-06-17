#Write a Python program to count the number of characters (character frequency) in a string



my_string = input("Enter a String : ")
count = {}

for i in my_string:
    if i in count:
        count[letter] += 1
    else:
     count[i] = 1


print("Conut Frequency is ...")
for key, value in count.items():
    print(f"{key} occurs {value} times")