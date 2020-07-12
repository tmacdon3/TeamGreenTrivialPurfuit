"""
@author: Tyler MacDonald
"""

from DatabaseInterface import DatabaseInterface
from DatabaseToolFrame import DatabaseToolFrame
from StateManager import StateManager
import sys
import tkinter as tk
from TitleScreenFrame import TitleScreenFrame
from QuestionDisplayFrame import QuestionDisplayFrame

class TrivialPurfuitApp(tk.Tk):

    def __init__(self):
        """
        """
        tk.Tk.__init__(self)

        self.title("Team Green's Trivial Purfuit")

        # window resolution
        # self.geometry("1024x768")

        self.state_manager = StateManager(self)
        self.database_interface = DatabaseInterface()

        self.active_frame = TitleScreenFrame(self, self.state_manager)
        self.active_frame.pack()

    def switch_frame(self, new_frame):
        self.active_frame.destroy()
        self.active_frame = new_frame
        self.active_frame.pack()

if __name__ == "__main__":
    app = TrivialPurfuitApp()
    app.mainloop()


# this is some template code for switching between frames
"""
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = TitleScreen(container, self)
        self.frames[TitleScreen] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(TitleScreen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        """