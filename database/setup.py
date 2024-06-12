from .connection import db_connection

def create_tables():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            publication_date DATE
            author TEXT ,
            genre TEXT NOT NULL           
                   
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number INT NOT NULL         
                   
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookscheckout (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            book_id TEXT,
            genre TEXT,
            checkout_date DATE,
            checkin_date DATE,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (book_id) REFERENCES books (id)            
                   
        )
    ''')

    conn.commit()
    conn.close()