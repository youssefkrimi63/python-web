class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []  # List to store associated BankAccount instances

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

# Example usage:
user1 = User("Alice", "alice@example.com")
user1.create_account(1000)  # Create an account with an initial balance of $1000
user1.make_deposit(0, 500)  # Deposit $500 into the first account
user1.display_user_balance(0)  # Display the balance of the first account
user1.make_withdrawal(0, 200)  # Withdraw $200 from the first account
user1.display_user_balance(0)  # Display the updated balance of the first account

user2 = User("Bob", "bob@example.com")
user2.create_account(500)  # Create an account with an initial balance of $500
user2.make_deposit(0, 200)  # Deposit $200 into the first account
user2.display_user_balance(0)  # Display the balance of the first account
