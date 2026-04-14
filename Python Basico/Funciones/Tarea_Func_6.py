#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def organize_from_a_to_z(text):
    words=text.split("-")
    words.sort()
    return "-".join(words)

def main():
    words_to_organize = 'python-variable-funcion-computadora-monitor'
    print(organize_from_a_to_z(words_to_organize))

main()
