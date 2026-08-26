# Contact Book

A simple command-line Contact Book application built with Python. The application allows users to manage contact information through a menu-driven interface.

## Features

* Add a new contact
* View a contact
* Edit contact information
* Delete a contact
* List all saved contacts
* Prevent duplicate contact names
* Display messages when a contact is not found
* Simple command-line interface

## Technologies Used

* Python 3
* Python Dictionaries
* Functions
* Conditional Statements
* Loops
* Command-Line Interface (CLI)

## Project Structure

```text
Contact-Book-Application/
│
├── contact_book.py
├── README.md
└── .gitignore
```

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository.
3. Open the project directory in a terminal.
4. Run:

```bash
python contact_book.py
```

## How It Works

The application displays a menu with six options:

1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit

Contact information is currently stored in a Python dictionary while the application is running.

## Current Limitations

The current version stores contacts only in memory. Therefore, contacts are lost when the application is closed.

## Future Improvements

* Add persistent data storage using JSON or SQLite
* Add contact search functionality
* Add input validation
* Improve error handling
* Add phone number and email validation
* Add a graphical user interface (GUI)
* Organize the application using a more modular architecture

## Author

Devmini Weerasinghe
