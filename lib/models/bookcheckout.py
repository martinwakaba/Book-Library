from datetime import date

class Bookcheckout:
    def __init__(self, id, user_id, book_id, genre, checkout_date):
        self._id =id
        self._user_id = user_id
        self._book_id = book_id
        self._genre = genre
        self._checkout_date = checkout_date

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
            raise ValueError("checkout_date must be a date instance")