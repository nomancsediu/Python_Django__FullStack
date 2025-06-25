# main.py_Abdullah Al Noman

from contact_manager import ContactManager
import file_manager
import utils

def show_menu():
    print("\n=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")

def main():
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... ", end="")
    manager = ContactManager()
    contacts = file_manager.load_from_file()
    manager.load_contacts(contacts)
    print("Done!")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            result = manager.add_contact(name, phone, email, address)
            print(result)
            if "successfully" in result:
                file_manager.save_to_file(manager.view_contacts())

        elif choice == '2':
            contacts = manager.view_contacts()
            utils.print_contacts(contacts)

        elif choice == '3':
            term = input("Enter search term (name/email/phone): ")
            results = manager.search_contact(term)
            if results:
                utils.print_contacts(results)
            else:
                print("No matching contact found.")

        elif choice == '4':
            phone = input("Enter the phone number of the contact to delete: ")
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                result = manager.remove_contact(phone)
                print(result)
                file_manager.save_to_file(manager.view_contacts())

        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select from the menu.")

if __name__ == "__main__":
    main()
