
def int_convert(list):
    print("\n ___Results___")
    number = 0
    for item in list:
        try:
            number += float(item)
            print(f'"{item}"was added correctly')
        except ValueError:
            print(f"Invalid element: {item}")
    print( f'Total is : {number}')


def main():
    my_list = ['10', 'apple', '5.5', '3', 'n/a']
    int_convert(my_list)


if __name__ == "__main__":
    main()