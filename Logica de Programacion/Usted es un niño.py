#Este programa va a definir si usted es un niño, un pre adolescente, un adolescente, um adulto joven, un adulto oo un adulto mayor. 
name = input("Ingrese su nombre: ")
last_name = input ("Ingrese su apellido: ")
age = float(input('Ingrese su edad: '))
# Use un float para la edad para incluir edades menores de un año.

if age < 1:
    print(f"{name} {last_name}, usted es un bebe.")
elif age >= 1 and age <= 11:
    print(f"{name} {last_name}, usted es un niño.")
elif age >= 12 and age <= 13:
    print(f"{name} {last_name}, usted es un pre adolescente.")
elif age >= 14 and age <= 17:
    print(f"{name} {last_name}, usted es un adolescente.")
elif age >= 18 and age <= 25:
    print(f"{name} {last_name}, usted es un adulto joven.")
elif age >= 26 and age <= 64:
    print(f"{name} {last_name}, usted es un adulto.")
else:
    print(f"{name} {last_name}, usted es un adulto mayor.")