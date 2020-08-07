
from database import Database

def main():
    db = Database('localhost', 'root', '')
    # db.show_tables()
    # db.display_all_questions()
    # data = db.get_all_question_answers()
    db.change_category_color('people', 'yellow')
    print(db.get_category_colors())


if __name__ == '__main__':
    main()
