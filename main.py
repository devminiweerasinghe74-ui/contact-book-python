from storage import load_contacts, save_contacts
from contact_manager import (
    add_contact,
    view_contact,
    edit_contact,
    delete_contact,
    list_all_contacts,
    search_contact
)


def display_header():
    print("\n" + "=" * 45)
    print("           CONTACT BOOK")
    print("=" * 45)


def display_menu():
    print("\n" + "-" * 45)
    print("MAIN MENU")
    print("-" * 45)

    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Search Contact")
    print("7. Exit")

    print("-" * 45)


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-7): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice

        print("Invalid choice! Please enter a number from 1 to 7.")


def pause():
    input("\nPress Enter to continue...")


def main():
    contact_book = load_contacts()

    display_header()

    while True:
        display_menu()

        choice = get_menu_choice()

        try:
            if choice == "1":
                add_contact(contact_book)
                save_contacts(contact_book)
                pause()

            elif choice == "2":
                view_contact(contact_book)
                pause()

            elif choice == "3":
                edit_contact(contact_book)
                save_contacts(contact_book)
                pause()

            elif choice == "4":
                delete_contact(contact_book)
                save_contacts(contact_book)
                pause()

            elif choice == "5":
                list_all_contacts(contact_book)
                pause()

            elif choice == "6":
                search_contact(contact_book)
                pause()

            elif choice == "7":
                print("\nThank you for using Contact Book!")
                print("Goodbye!")
                break

        except Exception as error:
            print(f"\nAn unexpected error occurred: {error}")
            print("Please try again.")
            pause()


if __name__ == "__main__":
    main()