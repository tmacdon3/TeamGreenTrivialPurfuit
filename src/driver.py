
from database import Database

import sys

def main():
    db = Database('localhost', 'root', sys.argv[1])
    
    print("DROP DATABASE")
    #db.drop_database()
    
    print("CREATE DATABASE")
    #db.create_database()
    
    print("SHOW DATABASE")
    #db.show_database()
    
    print("CREATE TABLES")
    #db.create_tables()
    
    print("SHOW TABLES")
    #db.show_tables()

    print("INSERT DATA")
    #db.insert_data()

    #print("DISPLAY ALL QUESTIONS")
    #print(db.display_all_questions())

    print("GET ALL QUESTION ANSWERS")
    #data = db.get_all_question_answers()
    #print(data)
    # data = db.get_question_answer_quadruplet('people')
    # db.change_category_color('people', 'yellow')
    db.add_question_answer('sup','supper','people')
    #db.remove_question_answer('sup', 'people')
    # print(db.get_category_colors())



if __name__ == '__main__':
    main()
