#Write a Python program to test whether a passed letter is a vowel or not.



def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False


letter = input("Enter a letter: ")
if is_vowel(letter):
    print(letter, "is a vowel.")
else:
    print(letter, "is not a vowel.")