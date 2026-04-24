class Authenticate:
    def login(self):
        print("Initializing...")

class Buyer:
    def make_order(self, item):
        print(f"Order for: {item}")


class Client(Authenticate, Buyer):
    def profile(self):
        print("Showing the profile in the dashboard.")


new_user = Client()
new_user.profile()
new_user.login()           # Heredado de Autenticable
new_user.make_order("MacBook Pro") # Heredado de Comprador




#another example of multiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating 🍖")


class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming 🏊")


class Flyer:
    def fly(self):
        print(f"{self.name} is flying ✈️")


class Duck(Animal, Swimmer, Flyer):
    """Duck inherits from Animal, Swimmer, and Flyer"""
    def quack(self):
        print(f"{self.name} is quacking 🦆")


print("\n Creating a Duck named Donald...")
duck = Duck("Donald")

print("\nUsing inherited and own methods:")
duck.eat()      # From Animal
duck.swim()     # From Swimmer
duck.fly()      # From Flyer
duck.quack()    # Own method


