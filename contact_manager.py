from validators import validate_phone, validate_email


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
    contact_name = input("Enter contact name: ").strip()

    if contact_name not in contact_book:
        print("Contact not found!")
        return

    contact = contact_book[contact_name]

    print(f"Name: {contact_name}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")


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
            print("Invalid phone number! Keeping old phone number.")

    email = input(f"Email [{contact['email']}]: ").strip()

    if email:
        if validate_email(email):
            contact['email'] = email
        else:
            print("Invalid email address! Keeping old email.")

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

    if confirmation == "y":
        del contact_book[contact_name]
        print("Contact deleted successfully!")

    elif confirmation == "n":
        print("Deletion cancelled.")

    else:
        print("Invalid choice. Deletion cancelled.")


def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
        return

    for contact_name, contact in contact_book.items():
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