class Book:
    def __init__(self, id, title, publication_date, author, genre) :
        self._id = id
        self._title = title
        self._publication_date = publication_date
        self._author = author
        self._genre = genre

    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,  value):
        if isinstance(value) != "":
            self._title = value
        else:
            raise ValueError("Title cannot be empty!!!")    
        
    
    
    @property
    def publication_date(self):
        return self._publication_date
    
    @publication_date.setter
    def publication_date(self,  value):
        if isinstance(value) != "":
            self._publication_date = value
        else:
            raise ValueError("Publication Date cannot be empty!!!")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,  value):
        if isinstance(value, str) != "":
            self._author = value
        else:
            raise ValueError("Author cannot be empty!!!")
    
    @property
    def genre(self):
        return self._genre
    
    #adding books
    def add_book(self, cursor):
        cursor.execute("INSERT INTO books (title, publication_date, author, genre) VALUES (?, ?, ?, ?)", (self._title, self._publication_date, self._author, self._genre))
        self._id = cursor
        return cursor
    
    #getting a list of all books
    @classmethod
    def get_all_books(cls, cursor):
        cursor.execute("SELECT * FROM books")
        all_books = cursor.fetchall()
        return [cls(id=row[0], title=row[1], publication_date=row[2], author=row[3], genre=row[4]) for row in all_books]
        
    #getting books by genre
    @classmethod
    def get_book_by_genre(cls,cursor, genre):
        cursor.execute("SELECT * FROM books WHERE genre = ? OR  title = ?", (genre,))
        book_data = cursor.fetchall()
        return cls(id=book_data[0], title=book_data[1], publication_date=book_data[2], author=book_data[3], genre=book_data[4]) if book_data else None

    
    #getting book by title by author
    @classmethod
    def get_book_by_author(cls, cursor, author):
        cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
        book_data = cursor.fetchall()
        return [cls(id=row[0], title=row[1], publication_date=row[2], author=row[3], genre=row[4]) for row in book_data]

    
    #getting book status
    def book_availability(self, cursor):
        cursor.execute("""
            SELECT COUNT(*)
            FROM bookscheckout
            WHERE book_id = ? AND checkout_date IS NOT NULL AND checkin_date IS NULL
        """, (self._id,))
        result = cursor.fetchone()
        return result[0] == 0  # Return True if no active checkouts, False otherwise