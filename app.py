from database.connection import db_connection
from database.setup import create_tables
from lib.models.book import Book
from lib.models.user import User
from lib.models.bookcheckout import Bookcheckout

#user
def create_user(cursor):
    username = input("Enter user name: ")
    user = User(None, username, None, None)
    user.create_user(cursor)
    print("User created")

def get_all_users(cursor):
    users = User.get_all_users(cursor)
    if users:
        print("All Users: ")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("No User Found")

def get_user(cursor):
    user_num = input("Enter the phone number: ")
    user = User(None, None, None, user_num)
    num = user.get_user(cursor)

def book(cursor):
    user_id = input("Enter the user's ID to display book: ")
    user = User(user_id, None, None, None)
    books = user.book(cursor)

    if books:
        print(f"Book lent to User ID {user_id}:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Publication: {book[2]}, Author: {book[3]}")
    else:
        print(f"No books found for User {user_id}.")




def main():
    
    create_tables()

    while True:
        print("\nChoose:")
        print("1.  Add User")
        print("2.  Add Book")
        print("3.  Create Article")

        choice = input


if __name__ == "__main__":
    main()
