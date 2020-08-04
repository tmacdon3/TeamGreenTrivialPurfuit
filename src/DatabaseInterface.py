"""
@author: Tyler MacDonald

Purpose:
    Add functions to this class that abstract away the complex database details and
    allow other subsystems to interact with the database in controlled ways
    while not knowing internal details
"""
from database import Database

class DatabaseInterface():

    def __init__(self, pw=""):
        """
        """
        # this is a test
        self.db = Database("localhost", "root", pw)

    def add_question_answer(self, question, answer, category):
        """
        """
        print("DatabaseInterface: Received Request to Add Item")
        self.db.add_question_answer('test_question','test_answer','people')

    def remove_question_answer(self, question, category):
        """
        """
        print("DatabaseInterface: Received Request to Remove Item")
        self.db.remove_question_answer(question, category)

    def get_all_question_answers(self):
        """

        Return list of {'question': x, 'correct_answer': x, 'category': x}
        """
        print("DatabaseInterface: Received Request to Get All")
        return self.db.get_all_question_answers()

    def change_category_color(self, category, color):
        """
        """
        print("DatabaseInterface: Received Request to Change Category Color")
        self.db.change_category_color(category, color)

    def get_question_answer_quadruplet(self, category):
        """

        Return list of {'question': x, 'correct_answer': x, 'random_answers': []}
        """
        print("DatabaseInterface: Received Request to Get Questions and Answers")
        return self.db.get_question_answer_quadruplet('people')

    def get_category_colors(self):
        """
        """
        print("DatabaseInterface: Received Request to get category color.")
        return self.db.get_category_colors()
