def int_convert(list):
    print("\n ___Results___")
    for item in list:
        try:
            number = int(item)
            print(f'"{item}" converted to {number}')
        except ValueError:
            print(f"Could not convert element: {item}")


def main():
    my_list = ["4", "hola", "10", "5.2"]
    int_convert(my_list)


if __name__ == "__main__":
    main()