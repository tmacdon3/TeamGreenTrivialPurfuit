import os
import sys
import tkinter as tk

LARGE_FONT= ("Verdana", 12)

x_padding = 25
y_padding = 25

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

class QuestionDisplayFrame(tk.Frame):

    def __init__(self, master):
        """
        """
        tk.Frame.__init__(self, master=master, bg="#264653")

        lbl_question_header = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="Question")
        lbl_time_limit = tk.Label(master=self, bg=LABEL_BG, text="Time Display")

        lbl_question_display = tk.Label(master=self, bg=LABEL_BG, text="Question from Database")
        self.btn_answer_one = tk.Button(master=self, bg=BUTTON_BG, text="Answer One", command=self.highlight_question_one)
        self.btn_answer_two = tk.Button(master=self, bg=BUTTON_BG, text="Answer Two", command=self.highlight_question_two)
        self.btn_answer_three = tk.Button(master=self, bg=BUTTON_BG, text="Answer Three", command=self.highlight_question_three)
        self.btn_answer_four = tk.Button(master=self, bg=BUTTON_BG, text="Answer Four", command=self.highlight_question_four)

        btn_confirm = tk.Button(master=self, bg=BUTTON_BG, text="Confirm", command=self.confirm_btn_command)

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
        self.btn_answer_one.focus_set()

    def highlight_question_two(self):
        """
        """
        self.btn_answer_two.focus_set()

    def highlight_question_three(self):
        """
        """
        self.btn_answer_three.focus_set()

    def highlight_question_four(self):
        """
        """
        self.btn_answer_four.focus_set()

    def confirm_btn_command(self):
        """
        """
        print("Confirm Button: {}".format(self.focus_get()['text']))
