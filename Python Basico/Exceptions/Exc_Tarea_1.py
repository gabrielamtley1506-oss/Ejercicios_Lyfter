# create a calculator with a menu with all the operations, include exceptions.

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("You can not divide for zero (0)")
    return a / b

def show_menu():
    print('\n___Menu of Operations___')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Erase Results')
    print('6. Exit')

def operation(num, option, other_num):
    if option == '1':
        return addition(num, other_num)
    elif option == '2':
        return subtraction(num, other_num)
    elif option == '3':
        return multiplication(num, other_num)
    elif option == '4':
        return division(num, other_num)

def main():
    num = int(input("Write your first number: "))
    
    while True:
        show_menu()
        option = input('\n Select an option: ')
        
        if option == '5':
            num = 0
            print("The result was erased")
            continue
        
        if option == '6':
            print("Exiting the Calculator...")
            break
        
        if option not in ['1', '2', '3', '4']:
            print("Invalid Option")
            continue
        
        try:
            other_num = int(input("Write the other number: "))
            num = operation(num, option, other_num)
            print(f"The result is: {num}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


