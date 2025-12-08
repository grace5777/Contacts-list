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

# loading the contact list 
from loading_contacts import load_initial_contacts 

# the main menu
def main():
    book = ContactBook()
    load_initial_contacts(book)

    # display menu loop
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, address)

        elif choice == "2":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "3":
            name = input("Enter name to edit: ")
            phone = input("New phone (blank to skip): ")
            address = input("New address (blank to skip): ")
            # phone or none means if left blank it will skip it
            book.edit_contact(name, phone or None, address or None)

        elif choice == "4":
            name = input("Enter name to search: ")
            book.search(name)

        elif choice == "5":
            book.show_all()

        elif choice == "6":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
