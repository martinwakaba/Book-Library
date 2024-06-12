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
    @classmethod
    #getting a list of all books
    def get_all_books(cls, cursor):
        cursor.execute("SELECT * FROM books")
        all_books = cursor.fetchall()
        return all_books
        
    #getting books by genre
    def get_book_by_genre(self,cursor):
        cursor.execute("SELECT * FROM books WHERE genre = ?", (self._genre))
        book_data = cursor.fetchall()
        return book_data
    
    #getting book by title by author
    def get_book_by_title(self, cursor):
        cursor.execute("SELECT title FROM books WHERE author = ?", (self._author))
        book_data = cursor.fetchall()
        return book_data if book_data else None