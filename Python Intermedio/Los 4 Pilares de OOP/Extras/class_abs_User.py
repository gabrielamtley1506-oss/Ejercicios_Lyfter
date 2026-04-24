from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        allowed = ["read"]
        return permission in allowed


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.get_role())                    # Admin
print(user1.has_permission("delete"))      # True
print(user1.has_permission("read"))        # True

print(user2.get_role())                    # Regular
print(user2.has_permission("read"))        # True
print(user2.has_permission("delete"))      # False