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

    def add_item(self):
        """
        """
        print("DatabaseInterface: Received Request to Add Item")

    def remove_item(self):
        """
        """
        print("DatabaseInterface: Received Request to Remove Item")

    def get_all(self):
        """
        """
        print("DatabaseInterface: Received Request to Get All")

    def change_category_color(self):
        """
        """
        print("DatabaseInterface: Received Request to Change Category Color")

    def get_question_and_answers(self):
        """
        """
        print("DatabaseInterface: Received Request to Get Questions and Answers")