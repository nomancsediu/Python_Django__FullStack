my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

contact = {
    "name": "John Doe",
    "phone": "123-456-7890",
    "email": "john@example.com"
}

# print(contact.get("email"))

contact["phone"] = "980-123-4563"

# print(contact)

contact["address"] = "123 Main St"

# print(contact)

# del contact["email"]

print(contact)

for key, value in contact.items():
    print(f"{key}: {value}")

if "email" in contact:
    print("Email found!")
else:
    print("Email not found.")

from os import name
# Contact Book

# Step 1: Initialize an empty contact book
contacts = {}

# Step 2: Display the menu
def show_menu():
  print("\n--- Contact Book Menu ---")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Search Contact")
  print("4. Edit Contact")
  print("5. Delete Contact")
  print("6. Exit")

# Step 3: Add a Contact
def add_contact():
  name = input("Enter contact name: ")
  phone = input("Enter contact number: ")
  email = input("Enter contact email: ")
  contacts[name] = {"phone": phone, "email": email}
  print(f"Contact {name} has been added to your contact book successfully!")

# Step 4: View All Contacts
def view_contacts():
  if contacts:
    print("\n--- Contact List ---")
    for name, details in contacts.items():
      print(f"Name: {name}")
      print(f"Phone: {details['phone']}")
      print(f"Email: {details['email']}")
  else:
    print("Your contact book is empty.")

# Step 5: Search a Contact
def search_contact():
  name = input("Enter the name of the contact you want to search: ")
  if name in contacts:
    print(f"\n--- Contact Details for {name} ---")
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
  else:
    print(f"Contact {name} not found in your contact book.")

# Step 6: Edit a contact
def edit_contact():
  name = input("Enter the name of the contact you want to edit: ")
  if name in contacts:
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} has been updated successfully!")
  else:
    print(f"Contact {name} not found in your contact book.")

# Step 7: Delete a contact
def delete_contact():
  name = input("Enter the name of the contact you want to delete: ")
  if name in contacts:
    del contacts[name]
    print(f"Contact {name} has been deleted successfully!")
  else:
    print(f"Contact {name} not found in your contact book.")

# Step 8: Main Program Loop
while True:
  show_menu()
  choice = input("Enter your choice (1-6): ")

  if choice == "1":
    add_contact()
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    search_contact()
  elif choice == "4":
    edit_contact()
  elif choice == "5":
    delete_contact()
  elif choice == "6":
    print("Thank you for using the Contact Book. Goodbye!")
    break
  else:
    print("Invalid choice. Please select a valid option (1-6).")