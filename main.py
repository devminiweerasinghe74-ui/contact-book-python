from storage import load_contacts, save_contacts
from contact_manager import (
    add_contact,
    view_contact,
    edit_contact,
    delete_contact,
    list_all_contacts,
    search_contact
)


def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Search Contact")
    print("7. Exit")


def main():
    contact_book = load_contacts()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contact_book)
            save_contacts(contact_book)

        elif choice == "2":
            view_contact(contact_book)

        elif choice == "3":
            edit_contact(contact_book)
            save_contacts(contact_book)

        elif choice == "4":
            delete_contact(contact_book)
            save_contacts(contact_book)

        elif choice == "5":
            list_all_contacts(contact_book)

        elif choice == "6":
            search_contact(contact_book)

        elif choice == "7":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()