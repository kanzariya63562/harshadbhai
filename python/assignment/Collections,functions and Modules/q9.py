# Write a Python function that takes two lists and returns true if they have at least one common member.





def member(a1, b2):
    for item in a1:

        if item in b2:
            return True
    return False

# Example usage
a1 = [1, 2, 3, 4]
b2 = [5, 6, 7, 4]

result = member(a1, b2)
print(f"Do the lists have at least one common member? {result}")

