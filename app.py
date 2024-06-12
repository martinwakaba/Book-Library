from database.connection import db_connection
from database.setup import create_tables
from lib.models.book import Book
from lib.models.user import User
from lib.models.bookcheckout import Bookcheckout

#user
def create_user(cursor):
    username = input("Enter user name: ")
    email = input("Enter email address")
    phone_number = input("Enter phone number")
    user = User(None, username, email, phone_number)
    user.create_user(cursor)
    print("User Added successfully!!!")

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

    if num:
        print(f"User associated with phone number {user_num}:")
        for n in num:
            print(f"ID: {n[0]}, Name: {n[1]}, Email: {n[2]}")
    else:
        print(f"No match!")        

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
        print("2.  Show Users")
        print("3.  Show User by number")

        choice = input("\nEnter A Number: ")

        if choice == "1":
            conn = db_connection()
            cursor = conn.cursor()
            create_user(cursor)
            conn.commit()
            conn.close()
        elif choice == "2":
            conn = db_connection()
            cursor = conn.cursor()
            get_all_users(cursor)
            conn.commit()
            conn.close()
        elif choice == "3":
            conn = db_connection()
            cursor = conn.cursor()
            get_user(cursor)
            conn.commit()
            conn.close()
        else:
            break




if __name__ == "__main__":
    main()
