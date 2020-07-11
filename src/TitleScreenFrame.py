"""
@author: Tyler MacDonald

Color Scheme:
https://coolors.co/palettes/trending
Top to Bottom colors
bg="#e76f51"
bg="#f4a261"
bg="#e9c46a"
bg="#2a9d8f"
bg="#264653"

"""

import os
import sys
import tkinter as tk

LARGE_FONT= ("Verdana", 12)
    
x_padding = (25,25)
y_padding = (25,25)

class TitleScreenFrame(tk.Frame):

    def __init__(self, master):
        """
        """
        tk.Frame.__init__(self, master=master)
        ## create first frame with team green icon
        frm_a = tk.Frame(bg="#264653")
        path_to_logo="resources" + os.path.sep + "team-green-icon.png"
        team_green_logo_image = tk.PhotoImage(file=path_to_logo)
        lbl_team_green_logo = tk.Label(master=frm_a, image=team_green_logo_image)
        lbl_team_green_logo.img = team_green_logo_image
        lbl_team_green_logo.pack(padx=x_padding, pady=y_padding)

        ## create second frame with buttons
        frm_b = tk.Frame(bg="#264653")
        btn_new_game = tk.Button(master=frm_b, text="New Game", command=self.new_game_btn_command, bg="#2a9d8f")
        btn_new_game.pack(padx=x_padding, pady=y_padding)
        btn_database_tool = tk.Button(master=frm_b, text="Database Tool", command=self.database_tool_btn_command, bg="#2a9d8f")
        btn_database_tool.pack(padx=x_padding, pady=y_padding)
        btn_quit_game = tk.Button(master=frm_b, text="Quit Game", command=self.quit_game_btn_command, bg="#2a9d8f")
        btn_quit_game.pack(padx=x_padding, pady=y_padding)

        ## create third title frame
        frm_c = tk.Frame(bg="#264653")
        lbl_game_title = tk.Label(master=frm_c, font=("Verdana", 44), bg="#2a9d8f", text="Welcome to Trivial Purfuit")
        lbl_game_title.pack(padx=x_padding, pady=y_padding)

        ## pack frames into the window
        frm_c.pack(fill=tk.BOTH, side=tk.TOP, expand=True )
        frm_a.pack(fill=tk.BOTH, side=tk.LEFT, expand=True )
        frm_b.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True )

    def database_tool_btn_command(self):
        """
        """
        print("Database Tool")

    def new_game_btn_command(self):
        """
        """
        print("New Game")

    def quit_game_btn_command(self):
        """
        """
        print("Quit Game")
        sys.exit(1)