#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.


def es_primo(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def prime_numbers(numbers):
    prime = []
    for num in numbers:
        if es_primo(num):
            prime.append(num)
    return prime


def main():
    numbers = [1, 2, 4, 6, 7, 13, 9, 67, 29]
    print(f'This is the list of prime numbers {prime_numbers(numbers)}')

main()
