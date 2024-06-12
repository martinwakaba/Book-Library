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
        
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10:
            raise ValueError("Phone number should be 10 characters")
        self._phone_number = value
    
    def create_user(self, cursor):
        cursor.execute("INSERT INTO users (name, email, phone_number) VALUES (?, ?, ?)", (self._name, self._email, self._phone_number))
        self._id = cursor.lastrowid
        return cursor
    #getting all users

    @classmethod
    def get_all_users(cls, cursor):
        cursor.execute("SELECT * FROM users")
        user_data = cursor.fetchall()
        return [cls(id=row[0], name=row[1], email=row[2], phone_number=row[3]) for row in user_data]
    
    #getting user by phone number
    @classmethod
    def get_user(cls, cursor, phone_number):
        cursor.execute("SELECT * FROM users WHERE phone_number = ?", (phone_number,))
        user_data = cursor.fetchone()
        return cls(id=user_data[0], name=user_data[1], email=user_data[2], phone_number=user_data[3]) if user_data else None

    #getting book lent to user

    def book(self, cursor):
        cursor.execute("""
            SELECT books.id, books.title, books.publication_date, books.author, books.genre
            FROM books
            JOIN bookscheckout ON books.id = bookscheckout.book_id
            WHERE bookscheckout.user_id = ?
        """, (self._id,))
        book_data = cursor.fetchall()
        return book_data

