class User:
    def __init__(self, id, name, email, phone_number):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string. ")
        if len(value) == 0:
            raise ValueError("Name cannot be empty!!!")
        
        self.name = value
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self._phone_number
    
    def create_user(self, cursor):
        cursor.execute("INSERT INTO users (name, email, phone_number) VALUES (?, ?, ?)", (self._name, self._email, self._phone_number))
        self._id = cursor.lastrowid
        return cursor
    #getting all users

    @classmethod
    def get_all_users(cls, cursor):
        cursor.execute("SELECT * FROM users")
        user_data = cursor.fetchall()
        return [cls(id=row[0], name=row[1]) for row in user_data]
    
    #getting user by phone number

    def get_user(self, cursor):
        cursor.execute("SELECT * FROM users WHERE phone_number = ?", (self._phone_number))
        all_user = cursor.fetchall()
        return all_user

    #getting book lent to user

    def book(self, cursor):
        cursor.execute("""
            SELECT books.title
            FROM books
            JOIN bookscheckout ON books.id = bookscheckout.book_id
            WHERE bookcheckout.user_id = ?
        """, (self._id,))
        book_data = cursor.fetchall()
        return book_data

