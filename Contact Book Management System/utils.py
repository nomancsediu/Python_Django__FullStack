# utils.py_Abdullah Al Noman

def print_contacts(contact_list):
    if not contact_list:
        print("No contacts found.")
        return
    print("\n===== All Contacts =====")
    for idx, c in enumerate(contact_list, start=1):
        print(f"{idx}. Name : {c['name']}")
        print(f"   Phone : {c['phone']}")
        print(f"   Email : {c['email']}")
        print(f"   Address: {c['address']}\n")
    print("========================\n")
