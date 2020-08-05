"""
@author: Tyler MacDonald
"""

from GameLogic import GameLogic
import os
from SaveState import SaveState
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

class NewGameFrame(tk.Frame):

    def __init__(self, master):
        """
        """
        tk.Frame.__init__(self, master=master, bg=FRAME_BG)
        self.master = master
        self.state_manager = master.state_manager
        self.lbl_new_game_header = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="New Game")

        self.lbl_choose_number_of_players = tk.Label(master=self, bg=LABEL_BG, text="Choose Number of Players:")
        self.lbx_number_of_players = tk.Listbox(master=self, height=4)
        for option in ["2", "3", "4"]:
                self.lbx_number_of_players.insert(tk.END, option)

        self.btn_start_game = tk.Button(master=self, bg=BUTTON_BG, text="Start Game", command=self.start_game_btn_command)

        self.lbl_new_game_header.grid(row=0, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        self.lbl_choose_number_of_players.grid(row=1, column=0, padx=x_padding, pady=y_padding)
        self.lbx_number_of_players.grid(row=1, column=1, padx=x_padding, pady=y_padding)
        self.btn_start_game.grid(row=2, column=0, columnspan=2, padx=x_padding, pady=y_padding)

    def start_game_btn_command(self):
        """
        """
        print("NewGameFrame: Sending State Transition Request to StateManager")
        self.game_logic = GameLogic(self.master.database_interface)
        self.game_logic.new_game()
        num_players = int(self.lbx_number_of_players.get(self.lbx_number_of_players.curselection()))
        self.game_logic.player_order(num_players)
        
        save_state = SaveState(self.game_logic)

        self.state_manager.transition_to_gameplay(save_state)