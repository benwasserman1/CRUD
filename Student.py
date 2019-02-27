# Ben Wasserman
# 02/25/19
# Database Management
# 2280906

# Student class with member variables of first_name,
# last_name, gpa, major, and faculty_advisor. Contains
# a function get_student_tuple() that takes no arguments
# and returns the student as a tuple


class Student:

    def __init__(self):
        self = self

    def __init__(self, first_name, last_name, gpa, major, faculty_advisor):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major
        self.faculty_advisor = faculty_advisor

    def input_student(self):
        # create new students
        first_name = input("First name: ")
        last_name = input("Last name: ")
        gpa = input("GPA: ")
        major = input("Major: ")
        faculty_advisor = input("Faculty Advisor: ")
        return first_name, last_name, gpa, major, faculty_advisor

    def get_student_tuple(self):
        student_tuple = (self.first_name, self.last_name, self.gpa, self.major, self.faculty_advisor)
        return student_tuple
