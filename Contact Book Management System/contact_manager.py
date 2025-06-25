# contact_manager.py_Abdullah Al Noman

import utils

class ContactManager:
    def __init__(self):
        self.contacts = []

    def load_contacts(self, contact_list):
        self.contacts = contact_list

    def add_contact(self, name, phone, email, address):
       
        if not phone.isdigit():
            return "Error: The phone number must be an integer."

        for contact in self.contacts:
            if contact['phone'] == phone:
                return "Error: Phone number already exists for another contact."

        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        return "Contact added successfully!"

    def view_contacts(self):
        return self.contacts

    def search_contact(self, term):
        term = term.lower()
        results = []
        for contact in self.contacts:
            if (term in contact['name'].lower() or
                term in contact['phone'] or
                term in contact['email'].lower()):
                results.append(contact)
        return results

    def remove_contact(self, phone):
        for contact in self.contacts:
            if contact['phone'] == phone:
                self.contacts.remove(contact)
                return "Contact deleted successfully!"
        return "Contact not found!"
