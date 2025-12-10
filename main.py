# importing from the other files
from loading_contacts import load_initial_contacts 
from contact import contact_book

# the main menu
def main():
    book = contact_book()
    load_initial_contacts(book)

    # display menu loop
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add a contact")
        print("2. Delete a contact")
        print("3. Edit a contact")
        print("4. Search for a contact")
        print("5. Show all contacts")
        print("6. Exit")

        choice = input("Please choose an option: ")

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
