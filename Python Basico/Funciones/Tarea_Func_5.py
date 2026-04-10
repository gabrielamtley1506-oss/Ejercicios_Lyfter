#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.


def count_case(text):
    upper_count=0
    lower_count=0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f'The number of uppercase letters is {upper_count} and the number of lower cases is {lower_count}')
            


count_case('Hello World, this is Gaby counting the cases.')