
from database import Database

def main():
    db = Database('localhost', 'root', '')
    db.create_database()
    db.show_database()
    db.create_tables()
    db.display_all_questions()

if __name__ == '__main__':
    main()
