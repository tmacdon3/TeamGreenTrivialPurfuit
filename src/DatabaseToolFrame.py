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
        self.state_manager = state_manager
        self.database_interface = database_interface
        
        lbl_database_tool = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="Database Tool")
        btn_restore_defaults = tk.Button(master=self, text="Restore Defaults", bg=BUTTON_BG, command=self.restore_defaults_btn_command)

        lbl_remove_selected = tk.Label(master=self, bg=LABEL_BG, text="Remove Selected Item")
        btn_remove_selected = tk.Button(master=self, bg=BUTTON_BG, text="Remove", command=self.remove_item_btn_command)

        # adding a question answer combo
        lbl_add_item = tk.Label(master=self, bg=LABEL_BG, text="Add a Question")
        ent_question = tk.Entry(master=self, width=15, bg=BUTTON_BG)
        ent_question.insert(0, "Question")
        ent_answer = tk.Entry(master=self, width=15, bg=BUTTON_BG)
        ent_answer.insert(0, "Answer")
        btn_add = tk.Button(master=self, bg=BUTTON_BG, text="Add", command=self.add_item_btn_command)
        lbx_categories = tk.Listbox(master=self, height=len(CATEGORIES))
        for item in CATEGORIES:
            lbx_categories.insert(tk.END, item)
        
        lbx_colors = tk.Listbox(master=self, height=2)
        for item in ["color_1", "color_2"]:
            lbx_colors.insert(tk.END, item)
        btn_change_category_color = tk.Button(master=self, bg=BUTTON_BG, text="Change Category Color", command=self.change_category_color_btn_command)

        txt_question_display = tk.Text(master=self)
        txt_question_display.insert("1.0", "This is where questions, answers, and categories will be displayed")

        btn_back = tk.Button(master=self, text="Back", bg=BUTTON_BG, command=self.back_btn_command)
        
        # layout everything properly
        lbl_database_tool.grid(row=0, column=0, padx=x_padding, pady=y_padding)
        btn_restore_defaults.grid(row=0, column=1, padx=x_padding, pady=y_padding)

        lbl_remove_selected.grid(row=1, column=0, padx=x_padding, pady=y_padding)
        btn_remove_selected.grid(row=2, column=0, padx=x_padding, pady=y_padding)
        
        lbl_add_item.grid(row=3, column=0, padx=x_padding, pady=y_padding)
        ent_question.grid(row=4, column=0, padx=x_padding, pady=y_padding)
        ent_answer.grid(row=5, column=0, padx=x_padding, pady=y_padding)
        lbx_categories.grid(row=6, column=0, padx=x_padding, pady=y_padding)
        btn_add.grid(row=7, column=0, padx=x_padding, pady=y_padding)

        lbx_colors.grid(row=8, column=0, padx=x_padding, pady=y_padding)
        btn_change_category_color.grid(row=9, column=0, padx=x_padding, pady=y_padding)
        
        txt_question_display.grid(row=1, column=1, rowspan=10, padx=x_padding, pady=y_padding)

        btn_back.grid(row=11, column=0, padx=x_padding, pady=y_padding)

    def add_item_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Add Item Request to DatabaseInterface")
        self.database_interface.add_question_answer("question", "answer", "category")

    def remove_item_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Remove Item Request to DatabaseInterface")
        self.database_interface.remove_question_answer("question")

    def restore_defaults_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Get All Request to DatabaseInterface")
        self.database_interface.get_all_question_answers()

    def change_category_color_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending Change Category Request to DatabaseInterface")
        self.database_interface.change_category_color("category", "color")

    def back_btn_command(self):
        """
        """
        print("DatabaseToolFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)
