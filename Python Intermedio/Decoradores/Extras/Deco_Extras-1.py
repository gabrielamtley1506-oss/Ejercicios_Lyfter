class Person:
    def __init__(self, name):
        self.name = name
        pass


    def repeat_twice(func):
        def wrapper(person):
            print(f"Hola {person.name}")
            print(f"Hola {person.name}")
            func(person)
        return wrapper


    @repeat_twice
    def greetings(self):
        print("I hope you are enjoying your day")

person1=Person("Gaby")
person1.greetings()