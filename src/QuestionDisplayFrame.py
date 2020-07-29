"""
@author: Tyler MacDonald
"""

import os
from State import State
import sys
import tkinter as tk
import tkinter.ttk as ttk

x_padding = 25
y_padding = 25

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

class QuestionDisplayFrame(ttk.Frame):

    def __init__(self, master, state_manager, database_interface):
        """
        """
        ttk.Frame.__init__(self, master=master)
        self.state_manager = state_manager
        self.database_interface = database_interface

        self.get_questions_and_answers()

        lbl_question_header = ttk.Label(master=self, font=("Verdana", 44), text="Question")
        lbl_time_limit = ttk.Label(master=self, text="Time Display")

        lbl_question_display = ttk.Label(master=self, text="Question from Database")
        self.btn_answer_one = ttk.Button(master=self, text="Answer One", command=self.highlight_question_one)
        self.btn_answer_two = ttk.Button(master=self, text="Answer Two", command=self.highlight_question_two)
        self.btn_answer_three = ttk.Button(master=self, text="Answer Three", command=self.highlight_question_three)
        self.btn_answer_four = ttk.Button(master=self, text="Answer Four", command=self.highlight_question_four)

        btn_confirm = ttk.Button(master=self, text="Confirm", command=self.confirm_btn_command)

        # configure layout stuff
        lbl_question_header.grid(row=0, column=0, padx=x_padding, pady=y_padding)
        lbl_time_limit.grid(row=0, column=1, padx=x_padding, pady=y_padding)
        lbl_question_display.grid(row=1, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        self.btn_answer_one.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_two.grid(row=3, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_three.grid(row=4, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_four.grid(row=5, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        btn_confirm.grid(row=6, column=0, columnspan=2, padx=x_padding, pady=y_padding)

    def highlight_question_one(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer One")
        self.btn_answer_one.focus_set()

    def highlight_question_two(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Two")
        self.btn_answer_two.focus_set()

    def highlight_question_three(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Three")
        self.btn_answer_three.focus_set()

    def highlight_question_four(self):
        """
        """
        print("QuestionDisplayFrame: Focus Set on Answer Four")
        self.btn_answer_four.focus_set()

    def get_questions_and_answers(self):
        """
        """
        print("QuestionDisplayFrame: Sending Request for Questions and Answers to DatabaseInterface")
        self.database_interface.get_question_answer_quadruplet("test")

    def confirm_btn_command(self):
        """
        """
        answer = self.focus_get()['text']
        print("QuestionDisplayFrame: Sending Correct/Incorrect Message to CoreGameLogic")
        print("QuestionDisplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.gameplay)
