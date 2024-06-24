import os

def validate_name(name):
    
    if not name.isalpha() and not name.isspace():
        print("Invalid name. Please enter only alphabets and spaces.")
        return False
    return True

def validate_contact(contact):
   
    if not contact.isdigit():
        print("Invalid contact number. Please enter only digits.")
        return False
    return True

def add_student(students):
    
    while True:
        name = input("Enter student's name: ")
        if validate_name(name):
            break

    while True:
        contact = input("Enter student's contact number: ")
        if validate_contact(contact):
            break

    students[name] = {"contact": contact}
    print(f"Student {name} added successfully!")

def remove_student(students):
   
    student_id = input("Enter student's ID to remove: ")
    if student_id in students:
        confirmation = input(f"Are you sure you want to remove {student_id}? (Y/N): ")
        if confirmation.upper() == 'Y':
            del students[student_id]
            print(f"Student {student_id} removed successfully!")
    else:
        print(f"Student with ID {student_id} does not exist.")

def view_all_students(students):
   
    if not students:
        print("No students found.")
        return

    print("-" * 40)
    print("| {:20s} | {:20s} |".format("Student Name", "Contact Number"))
    print("-" * 40)
    for student, details in students.items():
        print("| {:20s} | {:20s} |".format(student, details["contact"]))
    print("-" * 40)

def view_student_by_id(students):
    
    student_id = input("Enter student's ID to view: ")
    if student_id in students:
        print(f"Student Name: {student_id}")
        print(f"Contact Number: {students[student_id]['contact']}")
    else:
        print(f"Student with ID {student_id} does not exist.")

def faculty_menu(faculty_name, students):
   
    print(f"\nWelcome, {faculty_name}!")
    print("\nFaculty Menu:")
    print("1. View Assigned Students")
    print("2. Add Student Marks (Not implemented in this version)")
    print("3. Exit")

def main():
    """Manages the overall program flow, including menus, user interactions, and file operations."""
    students = {} 
    faculty_data = {}  
    log_file = None


    while True:
        print("\nStudent Management System")
        print("1. Counsellor Menu")
        print("2. Faculty Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nCounsellor Menu:")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View All Students")
            print("4. View Student by ID")
            print("5. Exit")

            counsellor_choice = input("Enter your choice: ")

            if counsellor_choice == '1':
                add_student(students)
               
            elif counsellor_choice == '2':
            
            
            
                  print("hello")