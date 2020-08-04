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
        
        # initialize matrix of cell types
        cell_btn_list = []

        print(self.game_logic.matrix)

        rows = 13
        columns = 13
        matrix = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                if row == 0 or column == 0 or row == rows-1 or column == columns-1 or row == int(rows / 2) or column == int(columns / 2):
                    cell_type = random.randint(0,3)
                    new_row.append(cell_type)

                    # create button
                    color = self.get_cell_color(cell_type)
                    btn_cell = tk.Button(master=self, width=6, height=3, bg=color)

                    # layout button
                    btn_cell.grid(row=row, column=column)

                    # add to button list
                    cell_btn_list.append(btn_cell)
            matrix.append(new_row)

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
        if cell_type == 0:
            return 'red'
        elif cell_type == 1:
            return 'blue'
        elif cell_type == 2:
            return 'green'
        elif cell_type == 3:
            return 'white'
        else:
            return 'black'

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