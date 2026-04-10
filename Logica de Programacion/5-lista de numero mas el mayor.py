# este programa le pide al usuario que ingrese 10 numeros y le muiestra la lista de numero seguidop del mayor que ingreso

list=[]
mayor=0
for index in range(0,10):
    numero=int(input('Escriba un numero: '))
    list.append(numero)
    if list[index]>=mayor:
        mayor=list[index]
print(f'La lista de numeros es:{list}. El mayor es: {mayor}')
