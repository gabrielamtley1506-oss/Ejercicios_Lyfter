
from actions import average
import csv
students = []

def save_csv(students_list, file_name="students.csv"):
    with open(file_name, "w", newline="", encoding="utf-8") as archive:
        fields = ["Full Name", "Section", "Spanish Grade", "English Grade", "Social Grade", "Science Grade", "Average"]
        writer = csv.DictWriter(archive, fieldnames=fields)
        
        writer.writeheader()
        
        for student in students_list:
            student["Average"] = average(student)
            writer.writerow(student)


def open_file(students_file):
    """Import students from a CSV file"""
    try:
        imported_students = []
        with open(students_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert grades to integers (they come as strings from CSV)
                row["Spanish Grade"] = int(row["Spanish Grade"])
                row["English Grade"] = int(row["English Grade"])
                row["Social Grade"] = int(row["Social Grade"])
                row["Science Grade"] = int(row["Science Grade"])
                
                # Remove Average if it exists (we'll recalculate it)
                row.pop("Average", None)
                
                imported_students.append(row)
        
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
   