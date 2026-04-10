# Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = ['access_level', 'age']  
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for index in list_of_keys:
    deleted_item = employee.pop(index)

print(employee)