"""
@author: Tyler MacDonald
"""

import os
import random
from State import State
import sys
import tkinter as tk
from GameLogic import GameLogic
from GameState import GameState
    
x_padding = 25
y_padding = 10

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

CATEGORIES = ["Category_1", "Category_2", "Category_3", "Category_4"]

class GameplayFrame(tk.Frame):

    def __init__(self, master, game_logic):
        """
        """
        tk.Frame.__init__(self, bg=FRAME_BG)
        self.game_logic = game_logic
        self.state_manager = master.state_manager
        self.game_state = GameState.roll_die
        self.game_logic.player_turn()
        self.current_player = self.game_logic.get_next_player()
        self.current_die_roll = 0

        rows = len(self.game_logic.matrix)
        
        # initialize matrix of cell types from game logic
        self.cell_btn_list = []
        row_index = 0
        for row in self.game_logic.matrix:
            column_index = 0
            for value in row:
                if value != -1:
                    btn_cell = tk.Button(master=self, width=6, height=3, bg=self.get_cell_color(value))
                    btn_cell.grid(row=row_index, column=column_index)
                    self.cell_btn_list.append(btn_cell)
                column_index += 1
            row_index += 1

        # title screen button
        self.btn_title_screen = tk.Button(master=self, bg=BUTTON_BG, text="Title Screen", command=self.title_screen_btn_command)
        self.btn_title_screen.grid(row=rows, column=0, columnspan=2, sticky="W")

        # player labels
        self.lbl_player_1 = tk.Label(master=self, text="Player 1 Score: ", bg=LABEL_BG)
        self.lbl_player_2 = tk.Label(master=self, text="Player 2 Score: ", bg=LABEL_BG)
        self.lbl_player_3 = tk.Label(master=self, text="Player 3 Score: ", bg=LABEL_BG)
        self.lbl_player_4 = tk.Label(master=self, text="Player 4 Score: ", bg=LABEL_BG)
        self.lbl_player_1.grid(row=rows, column=1, columnspan=3)
        self.lbl_player_2.grid(row=rows, column=4, columnspan=3)
        self.lbl_player_3.grid(row=rows, column=7, columnspan=3)
        self.lbl_player_4.grid(row=rows, column=10, columnspan=3)

        # roll dice button
        self.btn_roll_die = tk.Button(master=self, bg=BUTTON_BG, text="Roll Dice", command=self.roll_die_btn_command)
        self.btn_roll_die.grid(row=9, column=9, columnspan=2)

        # question button
        btn_question = tk.Button(master=self, bg=BUTTON_BG, text="Question", command=self.question_btn_command)
        btn_question.grid(row=10, column=9, columnspan=2)

        # status display
        self.msg_status = tk.Message(master=self, text="Status Display", bg=LABEL_BG)
        self.msg_status.grid(row=8, column=2, columnspan=3, rowspan=3)

        self._update_status_display()

    def _update_status_display(self):
        """
        """

        if self.game_state == GameState.roll_die:
            status_message = "{} should roll the dice".format(self.current_player)
        elif self.game_state == GameState.answer_question:
            status_message = "{} should request a question".format(self.current_player)
        elif self.game_state == GameState.choose_cell:
            status_message = "{} rolled a {} and should choose a cell to move to".format(self.current_player, self.current_die_roll)
        elif self.game_state == GameState.end_game:
            status_message = "{} should choose a category".format(self.current_player)
        else:
            status_message = "Unknown GameState. HELP!"

        self.msg_status["text"] = status_message

    def get_cell_color(self, cell_type):
        return self.game_logic.get_category_color(cell_type)

    def question_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.question)

    def roll_die_btn_command(self):
        """
        """
        if self.game_state == GameState.roll_die:
            self.current_die_roll = self.game_logic.roll_die()
            self.game_state = GameState.choose_cell
            self._update_status_display()
        else:
            print("Not the correct state to roll the die")

    def title_screen_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)