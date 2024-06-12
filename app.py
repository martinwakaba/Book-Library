from database.connection import db_connection
from database.setup import create_tables

def main():
    
    create_tables()

if __name__ == "__main__":
    main()
