class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def display_info(self):
    print(f"This is a {self.brand}: {self.model}.")

# Create an object
my_car = Car("Tesla", "Model 3")
my_car.display_info()

your_car = Car("Honda", "Accord")
your_car.display_info()

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"{self.name} is barking!")

# Create objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog2.bark()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("John", 25)
person1.greet()

# Bank Account Simulator

class BankAccount:
  def __init__(self, account_holder, initial_balance=0):
    self.account_holder = account_holder
    self.balance = initial_balance

  #Deposit Money
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")

  #Withdraw Money
  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")

  # Show Account Details
  def show_details(self):
    print("\n--- Account Details ---")
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Balance: ${self.balance}")


# Main Program
accounts = {}

def create_account():
  name = input("Enter account holder's name: ").strip()
  initial_deposit = float(input("Enter initial Deposit Amount: "))
  account = BankAccount(name, initial_deposit)
  accounts[name] = account
  print("Account created successfully!")

def access_account():
  name = input("Enter your name: ").strip()
  if name in accounts:
    account = accounts[name]
    while True:
      print("\n--- Account Menu ---")
      print("1. Deposit")
      print("2. Withdraw")
      print("3. Show Details")
      print("4. Exit")
      choice = input("Enter your choice(1-4): ")

      if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
      elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
      elif choice == '3':
        account.show_details()
      elif choice == '4':
        print("Exiting account menu.")
        break
      else:
        print("Invalid choice. Please select a valid option.")
  else:
    print("Account not found. Please create an account first.")

# Main Menu
while True:
  print("\n--- Bank Account Simulator ---")
  print("1. Create Account")
  print("2. Access Account")
  print("3. Exit")
  choice = input("Enter your choice(1-3): ")

  print(accounts)

  if choice == '1':
    create_account()
  elif choice == '2':
    access_account()
  elif choice == '3':
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid choice. Please select a valid option.")