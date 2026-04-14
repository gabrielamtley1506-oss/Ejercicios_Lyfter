#Experimente con el concepto de scope:

#Intente accesar a una variable definida dentro de una función desde afuera.

def local_variable():
    number=10
    print(f"This is the number inside this function {number}")

#print(f'This is me trying to have access to a local variable outside of the function {number}')


#Intente accesar a una variable global desde una función y cambiar su valor.

other_variable='This is a global variable'

def another_function():
    print(other_variable)               #We can easily refer to a global variable, but not to a local one outside the function :)

another_function()