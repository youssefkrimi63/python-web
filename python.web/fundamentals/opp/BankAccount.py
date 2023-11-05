class BankAccount:
    all_accounts = []  

    def __init__(self, interest_rate=0.01, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


account1 = BankAccount(0.01, 1000)
account2 = BankAccount()


account1.deposit(200).deposit(300).deposit(100).withdraw(150).yield_interest().display_account_info()


account2.deposit(300).deposit(500).withdraw(100).withdraw(200).withdraw(50).withdraw(250).yield_interest().display_account_info()


BankAccount.print_all_accounts_info()
