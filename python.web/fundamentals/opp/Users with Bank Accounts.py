class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []  

    def create_account(self, initial_balance=0):
        new_account = (initial_balance)
        self.accounts.append(new_account)
        return self

    def make_deposit(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].deposit(amount)
        else:
            print("Invalid account index")

    def make_withdrawal(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].withdraw(amount)
        else:
            print("Invalid account index")

    def display_user_balance(self, account_index):
        if 0 <= account_index < len(self.accounts):
            print(f"User: {self.name}, Balance: {self.accounts[account_index].balance}")
        else:
            print("Invalid account index")


user1 = User("Alice", "alice@example.com")
user1.create_account(1000)  
user1.make_deposit(0, 500)  
user1.display_user_balance(0)  
user1.make_withdrawal(0, 200)  
user1.display_user_balance(0)  
user2 = User("Bob", "bob@example.com")
user2.create_account(500)  
user2.make_deposit(0, 200)  
user2.display_user_balance(0)  