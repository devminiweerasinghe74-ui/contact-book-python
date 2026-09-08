import json


FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_contacts(contact_book):
    with open(FILE_NAME, "w") as file:
        json.dump(contact_book, file, indent=4)