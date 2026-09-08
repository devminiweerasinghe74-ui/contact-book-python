import json


FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty contact book.")
        return {}

    except json.JSONDecodeError:
        print("Warning: Contact data file is corrupted.")
        print("Starting with an empty contact book.")
        return {}

    except OSError as error:
        print(f"Error loading contacts: {error}")
        return {}


def save_contacts(contact_book):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contact_book, file, indent=4)

    except OSError as error:
        print(f"Error saving contacts: {error}")