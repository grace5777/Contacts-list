# contact class that stores the name, number and address
class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    # this is how the contact will be printed out 
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Address: {self.address}"

# the class for the contact list stored using a hash table
class ContactBook:

    def __init__(self):
        # using a python dictonary as the hash table
        # key = contact name
        # value = contact object
        self.contacts = {}

    # adding in a new contact (1)
    def add_contact(self, name, phone, address):
        # preventing duplicate contacts
        if name in self.contacts:
            print("A contact with this name already exists.")
            return
        self.contacts[name] = Contact(name, phone, address)
        print("Contact added successfully.")

    # removing a specific contact (2)
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # editing a specific contact (3)
    def edit_contact(self, name, new_phone=None, new_address=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        # will only update fields that have been provided otherwise will stay the same
        if new_phone:
            self.contacts[name].phone = new_phone
        if new_address:
            self.contacts[name].address = new_address
        print("Contact updated.")

    # searching for a specific contact (4)
    def search(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found.")

    # showing all the contacts (5)
    def show_all(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts.values():
            print(contact)