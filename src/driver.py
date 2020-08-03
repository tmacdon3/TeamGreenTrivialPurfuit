
from database import Database

def main():
    db = Database('localhost', 'root', '')
    db.create_database()
    # db.show_database()
    db.create_tables()
    db.insert_data()
    # db.show_tables()
    # db.display_all_questions()
    # data = db.get_all_question_answers()
    # data = db.get_question_answer_quadruplet('people')
    # db.change_category_color('people', 'yellow')
    # db.add_question_answer('sup','supper','people')
    # db.remove_question_answer('sup', 'people')
    # print(db.get_category_colors())



if __name__ == '__main__':
    main()
