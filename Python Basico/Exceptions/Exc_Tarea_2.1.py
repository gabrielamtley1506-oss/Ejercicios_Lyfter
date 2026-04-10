# Ask for a person's name and age, find the exceptions. 


def digit_name(name):
    if name.isdigit():
        raise ValueError ("The name cannot have digits")



def age_value(age):
    try:
        age=int(age)
        if age < 1 or age > 99:
            raise ValueError ("Number no Valid")
    except ValueError:
        raise ValueError("Age must be a number between 1 and 99")


def Personal_info():
    while True:
        try:
            name=input("What's your name: ")
            digit_name(name)
            age=input("What's your age: ")
            age_value(age)
            return f"Your name is {name} and you are {age} years old"
        except ValueError as e:
            print(f"Error: {e}")
    

def main():
    print(Personal_info())
    


if __name__ == "__main__":
    main()



