# Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, 
# genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.



nombre = input("Ingrese el nombre del empleado: ")
apellido = input("Ingrese el apellido del empleado: ")
dominio = input("Ingrese el dominio de la empresa (sin .com): ")
email = f"{nombre.lower()}.{apellido.lower()}@{dominio.lower()}.com"
print(f"El email generado es: {email}")
