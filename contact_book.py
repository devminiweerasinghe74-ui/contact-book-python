def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    phone = input("Enter phone number: ").strip()

    if not phone:
        print("Phone number cannot be empty!")
        return

    email = input("Enter email: ").strip()

    if not email:
        print("Email cannot be empty!")
        return

    address = input("Enter address: ").strip()

    if not address:
        print("Address cannot be empty!")
        return

    # Check if the name already exists
    if name in contact_book:
        print("Contact already exists!")
    else:
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
    contact_name = input()

    # check given user already in the list
    if contact_name in contact_book:
        # input rest of details
        contact_phone = input()
        contact_email = input()
        contact_address = input()

        contact = contact_book[contact_name]

        contact['phone'] = contact_phone
        contact['email'] = contact_email
        contact['address'] = contact_address

        print("Contact updated successfully!")

    # if user give empty input
    elif contact_name not in contact_book or contact_name == '':
        print("Contact not found!")


def delete_contact(contact_book):
    contact_name = input()

    if contact_name in contact_book:

        del contact_book[contact_name]
        print("Contact deleted successfully!")

    else:
        print("Contact not found!")


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

def main():
    contact_book = {}

    while True:

        display_menu()

        choice = input()

        if choice == '1':
            add_contact(contact_book)

        elif choice == '2':
            view_contact(contact_book)

        elif choice == '3':
            edit_contact(contact_book)

        elif choice == '4':
            delete_contact(contact_book)

        elif choice == '5':
            list_all_contacts(contact_book)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()



















