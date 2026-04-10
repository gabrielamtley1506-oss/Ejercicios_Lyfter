# Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

my_list=[]

count=int(input('Cuantos numeros vas a ingresar: '))

for index in range(count):

    num=int(input('Ingrese el numero: '))
    my_list.append(num)

find=int(input('Ingrese el numero a buscar: '))


print(f'El numero {find} se repite {my_list.count(find)} veces')

