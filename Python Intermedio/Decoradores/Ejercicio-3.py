from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year- self.date_of_birth.year- ((today.month, today.day)< (self.date_of_birth.month, self.date_of_birth.day))
        )

    def only_legal(func):
        def wrapper(user):
            if user.age >= 18:
                return func(user)
            else:
                raise ValueError("Error: Permission denied: age must be 18 or older")
        return wrapper

    @only_legal
    def enter_site(self):
        print(f"Welcome!")




my_user = User(date(2001, 6, 15))
print(f"Age: {my_user.age}")
my_user.enter_site()


my_user = User(date(2015, 6, 15))
print(f"Age: {my_user.age}")
my_user.enter_site()