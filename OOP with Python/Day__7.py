
# The Mini ATM Machine will allow users to:

# Authenticate with PINs securely.
# Check account balance.
# Deposit money.
# Withdraw money with balance validation.
# Change PIN.
# Exit securely.

# Classes Overview:

# BankAccount
# Attributes: account_number, pin, balance
# Methods: check_balance(), deposit(), withdraw(), change_pin()


# ATM
# Manages account authentication.
# Provides the main menu for users.

# Concepts Applied:

# Encapsulation: Secure PIN handling and balance access.
# Static Method: For utility tasks like PIN validation.
# Class Method: To maintain account-level settings.
# Polymorphism: Flexibility in transaction operations.

# Mini ATM Machine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    # Validate Pin
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin

    # Check Balance
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    #Withdraw Money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    # Change Pin
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Failed to change Pin. Ensure the old Pin si correct and the new PIN is 4 digits")

class ATM:
    def __init__(self):
        self.accounts = {}

    # Create Account
    def create_account(self):
        account_number = input("Enter account number: ")
        pin = input("Set a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully.")
        else:
            print("Invalid PIN. PIN must be 4 digits.")

    #Authenticate Account
    def authenticate_account(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentication Successful.")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN.")

    # Account Menu
    def account_menu(self, account):
        while True:
            print("\n--- ATM Menu ---:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            choice = input("Enter your choice(1-5): ")

            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == '5':
                print("Logging out. Thank you for using out ATM.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    # Main Men
    def main_menu(self):
        while True:
            print("\n--- Welcome to Mini ATM Machine ---:")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.authenticate_account()
            elif choice == '3':
                print("Thank you for using Mini ATM Machine. Goodbye!")
                break
            else:
                print("Invalid Choice. Please try again")


# Start the ATM System
if __name__ == "__main__":
  atm = ATM()
  atm.main_menu()

