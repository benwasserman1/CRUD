# Ben Wasserman
# 02/25/19
# Database Management
# 2280906

import sqlite3
import Student
import sys
import Menu
import SQL

conn = sqlite3.connect('StudentDB')
c = conn.cursor()

main_menu = True

# create instances for the menu and sql work
sql_handler = SQL.SQL(conn, c)
menu_handler = Menu.Menu()

while main_menu:

    choice = menu_handler.main_menu()

    if choice == "1":

        search = menu_handler.search_by_menu()

        if search == "1":

            # display all students and their attributes
            sql_handler.execute_full_statement('SELECT * FROM Students')

        elif search == "2":

            # Search by major, GPA, and advisor
            major = input("Major: ")
            major_tuple = (major,)
            sql_handler.execute_statement('SELECT * FROM Students WHERE Major = ?', major_tuple)

        elif search == "3":
            try:
                GPA = float(input("GPA: "))
            except ValueError:
                print("The input was invalid. Enter a number")
                GPA = input("GPA: ")

            gpa_selection = menu_handler.gpa_menu(GPA)

            gpa_tuple = (GPA,)

            if gpa_selection == "3":
                sql_handler.execute_statement('SELECT * FROM Students WHERE GPA = ?', gpa_tuple)
            elif gpa_selection == "2":
                sql_handler.execute_statement('SELECT * FROM Students WHERE GPA < ?', gpa_tuple)
            elif gpa_selection == "1":
                sql_handler.execute_statement('SELECT * FROM Students WHERE GPA > ?', gpa_tuple)
            elif gpa_selection == "q":
                sys.exit()

        elif search == "4":
            advisor = input("Advisor: ")
            advisor_tuple = (advisor,)
            sql_handler.execute_statement('SELECT * FROM Students WHERE FacultyAdvisor = ?', advisor_tuple)

        elif search == "q":
            sys.exit()

    elif choice == "2":

        sample_tuple = menu_handler.student_menu()
        new_student = Student.Student(sample_tuple[0], sample_tuple[1], sample_tuple[2], sample_tuple[3], sample_tuple[4])

        #new_student = Student.Student(first_name, last_name, gpa, major, faculty_advisor)
        c.execute('INSERT INTO Students(FirstName, LastName, GPA, Major, FacultyAdvisor) VALUES(?, ?, ?, ?, ?)', new_student.get_student_tuple())

        conn.commit()

    elif choice == "3":

        # update students
        student_id = input("Enter the ID of the student you would like to change: ")
        new_major = input("Major: ")
        new_advisor = input("Advisor: ")

        update_tuple = (new_major, new_advisor, student_id)
        c.execute('UPDATE Students SET Major = ?, FacultyAdvisor = ? WHERE StudentId = ?', update_tuple)
        conn.commit()

    elif choice == "4":

        # delete students by student ID
        delete_id = input("Enter the ID of the student you would like to delete: ")
        delete_tuple = (delete_id,)
        c.execute('DELETE FROM Students WHERE StudentId = ?', delete_tuple)
        conn.commit()

    elif choice == "q":
        sys.exit()

conn.close()


