# Cree una funcion que retorne la suma de los numeros de una lista.. 


def sum_digits_list(numbered_list):
    results=sum(numbered_list)
    print(f'The sum of the digits in the list is {results}')


def main():
    numbered_list=[4,6,2,29]  
    sum_digits_list(numbered_list)  


main()