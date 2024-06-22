# What relationship is appropriate for Student and Person?.






# A student-person relationship in the classroom is a positive relationship between the teacher and the student in efforts to gain trust and respect from each other. This relationship may consist of getting to know your students better, providing choice and encouraging the students to become stronger learners everyday. By doing this teachers are showing respect to their students, valuing their individuality and being polite. Having a positive relationship with your students helps them become more successful in the classroom as well as makes your classroom a safe and welcoming environment for all.




class Person:
    def __init__(self, name, address, dob):
        self.name = name
        self.address = address
        self.dob = dob

class Student(Person):
    def __init__(self, name, address, dob, student_id, major, gpa):
        super().__init__(name, address, dob)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa



# PersonID | Name   | Address  | DOB       | StudentID | Major    | GPA
# ---------+--------+----------+-----------+-----------+----------+------
# 1        | s1   | 123 St   | 2000-01-01| 123456    | CS       | 3.5
# 2        | s2   | 456 Ave  | 1999-02-02| 789012    | Math     | 3.8
# 3        | s3 | 789 Blvd | 1980-03-03| NULL  




# StudentID | PersonID | Major | GPA
# ----------+----------+-------+------
# 123456    | 1        | CS    | 3.5
# 789012    | 2        | Math  | 3.8


