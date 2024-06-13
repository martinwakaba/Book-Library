# lib/models/bookcheckout.py

from datetime import datetime, date

class Bookcheckout:
    def __init__(self, id, user_id, book_id, genre, checkout_date, checkin_date, book_taken=False):
        self._id = id
        self._user_id = user_id
        self._book_id = book_id
        self._genre = genre
        self._checkout_date = checkout_date
        self._checkin_date = checkin_date
        self._book_taken = book_taken

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def genre(self):
        return self._genre

    @property
    def checkout_date(self):
        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, value):
        if isinstance(value, date):
            self._checkout_date = value
        else:
            raise ValueError("check-out date must be a date instance")

    @property
    def checkin_date(self):
        return self._checkin_date

    @checkin_date.setter
    def checkin_date(self, value):
        if isinstance(value, date):
            self._checkin_date = value
        else:
            raise ValueError("check-in date must be a date instance")

    @property
    def book_taken(self):
        return self._book_taken

    @book_taken.setter
    def book_taken(self, value):
        if not isinstance(value, bool):
            raise ValueError("book_taken must be a boolean")
        self._book_taken = value

    # Adding check in and check out time
    def add_date(self, cursor):
        cursor.execute("INSERT INTO bookscheckout (checkin_date, checkout_date, book_taken) VALUES (?, ?, ?)",
                       (self._checkin_date, self._checkout_date, self._book_taken))
        time_date = cursor.lastrowid
        return time_date
    
    #checking availabilty of the book
    def checkout_book(self, cursor):
        cursor.execute("INSERT INTO bookscheckout (user_id, book_id, genre, checkout_date, book_taken) VALUES (?, ?, ?, ?, ?)",
                       (self._user_id, self._book_id, self._genre, self._checkout_date, self._book_taken))
        rows = cursor.rowcount  
        if rows > 0:
           
            cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (self._book_id,))
        return rows
