"""
@author: Tyler MacDonald

Purpose:
    Add functions to this class that abstract away the complex database details and 
    allow other subsystems to interact with the database in controlled ways 
    while not knowing internal details
"""

class DatabaseInterface():

    def __init__(self):
        """
        """
        pass

    def add_question_answer(self, question, answer, category):
        """
        """
        print("DatabaseInterface: Received Request to Add Item")

    def remove_question_answer(self, question):
        """
        """
        print("DatabaseInterface: Received Request to Remove Item")

    def get_all_question_answers(self):
        """

        Return list of {'question': x, 'answer': x, 'category': x}
        """
        print("DatabaseInterface: Received Request to Get All")

    def change_category_color(self, category, color):
        """
        """
        print("DatabaseInterface: Received Request to Change Category Color")

    def get_category_colors(self):
        """
        """
        print("DatabaseInterface: Received Request to Get Category Colors")

    def get_question_answer_quadruplet(self, category):
        """

        Return list of {'question': x, 'correct_answer': x, 'random_answers': []}
        """
        print("DatabaseInterface: Received Request to Get Questions and Answers")