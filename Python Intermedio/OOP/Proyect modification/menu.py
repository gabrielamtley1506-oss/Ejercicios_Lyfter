from actions import Student, add_student, students_average, display_all_students, top_3_students, delete_student, failed_students
from data import students, save_csv, open_file

def display_menu():
    print("\n ___Menu___" )
    print("1. Add new Student")
    print("2. Information of all the Students")
    print("3. Top 3 Students")
    print("4. Student grade point average")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Failed Students")
    print("8. Delete a Student")
    print("9. Exit")


def get_options():
    while True:
        try:
            display_menu()
            option = int(input("Write your option from the menu: "))
            
            if option == 1:
                new_student = add_student()
                students.append(new_student)
                print(f"Student {new_student.name} added successfully!")
            elif option == 2:
                display_all_students(students)
            elif option == 3:
                top_3_students(students)
            elif option == 4:
                students_average(students)
            elif option == 5:
                print("Export to CSV")
                save_csv(students)
            elif option == 6:
                file_name = input("Enter the CSV file name to import (ex: students.csv): ")
                imported = open_file(file_name)
                if imported:
                    students.extend(imported)
                    print(f"Total students in the system: {len(students)}")
            elif option == 7:
                failed_students(students)
            elif option == 8:
                delete_student(students)
            elif option == 9:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 9.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

