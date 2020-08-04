"""
@author: Tyler MacDonald
"""

import os
from State import State
import sys
import tkinter as tk
    
x_padding = 25
y_padding = 10

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

CATEGORIES = ["Category_1", "Category_2", "Category_3", "Category_4"]

class DatabaseToolFrame(tk.Frame):

    def __init__(self, master, state_manager, database_interface):
        """
        """
        tk.Frame.__init__(self, bg=FRAME_BG)

        self.question_answer_list = []

        self.state_manager = state_manager
        self.database_interface = database_interface
        
        self.lbl_database_tool = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="Database Tool")
        self.btn_restore_defaults = tk.Button(master=self, text="Restore Defaults", bg=BUTTON_BG, command=self.restore_defaults_btn_command)

        self.lbl_remove_selected = tk.Label(master=self, bg=LABEL_BG, text="Remove Selected Item")
        self.ent_remove_index = tk.Entry(master=self, width=5, bg=BUTTON_BG)
        self.ent_remove_index.insert(0, "Index")
        self.btn_remove_selected = tk.Button(master=self, bg=BUTTON_BG, text="Remove", command=self.remove_item_btn_command)

        # adding a question answer combo
        self.lbl_add_item = tk.Label(master=self, bg=LABEL_BG, text="Add a Question")
        self.ent_question = tk.Entry(master=self, width=15, bg=BUTTON_BG)
        self.ent_question.insert(0, "Question")
        self.ent_answer = tk.Entry(master=self, width=15, bg=BUTTON_BG)
        self.ent_answer.insert(0, "Answer")
        self.btn_add = tk.Button(master=self, bg=BUTTON_BG, text="Add", command=self.add_item_btn_command)
        self.lbx_categories = tk.Listbox(master=self, height=len(CATEGORIES))
        for item in CATEGORIES:
            self.lbx_categories.insert(tk.END, item)
        
        self.lbx_colors = tk.Listbox(master=self, height=2)
        for item in ["color_1", "color_2"]:
            self.lbx_colors.insert(tk.END, item)
        self.btn_change_category_color = tk.Button(master=self, bg=BUTTON_BG, text="Change Category Color", command=self.change_category_color_btn_command)

        self.txt_question_display = tk.Text(master=self)
        self._initialize_display()

        self.btn_back = tk.Button(master=self, text="Back", bg=BUTTON_BG, command=self.back_btn_command)
        
        # layout everything properly
        self.lbl_database_tool.grid(row=0, column=0, padx=x_padding, pady=y_padding)
        self.btn_restore_defaults.grid(row=0, column=1, padx=x_padding, pady=y_padding)

        self.lbl_remove_selected.grid(row=1, column=0, padx=x_padding, pady=y_padding)
        self.ent_remove_index.grid(row=2, column=0, padx=x_padding, pady=y_padding)
        self.btn_remove_selected.grid(row=3, column=0, padx=x_padding, pady=y_padding)
        
        self.lbl_add_item.grid(row=4, column=0, padx=x_padding, pady=y_padding)
        self.ent_question.grid(row=5, column=0, padx=x_padding, pady=y_padding)
        self.ent_answer.grid(row=6, column=0, padx=x_padding, pady=y_padding)
        self.lbx_categories.grid(row=7, column=0, padx=x_padding, pady=y_padding)
        self.btn_add.grid(row=8, column=0, padx=x_padding, pady=y_padding)

        self.lbx_colors.grid(row=9, column=0, padx=x_padding, pady=y_padding)
        self.btn_change_category_color.grid(row=10, column=0, padx=x_padding, pady=y_padding)
        
        self.txt_question_display.grid(row=1, column=1, rowspan=10, padx=x_padding, pady=y_padding)

        self.btn_back.grid(row=11, column=0, padx=x_padding, pady=y_padding)

    def _initialize_display(self):
        """
        """
        self.txt_question_display.delete("1.0","end")
        self.question_answer_list = self.database_interface.get_all_question_answers()
        index = 0
        for row in self.question_answer_list:
            index += 1
            question = row["question"]
            answer = row["correct_answer"]
            category = row["category"]
            # add the index so we can use it later to remove/search
            row["index"] = index
            self.txt_question_display.insert(tk.END, "Index: {}\nQuestion: {}\nAnswer: {}\nCategory: {}\n\n".format(index, question, answer, category))

    def _refresh_display(self):
        """
        """
        self.txt_question_display.delete("1.0","end")
        index = 0
        for row in self.question_answer_list:
            index += 1
            question = row["question"]
            answer = row["correct_answer"]
            category = row["category"]
            # add the index so we can use it later to remove/search
            row["index"] = index
            self.txt_question_display.insert(tk.END, "Index: {}\nQuestion: {}\nAnswer: {}\nCategory: {}\n\n".format(index, question, answer, category))

    def add_item_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Add Item Request to DatabaseInterface")
        self.database_interface.add_question_answer("question", "answer", "category")
        # TODO

    def remove_item_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Remove Item Request to DatabaseInterface")
        question_to_remove = ""
        category = ""
        index = 0
        index_to_remove = -1
        for row in self.question_answer_list:
            if int(self.ent_remove_index.get()) == row["index"]:
                question_to_remove = row["question"]
                category = row["category"]
                index_to_remove = index
            index += 1
        if question_to_remove == "":
            print("Index not found!")
        else:
            self.database_interface.remove_question_answer(question_to_remove, category)
            self.question_answer_list.pop(index_to_remove)
            
            # this is a hack... we aren't actually removing it from the database...
            self._refresh_display()
            #self._initialize_display()

    def restore_defaults_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Get All Request to DatabaseInterface")
        self._initialize_display()

    def change_category_color_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Change Category Request to DatabaseInterface")
        self.database_interface.change_category_color("category", "color")
        # TODO

    def back_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)
