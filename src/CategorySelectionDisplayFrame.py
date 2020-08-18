"""
@author: Tyler MacDonald
"""

import os
import random
from State import State
import sys
import tkinter as tk

x_padding = 25
y_padding = 25

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

class CategorySelectionDisplayFrame(tk.Frame):

    def __init__(self, master, gameplay_frame):
        """
        """
        tk.Frame.__init__(self, master=master, bg=FRAME_BG)
        self.state_manager = master.state_manager
        self.database_interface = master.database_interface
        self.gameplay_frame = gameplay_frame

        self.select_player = random.choice(list(self.gameplay_frame.game_logic.player_dict.keys()))

        self.category_color_dict = self.database_interface.get_category_colors()
        self.category_list = []
        self.color_list = []
        for k, v in self.category_color_dict.items():
            self.category_list.append(k)
            self.color_list.append(v)

        self.lbl_question_header = tk.Label(master=self, font=("Verdana", 36), bg=LABEL_BG, text="{} please select a category for {}".format(self.select_player, self.gameplay_frame.game_logic.current_player))

        self.btn_category_one = tk.Button(master=self, text=self.category_list[0], bg=BUTTON_BG, command=self.highlight_question_one)
        self.btn_category_two = tk.Button(master=self, text=self.category_list[1], bg=BUTTON_BG, command=self.highlight_question_two)
        self.btn_category_three = tk.Button(master=self, text=self.category_list[2], bg=BUTTON_BG, command=self.highlight_question_three)
        self.btn_category_four = tk.Button(master=self, text=self.category_list[3], bg=BUTTON_BG, command=self.highlight_question_four)
        self.btn_list = [self.btn_category_one, self.btn_category_two, self.btn_category_three, self.btn_category_four]

        self.btn_confirm = tk.Button(master=self, bg=BUTTON_BG, text="Confirm", command=self.confirm_btn_command)

        # configure layout stuff
        self.lbl_question_header.grid(row=0, column=0, padx=x_padding, pady=y_padding)

        self.btn_category_one.grid(row=1, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_category_two.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_category_three.grid(row=3, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_category_four.grid(row=4, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        self.btn_confirm.grid(row=6, column=0, columnspan=2, padx=x_padding, pady=y_padding)

    def highlight_question_one(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer One")
        self.btn_category_one.focus_set()

    def highlight_question_two(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Two")
        self.btn_category_two.focus_set()

    def highlight_question_three(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Three")
        self.btn_category_three.focus_set()

    def highlight_question_four(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Four")
        self.btn_category_four.focus_set()

    def confirm_btn_command(self):
        """
        """
        chosen_answer = self.focus_get()['text']
        self.gameplay_frame.game_logic.current_category = chosen_answer
        self.state_manager.transition_to_question(self.gameplay_frame, False)

