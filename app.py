from database.connection import db_connection
from database.setup import create_tables
from lib.models.book import Book
from lib.models.user import User
from lib.models.bookcheckout import Bookcheckout

#user
def create_user(cursor):
    username = input("Enter user name: ")
    user = User(None, username)
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


def main():
    
    create_tables()

if __name__ == "__main__":
    main()
