
from actions import average, Student
import csv
students = []

def save_csv(students_list, file_name="students.csv"):
    with open(file_name, "w", newline="", encoding="utf-8") as archive:
        fields = ["Full Name", "Section", "Spanish Grade", "English Grade", "Social Grade", "Science Grade", "Average"]
        writer = csv.DictWriter(archive, fieldnames=fields)
        
        writer.writeheader()
        
        for student in students_list:
            student_data = {
                "Full Name": student.name,
                "Section": student.section,
                "Spanish Grade": student.spanish_grade,
                "English Grade": student.english_grade,
                "Social Grade": student.social_grade,
                "Science Grade": student.science_grade,
                "Average": average(student)
            }
            writer.writerow(student_data)


def open_file(students_file):
    #Import students from a CSV file
    try:
        imported_students = []
        with open(students_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                spanish_grade = int(row["Spanish Grade"])
                english_grade = int(row["English Grade"])
                social_grade = int(row["Social Grade"])
                science_grade = int(row["Science Grade"])
                
                student_exists = any(
                    s.name.lower() == row["Full Name"].lower() and 
                    s.section.lower() == row["Section"].lower() 
                    for s in students
                )
                
                if not student_exists:
                    student = Student(
                        row["Full Name"],
                        row["Section"],
                        spanish_grade,
                        english_grade,
                        social_grade,
                        science_grade
                    )
                    imported_students.append(student)
        
        students.extend(imported_students)
        print(f"\n{len(imported_students)} student(s) imported successfully from '{students_file}'!\n")
        return imported_students
    
    except FileNotFoundError:
        print(f"Error: File '{students_file}' not found.")
        return []
    except ValueError:
        print("Error: Invalid grade format in CSV file. Grades must be numbers.")
        return []
    except Exception as e:
        print(f"Error importing file: {e}")
        return []