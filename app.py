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



def main():
    
    create_tables()

if __name__ == "__main__":
    main()
