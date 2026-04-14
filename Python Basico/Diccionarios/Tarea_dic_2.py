#Crear un diccionario a partir de dos listas


list_a = ['first_name', 'last_name', 'role']
list_b = ['Gabriela', 'Amat', 'Software Engineer']

person = {}

for index in range(len(list_a)):
    person[list_a[index]]=list_b[index]

print(person)