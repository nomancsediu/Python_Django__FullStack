
class Calculator:
  base_value = 100

  @staticmethod
  def add(value1, value2):
    return value1 + value2

  @classmethod
  def multiply_base(cls, multiplier):
    return cls.base_value * multiplier

# Using Static Method
print(Calculator.add(4, 5))

# Using Class Method
print(Calculator.multiply_base(2))

class Utility:
  @staticmethod
  def greet_user(name):
    print(f"Hello, {name}")

Utility.greet_user("John")

class Counter:
  count = 0

  @classmethod
  def increment(cls):
    cls.count += 10

Counter.increment()
print(Counter.count)

# Inventory Management System

class Inventory:
  total_items = 0

  def __init__(self, product_name, price, quantity):
    self.product_name = product_name
    self.price = price
    self.quantity = quantity
    Inventory.total_items += quantity

  # Instance Method: Show Product Details
  def show_product_details(self):
    print("\n--- Product Details ---")
    print(f"Product Name: {self.product_name}")
    print(f"Price: {self.price}")
    print(f"Quantity: {self.quantity}")

  # Instance Method: Sell Product
  def sell_product(self, amount):
    if amount <= self.quantity:
      self.quantity -= amount
      Inventory.total_items -= amount
      print(f"{amount} {self.product_name}(s) sold.")
    else:
      print("Insufficient quantity.")

  # Static Method: Calculate Discount
  @staticmethod
  def calculate_discount(price, discount_percentage):
    return price * (1 - discount_percentage / 100)

  # Class Method: Total Items Report
  @classmethod
  def total_items_report(cls):
    print(f"\nTotal Items: {cls.total_items}")

# Main Program
products = []

# Add Product to inventory
def add_product():
  product_name = input("Enter product name: ")
  price = float(input("Enter price: "))
  quantity = int(input("Enter quantity: "))
  product = Inventory(product_name, price, quantity)
  products.append(product)
  print(f"{quantity} {product_name}(s) added to inventory.")

#Display All Products
def view_products():
  print("\n--- Inventory ---")
  if not products:
    print("No products in inventory.")
  else:
    for product in products:
      product.show_product_details()

# Sell Product
def sell_product():
  product_name = input("Enter product name to sell: ")
  for product in products:
    if product.product_name == product_name:
      amount = int(input("Enter amount to sell: "))
      product.sell_product(amount)
      break
  else:
    print("Product not found in inventory.")

# Calculate Discount
def discount_price():
  price = float(input("Enter price: "))
  discount_percentage = float(input("Enter discount percentage: "))
  discounted_price = Inventory.calculate_discount(price, discount_percentage)
  print(f"Discounted Price: {discounted_price}")


# Main Menu
while True:
  print("\n--- Inventory Management System ---")
  print("1. Add Product")
  print("2. View Products")
  print("3. Sell Product")
  print("4. Calculate Discount")
  print("5. Total Items Report")
  print("6. Exit")

  choice = input("Enter your choice(1-6): ")

  if choice == "1":
    add_product()
  elif choice == "2":
    view_products()
  elif choice == "3":
    sell_product()
  elif choice == "4":
    discount_price()
  elif choice == "5":
    Inventory.total_items_report()
  elif choice == "6":
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please try again.")