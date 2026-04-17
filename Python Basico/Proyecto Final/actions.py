

def get_valid_grade(subject):
    """Get and validate a grade input (must be 0-100)"""
    while True:
        try:
            grade = int(input(f"{subject} Grade: "))
            if not (0 <= grade <= 100):
                print("Grade must be between 0 and 100")
                continue
            return grade
        except ValueError:
            print("Grade must be a number")


def is_valid_name():
    while True:
        name = input("Full Name: ").strip()
        
        if not name:
            print("Name cannot be blank. Please enter a valid name.")
            continue
        
        if any(char.isdigit() for char in name):
            print("Name must not contain numbers.")
            continue
        
        return name


def is_valid_section():
    while True:
        section = input("Section: ").strip().upper()
        
        if len(section) != 3:
            print("Please enter a valid section (ex: 11A)")
            continue
        
        if not section[:2].isdigit():
            print("Please enter a valid section (ex: 11A)")
            continue
        
        if not (section[2].isalpha() and section[2].isupper()):
            print("Please enter a valid section (ex: 11A)")
            continue
        
        return section      


def add_student():
    #User types the information of an student
    name = is_valid_name()
    section = is_valid_section()
    spanish_grade = get_valid_grade("Spanish")
    english_grade = get_valid_grade("English")
    social_grade = get_valid_grade("Social")
    science_grade = get_valid_grade("Science")

    student = {
        "Full Name": name,
        "Section": section,
        "Spanish Grade": spanish_grade,
        "English Grade": english_grade,
        "Social Grade": social_grade,
        "Science Grade": science_grade
    }
    return student 


def average(student):
    #Calculate the average of the student
    spanish_grade = student["Spanish Grade"]
    english_grade = student["English Grade"]
    social_grade = student["Social Grade"]
    science_grade = student["Science Grade"]
    
    avg = (spanish_grade + english_grade + social_grade + science_grade) // 4
    return avg     


def display_all_students(students_list): 
    #Display information of all students
    if not students_list:
        print("No students to display.")
        return
    
    print("\n" + "="*70)
    print("ALL STUDENTS INFORMATION")
    print("="*70)
    
    for i, student in enumerate(students_list, 1):
        avg = average(student)
        print(f"\n{i}. Name: {student['Full Name']}")
        print(f"   Section: {student['Section']}")
        print(f"   Spanish Grade: {student['Spanish Grade']}")
        print(f"   English Grade: {student['English Grade']}")
        print(f"   Social Grade: {student['Social Grade']}")
        print(f"   Science Grade: {student['Science Grade']}")
        print(f"   Average: {avg}")
    
    print("\n" + "="*70 + "\n")


def students_average(students_list):
    # Display the average grade 
    if not students_list:
        print("No students to display.")
        return
    
    print("\n" + "="*50)
    print("STUDENT GRADE POINT AVERAGE")
    print("="*50)
    
    total_avg = 0
    for student in students_list:
        avg = average(student)
        total_avg += avg
    
    overall_average = total_avg / len(students_list)
    print("\n" + "-"*50)
    print(f"Overall Average: {overall_average:.2f}")
    print("="*50 + "\n")


def top_3_students(students_list):
    #Display the top 3 students with the best averages
    if not students_list:
        print("No students to display.")
        return
    
    if len(students_list) < 3:
        print(f"\nWarning: Only {len(students_list)} student(s) in the list.\n")
    
    students_with_avg = [(student, average(student)) for student in students_list]
    
    students_with_avg.sort(key=lambda x: x[1], reverse=True)

    top_3 = students_with_avg[:3]
    
    print("\n" + "="*50)
    print("TOP 3 STUDENTS BY AVERAGE")
    print("="*50)
    
    for i, (student, avg) in enumerate(top_3, 1):
        print(f"\n{i}. {student['Full Name']} ({student['Section']})")
        print(f"   Average: {avg}")
    
    print("\n" + "="*50 + "\n")


def delete_student(students_list):
    #Delete a student from the list by name and section
    if not students_list:
        print("No students to delete.")
        return
    
    print("\n" + "="*50) 
    print("STUDENTS LIST")
    print("="*50)
    
    for student in students_list:
        print(f"{student['Full Name']} ({student['Section']})")
    
    name = input("\nEnter the student's full name to delete: ")
    section = input("Enter the student's section: ")
    
    for student in students_list:
        if student['Full Name'].lower() == name.lower() and student['Section'].lower() == section.lower():
            students_list.remove(student)
            print(f"\nStudent '{student['Full Name']}' from section '{student['Section']}' deleted successfully!")
            return
    
    print(f"\nStudent '{name}' from section '{section}' not found.")


def failed_students(students_list):
    #Display students who failed (have a grade < 60 in any subject)
    if not students_list:
        print("No students to display.")
        return
    
    failed = []
    for student in students_list:
        if (student["Spanish Grade"] < 60 or 
            student["English Grade"] < 60 or 
            student["Social Grade"] < 60 or 
            student["Science Grade"] < 60):
            failed.append(student)
    
    if not failed:
        print("\nNo failed students. Congratulations!")
        return
    
    print("\n" + "="*70)
    print("FAILED STUDENTS (with less than 60 in any subject)")
    print("="*70)
    
    for i, student in enumerate(failed, 1):
        avg = average(student)
        print(f"\n{i}. Name: {student['Full Name']} ({student['Section']})")
        print(f"   Spanish Grade: {student['Spanish Grade']}")
        print(f"   English Grade: {student['English Grade']}")
        print(f"   Social Grade: {student['Social Grade']}")
        print(f"   Science Grade: {student['Science Grade']}")
        print(f"   Average: {avg}")
        
        failed_subjects = []
        if student["Spanish Grade"] < 60:
            failed_subjects.append(f"Spanish ({student['Spanish Grade']})")
        if student["English Grade"] < 60:
            failed_subjects.append(f"English ({student['English Grade']})")
        if student["Social Grade"] < 60:
            failed_subjects.append(f"Social ({student['Social Grade']})")
        if student["Science Grade"] < 60:
            failed_subjects.append(f"Science ({student['Science Grade']})")
        
        print(f"   Failed in: {', '.join(failed_subjects)}")
    
    print("\n" + "="*70 + "\n")