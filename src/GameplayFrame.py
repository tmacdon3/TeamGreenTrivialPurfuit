"""
@author: Tyler MacDonald
"""

import os
import random
from State import State
import sys
import tkinter as tk
import tkinter.ttk as ttk


x_padding = 25
y_padding = 10

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

CATEGORIES = ["Category_1", "Category_2", "Category_3", "Category_4"]

class GameplayFrame(ttk.Frame):

    def __init__(self, master, state_manager):
        """
        """
        ttk.Frame.__init__(self)
        self.state_manager = state_manager

        # initialize matrix of cell types
        cell_btn_list = []
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
                    btn_cell = ttk.Button(master=self)

                    # layout button
                    btn_cell.grid(row=row, column=column)

                    # add to button list
                    cell_btn_list.append(btn_cell)
            matrix.append(new_row)

        # title screen button
        btn_title_screen = ttk.Button(master=self, text="Title Screen", command=self.title_screen_btn_command)
        btn_title_screen.grid(row=rows, column=0, columnspan=2, sticky="W")

        # player labels
        lbl_player_1 = ttk.Label(master=self, text="Player 1 Display")
        lbl_player_2 = ttk.Label(master=self, text="Player 2 Display")
        lbl_player_3 = ttk.Label(master=self, text="Player 3 Display")
        lbl_player_4 = ttk.Label(master=self, text="Player 4 Display")
        lbl_player_1.grid(row=rows, column=1, columnspan=3)
        lbl_player_2.grid(row=rows, column=4, columnspan=3)
        lbl_player_3.grid(row=rows, column=7, columnspan=3)
        lbl_player_4.grid(row=rows, column=10, columnspan=3)

        # roll dice button
        btn_roll_dice = ttk.Button(master=self, text="Roll Dice", command=self.roll_dice_btn_command)
        btn_roll_dice.grid(row=9, column=9, columnspan=2)

        # question button
        btn_question = ttk.Button(master=self, text="Question", command=self.question_btn_command)
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
        print("GameplayFrame: Roll Dice")

    def title_screen_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)