#Write a Python function to insert a string in the middle of a string.




def insert_string_in_middle(main_string, string_to_insert):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + string_to_insert + main_string[middle_index:]


main_str = input("Enter the main string: ")
str_to_insert = input("Enter the string to insert: ")

result = insert_string_in_middle(main_str, str_to_insert)
print("Result:", result)