"""
@author: Tyler MacDonald
"""

import tkinter as tk
from TitleScreenFrame import TitleScreenFrame

class TrivialPurfuitApp(tk.Tk):

    def __init__(self):
        """
        """
        tk.Tk.__init__(self)

        #self.geometry("1024x768")

        title_screen = TitleScreenFrame(self)
        title_screen.pack()

if __name__ == "__main__":
    app = TrivialPurfuitApp()
    app.mainloop()


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