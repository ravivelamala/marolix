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

while True:
    print("Options:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")

    choice = input("Enter option (1/2/3/4): ")

    if choice == "1":
        print(account.check_balance())
    elif choice == "2":
        amount = float(input("Enter the deposit amount: $"))
        print(account.deposit(amount))
    elif choice == "3":
        amount = float(input("Enter the withdrawal amount: $"))
        print(account.withdraw(amount))
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
