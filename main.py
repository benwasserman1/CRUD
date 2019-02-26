# Ben Wasserman
# 02/25/19
# Database Management
# 2280906

import sqlite3
import Student
import sys

conn = sqlite3.connect('StudentDB')
c = conn.cursor()

main_menu = True

print("------ Welcome to a CRUD application -------")
print("Enter 'q' at anytime to quit the application\n")

while main_menu:

    print("------ Main Menu --------")

    initial_menu = input("1. Search for records\n"
                         "2. Create new records\n"
                         "3. Update records\n"
                         "4. Delete records\n")

    if initial_menu != "q":
        while int(initial_menu) < 1 or int(initial_menu) > 4:
            print("Improper input. Enter a number between 1 and 4")
            initial_menu = input("1. Search for records\n"
                                 "2. Create new records\n"
                                 "3. Update records\n"
                                 "4. Delete records\n")

    if initial_menu == "1":

        print("\nHow would you like to search? \n")

        search_by_menu = input("1. Search all records\n"
                               "2. Search by major\n"
                               "3. Search by GPA\n"
                               "4. Search by advisor\n")

        if search_by_menu != "q":
            while int(search_by_menu) < 1 or int(search_by_menu) > 4:
                print("Improper input. Enter a number between 1 and 4")
                search_by_menu = input("1. Search all records\n"
                                       "2. Search by major\n"
                                       "3. Search by GPA\n"
                                       "4. Search by advisor\n")

        if search_by_menu == "1":

            # display all students and their attributes
            c.execute('SELECT * FROM Students')
            print(c.fetchall())

        elif search_by_menu == "2":

            # Search by major, GPA, and advisor
            major = input("Major: ")
            major_tuple = (major,)
            c.execute('SELECT * FROM Students WHERE Major = ?', major_tuple)
            print(c.fetchall())

        elif search_by_menu == "3":

            try:
                GPA = int(input("GPA: "))
            except ValueError:
                print("The input was invalid. Enter a number")
                GPA = input("GPA: ")

            gpa_tuple = (GPA,)
            gpa_menu = input("Return all students with a major "
                             "\n1. Greater than " + GPA +
                             "\n2. Less than " + GPA +
                             "\n3. Equal to " + GPA + "\n")

            if gpa_menu == "3":
                c.execute('SELECT * FROM Students WHERE GPA = ?', gpa_tuple)
                print(c.fetchall())
            elif gpa_menu == "2":
                c.execute('SELECT * FROM Students WHERE GPA < ?', gpa_tuple)
                print(c.fetchall())
            elif gpa_menu == "1":
                c.execute('SELECT * FROM Students WHERE GPA > ?', gpa_tuple)
                print(c.fetchall())
            elif gpa_menu == "q":
                sys.exit()


        elif search_by_menu == "4":
            advisor = input("Advisor: ")
            advisor_tuple = (advisor,)
            c.execute('SELECT * FROM Students WHERE FacultyAdvisor = ?', advisor_tuple)
            print(c.fetchall())

        elif search_by_menu == "5":
            print("Return to main menu")

        elif search_by_menu == "q":
            sys.exit()


    elif initial_menu == "2":

        # create new students
        first_name = input("First name: ")
        last_name = input("Last name: ")
        gpa = input("GPA: ")
        major = input("Major: ")
        faculty_advisor = input("Faculty Advisor: ")

        new_student = Student.Student(first_name, last_name, gpa, major, faculty_advisor)
        c.execute('INSERT INTO Students(FirstName, LastName, GPA, Major, FacultyAdvisor) VALUES(?, ?, ?, ?, ?)', new_student.get_student_tuple())

        conn.commit()

    elif initial_menu == "3":

        # update students
        student_id = input("Enter the ID of the student to change: ")
        new_major = input("Major: ")
        new_advisor = input("Advisor: ")

        update_tuple = (new_major, new_advisor, student_id)
        c.execute('UPDATE Students SET Major = ?, FacultyAdvisor = ? WHERE StudentId = ?', update_tuple)
        conn.commit()

    elif initial_menu == "4":

        # delete students by student ID
        delete_id = input("Enter the ID of the student you would like to delete: ")
        delete_tuple = (delete_id,)
        c.execute('DELETE FROM Students WHERE StudentId = ?', delete_tuple)
        conn.commit()

    elif initial_menu == "q":
        sys.exit()

conn.close()


