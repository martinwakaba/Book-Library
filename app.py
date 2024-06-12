from database.connection import db_connection
from database.setup import create_tables
from lib.models.book import Book
from lib.models.user import User
from lib.models.bookcheckout import Bookcheckout

#user
def create_user(cursor):
    username = input("Enter user name: ")
    email = input("Enter email address: ")
    phone_number = input("Enter phone number: ")
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
    user = User.get_user(cursor, user_num)  
    if user:
        print(f"User associated with phone number {user_num}:")
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print(f"No match!")        

def book(cursor):
    user_id = input("Enter the user's ID to display books: ")
    user = User(user_id, None, None, None)
    books = user.book(cursor)

    if books:
        print(f"Books lent to User ID {user_id}:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Publication Date: {book[2]}, Author: {book[3]}, Genre: {book[4]}")
    else:
        print(f"No books found for User {user_id}.")


#book

def add_book(cursor):
    book_title = input("Enter book title: ")
    publication = input("Enter publication date: ")
    author = input("Enter book's author: ")
    genre = input("Enter the genre of the book: ")
    book = Book(None, book_title, publication, author, genre)
    book.add_book(cursor)
    print("Book Added successfully!!!")

def get_all_books(cursor):
    all_books = Book.get_all_books(cursor)
    if all_books:
        print("All books")
        for book in all_books:
            print(f"ID: {book.id}, Title: {book.title}, Publication Date: {book.publication_date}, Author: {book.author}, Genre: {book.genre}")

    else:
        print(f"No Books available")

def get_book_by_genre(cursor):
    book_genre = input("Enter the book genre: ")
    book = Book.get_book_by_genre(cursor, book_genre)  
    if book:
        print(f"User associated with phone number {book_genre}:")
        print(f"ID: {book.id}, Title: {book.title}, Publication Date: {book.publication_date}, Author: {book.author}")
    else:
        print(f"No match!")



def main():
    
    create_tables()

    while True:
        print("\nChoose:")
        print("1.  Add User")
        print("2.  Show Users")
        print("3.  Show User by number")
        print("4.  Show Book lent to user")
        print("5.  Add a book")
        print("6.  Show books")
        print("7. Show Book by genre")

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
        elif choice == "4":
            conn = db_connection()
            cursor = conn.cursor()
            book(cursor)
            conn.commit()
            conn.close()    
        elif choice == "5":
            conn = db_connection()
            cursor = conn.cursor()
            add_book(cursor)
            conn.commit()
            conn.close()
        elif choice == "6":
            conn = db_connection()
            cursor = conn.cursor()
            get_all_books(cursor)
            conn.commit()
            conn.close()
        elif choice == "7":
            conn = db_connection()
            cursor = conn.cursor()
            get_book_by_genre(cursor)
            conn.commit()
            conn.close()    
        else:
            break




if __name__ == "__main__":
    main()
