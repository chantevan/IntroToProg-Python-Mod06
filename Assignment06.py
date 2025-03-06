# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chantal Van den bussche, 3/5/2025, Created & edited script
# ------------------------------------------------------------------------------------------ #
import json

# -- Data Storage -- #
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data
# Commented out the below from being global variables and used locally instead
    # student_first_name: str = ''  # Holds the first name of a student entered by the user.
    # student_last_name: str = ''  # Holds the last name of a student entered by the user.
    # course_name: str = ''  # Holds the name of a course entered by the user.
    # student_data: dict = {}  # one row of student data
    # csv_data: str = ''  # Holds combined string data separated by a comma.
    # json_data: str = ''  # Holds combined string data in a json format.
    # file = None  # Holds a reference to an opened file.

# -- Processing -- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Chantal Van den bussche, 3/5/2025, Created Class
    """

    @staticmethod
    def read_data_fromfile(file_name:str, student_data: list):
        """
        A function that reads and imports data from a JSON file \
        into a list of dictionary rows

        :param file_name:
        :param student_data:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created CLass
        """
        # When the program starts, read the file data into a list of lists (table)
        # Extract the data from the file
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message= "ERROR! There was a problem "
                                              "reading your file.", error= e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        A function that writes data to a JSON file using data stored in list \
        of dictionary rows

        :param file_name:
        :param student_data:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created CLass
        """
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data= student_data)
        except Exception as e:
            IO.output_error_messages(message= "ERROR! There was an issue "
                                              "writing data to your file.",
                                     error= e)
        finally:
            if file.closed == False:
                file.close()


# -- Presentation -- #
class IO:
    """
    A collection of presentation layer files that manage user I/O

    ChangeLog: (Who, When, What)
    Chantal Van den bussche, 3/5/2025, Created Class"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        A function that handles error messaging

        :param message:
        :param error:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created Function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        A function that displays menu of choices to the user

        :param menu:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created Function
        """
        print(MENU)

    @staticmethod
    def input_menu_choice():
        """
        A function that takes user input for their menu choice

        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created Function
        """
        choice = "0" # Needs to be string!!
        try:
            choice = input("Enter your menu choice as a number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please enter only 1, 2. 3, or 4.")
        except Exception as e:
            IO.output_error_messages(e.__str__()) # Avoiding technical error message
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        A function that display registered students to their enrolled courses

        :param student_data:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created Function
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        A function that appends user input for student's first name, \
        last name, and course name into a list of dictionary rows

        :param student_data:
        :return:

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/5/2025, Created Function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message= "Student name must contain "
                                              "only alphabetical letters.",
                                     error= e)
        except Exception as e:
            IO.output_error_messages(message= "ERROR! There was an issue with"
                                              " your entered data.", error= e)
        return student_data


# MAIN BODY

# At program start, read and store data into list of lists
students = FileProcessor.read_data_fromfile(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
