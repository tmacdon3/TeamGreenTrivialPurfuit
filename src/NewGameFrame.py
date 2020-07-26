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

class NewGameFrame(ttk.Frame):

    def __init__(self, master, state_manager):
        """
        """
        ttk.Frame.__init__(self, master=master)
        self.state_manager = state_manager

        lbl_new_game_header = ttk.Label(master=self, font=("Verdana", 44), text="New Game")

        lbl_choose_number_of_players = ttk.Label(master=self, text="Choose Number of Players:")
        lbx_number_of_players = tk.Listbox(master=self, height=4)
        for option in ["2", "3", "4"]:
                lbx_number_of_players.insert(tk.END, option)

        btn_start_game = ttk.Button(master=self, text="Start Game", command=self.start_game_btn_command)

        lbl_new_game_header.grid(row=0, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        lbl_choose_number_of_players.grid(row=1, column=0, padx=x_padding, pady=y_padding)
        lbx_number_of_players.grid(row=1, column=1, padx=x_padding, pady=y_padding)
        btn_start_game.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)

    def start_game_btn_command(self):
        """
        """
        print("NewGameFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.gameplay)