# Ben Wasserman
# 02/25/19
# Database Management
# 2280906


class Menu:

    def __init__(self):
        print("------ Welcome to a CRUD application -------")
        print("Enter 'q' from any menu to quit the application\n")

    def main_menu(self):
        choice = -1
        try:
            while int(choice) < 1 or int(choice) > 4:
                print("------ Main Menu --------")

                choice = input("1. Search for records\n"
                               "2. Create new records\n"
                               "3. Update records\n"
                               "4. Delete records\n")

                if choice == "q":
                    return choice

        except ValueError:
            self.main_menu()
        return choice

    def search_by_menu(self):
        search = -1
        try:
            while int(search) < 1 or int(search) > 4:
                print("------ Search Menu --------")

                search= input("1. Search all records\n"
                                    "2. Search by major\n"
                                    "3. Search by GPA\n"
                                    "4. Search by advisor\n")
                if search == "q":
                    return search

        except ValueError:
            self.search_by_menu()

        return search

    def gpa_menu(self, GPA):
        print("------ GPA Menu --------")

        gpa_menu = input("Return all students with a major "
                         "\n1. Greater than " + GPA +
                         "\n2. Less than " + GPA +
                         "\n3. Equal to " + GPA + "\n")

        return gpa_menu

    def student_menu(self):
        # create new students
        first_name = input("First name: ")
        last_name = input("Last name: ")
        gpa = input("GPA: ")
        major = input("Major: ")
        faculty_advisor = input("Faculty Advisor: ")

        return first_name, last_name, gpa, major, faculty_advisor

