
class User:
  def __init__(self, username, password):
    self.username = username
    self.__password = password

  def get_password(self):
    return "*****"

  def set_password(self, new_password):
    if len(new_password) >= 8:
      self.__password = new_password
      print("Passsword updated successfully")
    else:
      print("Password must be al least 8 characters")

user = User("vivian_aranha", "Secure123")
print(user.username)
print(user.get_password())
user.set_password("NewPassword")

class UserProfile:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.__password = password

  def show_profile(self):
    print(f"Username: {self.username}")
    print(f"Email: {self._email}")
    print(f"Password: {self.__password}")

user = UserProfile("Alice", "alice@example.com", "pass1234")
user.show_profile()

class Account:
  def __init__(self, balance):
    self.__balance = balance

  def get_balance(self):
    return self.__balance

  def set_balance(self, new_balance):
    if new_balance >= 0:
      self.__balance = new_balance
      print("Balance updated successfully")
    else:
      print("Invalid balance value")

account = Account(1000)
print(account.get_balance())
account.set_balance(1500)
print(account.get_balance())

class User:
  def __init__(self, username):
    self.__username = username
    self.__password = None

  def set_password(self, password):
    if len(password) < 6:
      print("Password must be at least 6 characters long")
    else:
      self.__password = password
      print("Password set successfully")


  def get_password(self):
    return self.__password

user = User("Alice")
user.set_password("password123")
print(user.get_password())

# Secure User Profile App

class UserProfile:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.__password = password
    self.set_password(password)

  # Getter for email
  def get_email(self):
    return self._email

  # Setter for Email
  def set_email(self, new_email):
    if "@" in new_email and "." in new_email:
      self._email = new_email
      print("Email updated successfully")
    else:
      print("Invalid email format")


  # Setter for password
  def set_password(self, new_password):
    if len(new_password) < 6:
      print("Password must be at least 6 characters long")
    else:
      self.__password = new_password
      print("Password set successfully")

  # Display Profile
  def display_profile(self):
    print("\n--- User Profile ---")
    print(f"Username: {self.username}")
    print(f"Email: {self._email}")
    print(f"Password: {self.__password}")


#Main Program
users = []

def create_user():
  username = input("Enter username: ")
  email = input("Enter email: ")
  password = input("Enter password: ")
  user = UserProfile(username, email, password)
  users.append(user)
  print("User created successfully")

def view_profiles():
  if not users:
    print("No users found")
  else:
    for user in users:
      user.display_profile()

def update_email():
  username = input("Enter username to update email: ")
  for user in users:
    if user.username == username:
      new_email = input("Enter new email: ")
      user.set_email(new_email)
      return
  print("User not found")

# Main Menu

while True:
  print("\n--- Secure User Profile App ---")
  print("1. Create User")
  print("2. View All Profiles")
  print("3. Update Email")
  print("4. Exit")

  choice = input("Enter your choice(1-4): ")

  if choice == "1":
    create_user()
  elif choice == "2":
    view_profiles()
  elif choice == "3":
    update_email()
  elif choice == "4":
    print("Exiting the program")
    break
  else:
    print("Invalid choice. Please try again")