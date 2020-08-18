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

class StatisticsDisplayFrame(tk.Frame):

    def __init__(self, master, game_logic):
        """
        """
        tk.Frame.__init__(self, master=master, bg=FRAME_BG)
        self.state_manager = master.state_manager
        self.game_logic = game_logic

        prize = random.choice(["Gold Star", "Pot of Gold", "High Five", "Pat on the Back"])
        self.lbl_statistics_header = tk.Label(master=self, font=("Verdana", 36), bg=LABEL_BG, text="Congratulations {}! You have won the game and a {}!".format(self.game_logic.current_player, prize))

        self.txt_statistics_display = tk.Text(master=self)

        self._update_statistics_display()

        self.btn_title_screen = tk.Button(master=self, bg=BUTTON_BG, text="Title Screen", command=self.title_btn_command)

        # configure layout stuff
        self.lbl_statistics_header.grid(row=0, column=0, padx=x_padding, pady=y_padding)

        self.txt_statistics_display.grid(row=1, column=0, columnspan=2)

        self.btn_title_screen.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)

    def _update_statistics_display(self):
        """
        """
        for k, v in self.game_logic.player_dict.items():
            self.txt_statistics_display.insert(tk.END, "{}:\n".format(k))
            score_matrix = v.get_score_matrix()
            index = 0
            for row in score_matrix:
                if index != 0:
                    self.txt_statistics_display.insert(tk.END, "\tCategory: {}\n\tCorrect: {}\n\tIncorrect: {}\n\n".format(row[0], row[1], row[2]))
                    index += 1
                else:
                    index += 1
            
            #self.txt_question_display.insert(tk.END, "Index: {}\nQuestion: {}\nAnswer: {}\nCategory: {}\n\n".format(index, question, answer, category))

    def title_btn_command(self):
        """
        """
        self.state_manager.transition_state(State.title_screen)
