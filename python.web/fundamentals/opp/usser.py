class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        else:
            print("Insufficient balance for the transfer.")


user1 = User("Guido van Rossum")
user2 = User("Linus Torvalds")
user3 = User("Larry Page")



user1.make_deposit(300)
user1.make_withdrawal(20)


user1.display_user_balance()


user2.make_deposit(200)

user2.make_withdrawal(70)



user2.display_user_balance()


user3.make_deposit(500)
user3.make_withdrawal(100)


user3.display_user_balance()


user1.transfer_money(user3, 40)


user1.display_user_balance()
user3.display_user_balance()
