"""
@author: Tyler MacDonald
"""

import os
import random
from State import State
import sys
import tkinter as tk
from GameLogic import GameLogic
    
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
        self.game_logic = game_logic
        tk.Frame.__init__(self, bg=FRAME_BG)
        self.state_manager = master.state_manager

        rows = len(self.game_logic.matrix)
        
        # initialize matrix of cell types from game logic
        cell_btn_list = []
        row_index = 0
        for row in self.game_logic.matrix:
            column_index = 0
            for value in row:
                if value != -1:
                    btn_cell = tk.Button(master=self, width=6, height=3, bg=self.get_cell_color(value))
                    btn_cell.grid(row=row_index, column=column_index)
                    cell_btn_list.append(btn_cell)
                column_index += 1
            row_index += 1

        # title screen button
        btn_title_screen = tk.Button(master=self, bg=BUTTON_BG, text="Title Screen", command=self.title_screen_btn_command)
        btn_title_screen.grid(row=rows, column=0, columnspan=2, sticky="W")

        # player labels
        lbl_player_1 = tk.Label(master=self, text="Player 1 Display", bg=LABEL_BG)
        lbl_player_2 = tk.Label(master=self, text="Player 2 Display", bg=LABEL_BG)
        lbl_player_3 = tk.Label(master=self, text="Player 3 Display", bg=LABEL_BG)
        lbl_player_4 = tk.Label(master=self, text="Player 4 Display", bg=LABEL_BG)
        lbl_player_1.grid(row=rows, column=1, columnspan=3)
        lbl_player_2.grid(row=rows, column=4, columnspan=3)
        lbl_player_3.grid(row=rows, column=7, columnspan=3)
        lbl_player_4.grid(row=rows, column=10, columnspan=3)

        # roll dice button
        btn_roll_dice = tk.Button(master=self, bg=BUTTON_BG, text="Roll Dice", command=self.roll_dice_btn_command)
        btn_roll_dice.grid(row=9, column=9, columnspan=2)

        # question button
        btn_question = tk.Button(master=self, bg=BUTTON_BG, text="Question", command=self.question_btn_command)
        btn_question.grid(row=10, column=9, columnspan=2)

    def get_cell_color(self, cell_type):
        return self.game_logic.get_category_color(cell_type)

    def question_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.question)

    def roll_dice_btn_command(self):
        """
        """
        
        print(self.game_logic.roll_die())
        print("GameplayFrame: Roll Dice")

    def title_screen_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)