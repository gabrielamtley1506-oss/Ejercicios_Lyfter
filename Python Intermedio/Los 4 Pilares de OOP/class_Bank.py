class Bank_account:
    def __init__(self, balance):
        self.balance = balance

    
    def add_balance(self, amount=None):
        while True:
            if amount is None:
                try:
                    amount = int(input("How much you want to add: "))
                except ValueError:
                    print("Error: Please enter a valid number, not letters")
                    continue
            if amount <= 0: 
                print("Error the amount must be positive")
                amount = None
            else:
                self.balance += amount
                break
        return self.balance



    def withdraw_balance(self, amount=None):
        while True:
            if amount is None:
                try:
                    amount = int(input("How much you want to withdraw: "))
                except ValueError:
                    print("Error: Please enter a valid number, not letters")
                    continue
            if amount <= 0:
                print("The amount to withdraw must be positive")
                amount = None
            elif amount > self.balance:
                print("Insufficient funds")
                amount = None
            else :
                self.balance -= amount
                break
        return self.balance

class Savings_account(Bank_account):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def withdraw_balance(self, amount=None):
        while True:
            if amount is None:
                try:
                    amount = int(input("How much you want to withdraw: "))
                except ValueError:
                    print("Error: Please enter a valid number, not letters")
                    continue
            if amount <= 0:
                print("The amount to withdraw must be positive")
                amount = None
            elif amount > self.balance:
                print("Insufficient funds")
                amount = None
            elif self.balance - amount < self.min_balance:
                print(f"Your balance has to be above your minimum required that is: ${self.min_balance}")
                amount = None
            else :
                self.balance -= amount
                break
        return self.balance

account1 = Bank_account(2000)
print(f"The account balance is: ${account1.add_balance()}")
print(f"After the withdraw the account balance is: ${account1.withdraw_balance()}")


saving_Gaby=Savings_account(1000, 50)
print(f"The account balance is: ${saving_Gaby.add_balance()}")
print(f"After the withdraw the account balance is: ${saving_Gaby.withdraw_balance()}")
