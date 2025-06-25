# file_manager.py_Abdullah Al Noman

import csv

def load_from_file(filename="contacts.csv"):
    contacts = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  
    return contacts

def save_to_file(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
