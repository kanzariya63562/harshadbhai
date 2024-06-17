#Write a Python function that takes a list of words and returns the length of the longest one.




def length(my_list):
    counter = 0
    for item in my_list:
        if len(item) >= counter:
            counter = len(item)
            return counter



list = ["hello","word","a","longest","min"]
print("Longest  word count is %d "  %length(list))