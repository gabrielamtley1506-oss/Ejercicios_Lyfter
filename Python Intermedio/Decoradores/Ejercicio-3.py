from datetime import date

def only_legal(func):
    def wrapper(*args, **kwargs):

        user = None
        for arg in args:
            if isinstance(arg, User):
                user = arg
                break

        if user is None:
            for val in kwargs.values():
                if isinstance(val, User):
                    user = val
                    break

        if user is None:
            raise TypeError("only_legal: no User instance found in arguments")

        if user.age < 18:
            raise ValueError(f"Permission denied: user is {user.age} years old (must be 18+)")

        return func(*args, **kwargs)
    return wrapper


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )

    @only_legal
    def enter_site(self, section="home"):
        print(f"Welcome {self.name}! Section: {section}")

    @only_legal
    def buy_alcohol(self):
        print(f"{self.name} can purchase alcohol.")


@only_legal
def send_email(subject, user):
    print(f"Email sent to {user.name}: {subject}")



adult = User("Carlos", date(2001, 6, 15))
minor = User("Sofia",  date(2015, 6, 15))

adult.enter_site(section="movies")   
adult.buy_alcohol()                   
send_email("Newsletter", user=adult)  

try:
    minor.enter_site()
except ValueError as e:
    print(e)