# Dada n cantidad de notas del usuario calcular;
# Cuantas notas tiene aprobadas mas de 70
# Cuantas notas tiene desaprobadas menor a 70
# El promedio de todas
# EL promedio de las aprobadsas
# El promedio de las desaprobadas

total_of_grades = int(input("Ingrese la cantidad de notas: "))
count_of_grades=1 
grade=0
passed_grades=0
average_passed_grades=0
failed_grades=0
average_failed_grades=0
average_grades=0
while count_of_grades <= total_of_grades :
    grade=float(input(f"Ingrese la nota {count_of_grades}: "))
    count_of_grades += 1
    if grade >= 70:
        passed_grades += 1
        average_passed_grades += grade
    else:
        failed_grades += 1
        average_failed_grades += grade

    average_grades += grade
average_grades = average_grades / total_of_grades

print(f"La cantidad de notas aprobadas es: {passed_grades}")
print(f"La cantidad de notas desaprobadas es: {failed_grades}")
print(f"El promedio de todas las notas es: {average_grades}")

#Este bloque evita la division por cero. 
if passed_grades >0:
    average_passed_grades = average_passed_grades / passed_grades
    print(f"El promedio de las notas aprobadas es: {average_passed_grades}")
else:
    print("No hay notas aprobadas.")
if failed_grades >0:
    average_failed_grades = average_failed_grades / failed_grades
    print(f"El promedio de las notas desaprobadas es: {average_failed_grades}")
else:
    print("Felicidades! No hay notas desaprobadas.")


