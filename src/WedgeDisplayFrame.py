"""
@author: Tyler MacDonald
"""

import tkinter as tk

class WedgeDisplayFrame(tk.Frame):

    def __init__(self, master, player):
        """
        """
        tk.Frame.__init__(self, master)

        self.lbl_player = tk.Label(self, text=player)

        self.btn_wedge_1 = tk.Button(self)
        self.btn_wedge_2 = tk.Button(self)
        self.btn_wedge_3 = tk.Button(self)
        self.btn_wedge_4 = tk.Button(self)
        self.btn_wedge_list = [self.btn_wedge_1, self.btn_wedge_2, self.btn_wedge_3, self.btn_wedge_4]

        # layout
        self.lbl_player.grid(row=0, column=0, columnspan=2, sticky="news")
        self.btn_wedge_1.grid(row=1, column=0, sticky="news")
        self.btn_wedge_2.grid(row=1, column=1, sticky="news")
        self.btn_wedge_3.grid(row=2, column=0, sticky="news")
        self.btn_wedge_4.grid(row=2, column=1, sticky="news")

    def update_wedge_from_score(self, score):
        """
        """
        if "a" in score:
            self.btn_wedge_1.configure(bg="green")
        elif "b" in score:
            self.btn_wedge_2.configure(bg="red")
        elif "c" in score:
            self.btn_wedge_3.configure(bg="white")
        elif "d" in score:
            self.btn_wedge_4.configure(bg="blue")