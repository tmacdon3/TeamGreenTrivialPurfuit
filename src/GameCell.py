"""
@author: Tyler MacDonald
"""

import tkinter as tk

class GameCell(tk.Button):

    def __init__(self, game_frame, color, width, height, category, row, column):
        """
        """
        tk.Button.__init__(self, master=game_frame, width=width, height=height, bg=color, command=self._send_coordinates_to_game_frame)

        self.game_frame = game_frame
        self.row = row
        self.column = column
        self.category = category

        self.player_list = []

    def add_player(self, player):
        """
        """
        self.player_list.append(player)
        self._update_display()

    def remove_player(self, player):
        """
        """
        self.player_list.remove(player)
        self._update_display()

    def _update_display(self):
        """
        """
        text = ""
        for player in self.player_list:
            text += player + ","
        text = text[:-1]
        self.configure(text=text)

    def _send_coordinates_to_game_frame(self):
        """
        """
        self.game_frame.button_was_clicked(self.row, self.column)