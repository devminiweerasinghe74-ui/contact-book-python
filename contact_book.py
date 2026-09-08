import json
import re

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Search Contact")
    print("7. Exit")

def validate_phone(phone):
    pattern = r"^[0-9]{10}$"
    return re.fullmatch(pattern, phone) is not None


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.fullmatch(pattern, email) is not None

def add_contact(contact_book):
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if name in contact_book:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number! Enter a 10-digit phone number.")
        return

    email = input("Enter email: ").strip()

    if not validate_email(email):
        print("Invalid email address!")
        return

    address = input("Enter address: ").strip()

    if not address:
        print("Address cannot be empty!")
        return

    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")

def view_contact(contact_book):
    contact_name = input()

    # check given name in the contact dictionary
    if contact_name in contact_book:

        contact = contact_book[contact_name]

        print(f"Name: {contact_name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    else:
        print("Contact not found!")


def edit_contact(contact_book):
    contact_name = input("Enter contact name to edit: ").strip()

    if contact_name not in contact_book:
        print("Contact not found!")
        return

    contact = contact_book[contact_name]

    print("\nPress Enter to keep the current value.")

    phone = input(f"Phone [{contact['phone']}]: ").strip()

    if phone:
        if validate_phone(phone):
            contact['phone'] = phone
        else:
            print("Invalid phone number! Keeping the old phone number.")

    email = input(f"Email [{contact['email']}]: ").strip()

    if email:
        if validate_email(email):
            contact['email'] = email
        else:
            print("Invalid email address! Keeping the old email.")

    address = input(f"Address [{contact['address']}]: ").strip()

    if address:
        contact['address'] = address

    print("Contact updated successfully!")


def delete_contact(contact_book):
    contact_name = input("Enter contact name to delete: ").strip()

    if contact_name not in contact_book:
        print("Contact not found!")
        return

    confirmation = input(
        f"Are you sure you want to delete '{contact_name}'? (y/n): "
    ).strip().lower()

    if confirmation == 'y':
        del contact_book[contact_name]
        print("Contact deleted successfully!")

    elif confirmation == 'n':
        print("Deletion cancelled.")

    else:
        print("Invalid choice. Deletion cancelled.")


def list_all_contacts(contact_book):
    # Check if the contact_book is empty
    if len(contact_book) == 0:
        print("No contacts available.")

    else:

        for contact_name in contact_book:
            contact = contact_book[contact_name]
            print(f"Name: {contact_name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

def search_contact(contact_book):
    search_name = input("Enter contact name to search: ").strip().lower()

    if not search_name:
        print("Search name cannot be empty!")
        return

    found = False

    for contact_name, contact in contact_book.items():
        if search_name in contact_name.lower():
            print("\nContact found:")
            print(f"Name: {contact_name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

            found = True

    if not found:
        print("No matching contacts found.")

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

def save_contacts(contact_book):
    with open("contacts.json", "w") as file:
        json.dump(contact_book, file, indent=4)

def main():

    contact_book = load_contacts()

    while True:

        display_menu()

        choice = input()

        if choice == '1':
            add_contact(contact_book)
            save_contacts(contact_book)

        elif choice == '2':
            view_contact(contact_book)

        elif choice == '3':
            edit_contact(contact_book)
            save_contacts(contact_book)

        elif choice == '4':
            delete_contact(contact_book)
            save_contacts(contact_book)

        elif choice == '5':
            list_all_contacts(contact_book)

        elif choice == '6':
            search_contact(contact_book)

        elif choice == '7':
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()



















