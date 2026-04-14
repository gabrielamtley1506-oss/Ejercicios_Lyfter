#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras


def get_minimum_letters(the_words, minimum_let):
    results = []
    for word in the_words:
        if len(word) > minimum_let:
            results.append(word)
    return results


def main():
    random_words = ["cielo", "sol", "maravilloso", "día"]
    mini_let = int(input("Ingrese el numero de letras minimas en la palabra: "))
    print(get_minimum_letters(random_words, mini_let))
    

main()
