class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self  

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.name} to make a withdrawal.")
        return self  

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self  


guido = User("Guido")
monty = User("Monty")


guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
monty.make_deposit(50).make_deposit(75).make_withdrawal(25).make_withdrawal(10).display_user_balance()
