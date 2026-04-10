# Este programa es un juego de adivinanza de números.

import random
secret_number = random.randint(1, 10 )

number= int( input("Adivina un número entre 1 y 10: ") )
while number != secret_number:
    print("Número incorrecto. Intenta de nuevo.")
    number= int( input("Adivina un número entre 1 y 10: ") )
print("¡Felicidades! Adivinaste el número secreto.")

