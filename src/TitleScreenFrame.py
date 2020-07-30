"""
@author: Tyler MacDonald
"""

import os
from State import State
import sys
import tkinter as tk
from PIL import Image
from PIL.ImageTk import PhotoImage

LARGE_FONT= ("Verdana", 12)

x_padding = 25
y_padding = 25

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

class TitleScreenFrame(tk.Frame):

    def __init__(self, master, state_manager):
        """
        """
        tk.Frame.__init__(self, master=master, bg=FRAME_BG)
        self.state_manager = state_manager

        ## create first frame with team green icon
        path_to_logo="resources" + os.path.sep + "team-green-icon.png"
        team_green_logo_image = self._load_image(path_to_logo)
        lbl_team_green_logo = tk.Label(master=self, image=team_green_logo_image)
        lbl_team_green_logo.img = team_green_logo_image

        ## create second frame with buttons
        btn_new_game = tk.Button(master=self, text="New Game", command=self.new_game_btn_command, bg=BUTTON_BG)
        btn_database_tool = tk.Button(master=self, text="Database Tool", command=self.database_tool_btn_command, bg=BUTTON_BG)
        btn_quit_game = tk.Button(master=self, text="Quit Game", command=self.quit_game_btn_command, bg=BUTTON_BG)

        ## create third title frame
        lbl_game_title = tk.Label(master=self, font=("Verdana", 44), bg=LABEL_BG, text="Welcome to Trivial Purfuit")

        # layout properly
        lbl_game_title.grid(row=0, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        lbl_team_green_logo.grid(row=1, column=0, rowspan=3, padx=x_padding, pady=y_padding)
        btn_new_game.grid(row=1, column=1, padx=x_padding, pady=y_padding)
        btn_database_tool.grid(row=2, column=1, padx=x_padding, pady=y_padding)
        btn_quit_game.grid(row=3, column=1, padx=x_padding, pady=y_padding)

    def _load_image(self, path_to_image):
        """
        """
        image = Image.open(path_to_image)
        return PhotoImage(image)

    def database_tool_btn_command(self):
        """
        """
        print("TitleScreenFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.database_tool)

    def new_game_btn_command(self):
        """
        """
        print("TitleScreenFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.new_game)

    def quit_game_btn_command(self):
        """
        """
        print("TitleScreenFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.quit)
