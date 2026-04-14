#Cree una función que reciba un string y retorne cuántas vocales contiene


def get_the_vocals(text):
    vocals="aeiouáéíóú"
    results=0
    for char in text.lower():
        if char in vocals:
            results+=1
    return results


def main():
    the_string=str(input("Ingrese su texto: "))
    print(get_the_vocals(the_string))

main()
