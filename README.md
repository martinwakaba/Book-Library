Book Library Management System
Overview
The Book Library Management System is a Python application designed to manage users, books, and book checkouts within a library. It allows users to add new users, add books to the library, associate users with borrowed books, and perform various queries related to users and books.

Small Presentation for this project https://docs.google.com/presentation/d/1Qx0XBm5y5-P2EQkuRiYUC54QlZawsoKnlK-V4AiUCdo/edit#slide=id.g2e579e6d25f_0_8

Features
User Management:

Add new users with their name, email, phone number, and optionally assign them a book from the library.
Retrieve all users or find a specific user by phone number.
Book Management:

Add new books with details like title, publication date, author, and genre.
Retrieve all books, filter books by genre or author.
Book Checkout System:

Track books borrowed by users, including checkout and check-in dates.
Automatically update the checkout status when a user takes a book.
Components
The project consists of the following major components:

Database Setup (database/setup.py):

Defines the structure of the database tables (books, users, bookscheckout).
Sets up relationships between tables using foreign keys.
Models (lib/models/):

User (user.py):
Manages user data, including creation, retrieval, and association with borrowed books.
Book (book.py):
Handles book data, including creation, retrieval, and querying by genre or author.
Bookcheckout (bookcheckout.py):
Manages the checkout process, updating the bookscheckout table with user-book associations.
Application Logic (app.py):

Provides a command-line interface (CLI) for interacting with the system.
Allows users to add new users, add books, borrow books, and perform various queries on users and books.
Getting Started
Setup:

Ensure Python 3.x is installed.
Install required dependencies using pip install -r requirements.txt.
Database Initialization:

Run python app.py to initialize the database tables (books, users, bookscheckout).
Usage:

Follow the CLI prompts to add users, add books, and perform queries.
Choose options from the menu displayed in the CLI to interact with different functionalities.
Dependencies
Python 3.x
SQLite (for database storage)
Required Python packages (check requirements.txt for details)
Contributing
Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
