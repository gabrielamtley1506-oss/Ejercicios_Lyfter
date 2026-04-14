#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto


def char_count(text, character):
    count = 0
    for char in text:
        if char == character:
            count += 1
    return count

def main():
    text = input('Enter a text:')
    character = input('Enter a character to count:')
    print(f'The character "{character}" appears {char_count(text, character)} times in the text.')


main()