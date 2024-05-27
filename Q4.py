#Question4: Object-Oriented Programming -Bank ClasS
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount

    def __str__(self):
        return f"Current balance: ${self.balance}, Interest rate: {self.interest_rate}%"

# Create an instance of BankAccount
account = BankAccount("22315", "BATOL")
account.deposit(1000)
print("Current balance:", account.get_balance())
account.withdraw(500)
print("Current balance:", account.get_balance())

# Create an instance of SavingsAccount
savings_account = SavingsAccount("7758", "NOUR", 0.05)
savings_account.deposit(2000)
print("Current balance before interest:", savings_account.get_balance())
savings_account.apply_interest()
print(savings_account)