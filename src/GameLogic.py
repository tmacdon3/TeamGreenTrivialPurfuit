"""
@author: Joseph Aulds
"""
import random
from State import State
from DatabaseInterface import DatabaseInterface

import numpy as np

class GameLogic():
    def __init__(self,
                ):
  
        """
        """
        pass
        
    def new_game(self,
                ): 
        self.database_interface = DatabaseInterface()

        # self.category_colors = 
        self.database_interface.get_category_colors()

        # initialize matrix of cell types
        # cell_btn_list = []
        rows = 13
        columns = 13
        matrix = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                if row == 0 or column == 0 or row == rows-1 or column == columns-1 or row == int(rows / 2) or column == int(columns / 2):
                    cell_type = random.randint(0,3)
                    new_row.append(cell_type)

                    # # create button
                    # color = self.get_cell_color(cell_type)
                    # btn_cell = tk.Button(master=self, width=6, height=3, bg=color)

                    # # layout button
                    # btn_cell.grid(row=row, column=column)

                    # # add to button list
                    # cell_btn_list.append(btn_cell)
            matrix.append(new_row)
        for i in matrix:
            print(i)
            for j in matrix:
                print(j)

        

    def roll_die(self):
        return random.randint(1,6)

    def player_order(self, 
                    num_players):
        self.num_players = num_players
        self.order = np.array([0] * 4)
        for i in range(self.num_players):
            self.order[i] = self.roll_die()
        self.max = self.order.argmax()
        print("Player" + str(self.max + 1) + " goes first")

class Player():
    def __init__(self,
             position,
             score,
             ):
             self.position = position




if __name__ == "__main__":
    
    gl = GameLogic()
    gl.new_game()