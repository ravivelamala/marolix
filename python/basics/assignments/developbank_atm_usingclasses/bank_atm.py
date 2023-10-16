# develop bank(atm) application using classes 
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid withdrawal amount or insufficient balance."


# Example usage of the BankAccount class
account_number = "12345"  # Replace with your account number
account = BankAccount(account_number)

# Check initial balance
print(account.check_balance())

# Deposit funds
deposit_amount = 100
print(account.deposit(deposit_amount))

# Withdraw funds
withdraw_amount = 50
print(account.withdraw(withdraw_amount))

# Check updated balance
print(account.check_balance())
