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

class QuestionDisplayFrame(tk.Frame):

    def __init__(self, master, save_state):
        """
        """
        tk.Frame.__init__(self, master=master, bg=FRAME_BG)
        self.state_manager = master.state_manager
        self.database_interface = master.database_interface

        self.save_state = save_state

        self.category = save_state.game_logic.current_category

        self._get_questions_and_answers()

        self.lbl_question_header = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="Question")
        #self.lbl_time_limit = tk.Label(master=self, bg=LABEL_BG, text="Time Display")

        self.lbl_question_display = tk.Label(master=self, bg=LABEL_BG)
        self.btn_answer_one = tk.Button(master=self, bg=BUTTON_BG, command=self.highlight_question_one)
        self.btn_answer_two = tk.Button(master=self, bg=BUTTON_BG, command=self.highlight_question_two)
        self.btn_answer_three = tk.Button(master=self, bg=BUTTON_BG, command=self.highlight_question_three)
        self.btn_answer_four = tk.Button(master=self, bg=BUTTON_BG, command=self.highlight_question_four)
        self.btn_list = [self.btn_answer_one, self.btn_answer_two, self.btn_answer_three, self.btn_answer_four]

        self.btn_confirm = tk.Button(master=self, bg=BUTTON_BG, text="Confirm", command=self.confirm_btn_command)

        # configure layout stuff
        self.lbl_question_header.grid(row=0, column=0, padx=x_padding, pady=y_padding)
        #self.lbl_time_limit.grid(row=0, column=1, padx=x_padding, pady=y_padding)
        self.lbl_question_display.grid(row=1, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        self.btn_answer_one.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_two.grid(row=3, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_three.grid(row=4, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.btn_answer_four.grid(row=5, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        self.btn_confirm.grid(row=6, column=0, columnspan=2, padx=x_padding, pady=y_padding)

        self._update_button_text()

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

    def _update_button_text(self):
        """
        """
        L1 = random.sample(range(len(self.btn_list)), len(self.btn_list))
        L2 = random.sample(range(len(self.btn_list)), len(self.btn_list))
        for index in range(len(L1)):
            btn = self.btn_list[L1[index]]
            answer = self.all_answers[L2[index]]
            btn["text"] = answer

        self.lbl_question_display["text"] = self.question

    def _get_questions_and_answers(self):
        """
        """
        print("QuestionDisplayFrame: Sending Request for Questions and Answers to DatabaseInterface")
        # TODO: Fix this so it doesn't return a ton of them
        results = self.database_interface.get_question_answer_quadruplet(self.category)[0]
        self.question = results["question"]
        self.answer = results["correct_answer"]
        self.fake_answer_list = results["random_answers"]
        self.all_answers = [self.answer] + self.fake_answer_list

    def confirm_btn_command(self):
        """
        """
        chosen_answer = self.focus_get()['text']
        if chosen_answer == self.answer:
            print("correct: {} == {}".format(chosen_answer, self.answer))
            self.save_state.game_logic.answered_correctly = True
            self.save_state.game_logic.update_score()
            self.save_state.game_logic.update_player_data()
            self.state_manager.transition_to_gameplay_from_question()
        else:
            print("incorrect: {} != {}".format(chosen_answer, self.answer))
            self.save_state.game_logic.answered_correctly = False
            self.save_state.game_logic.update_player_data()
            self.state_manager.transition_to_gameplay_from_question()
