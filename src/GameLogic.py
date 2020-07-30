"""
@author: Joseph Aulds
"""
import random
import numpy as np
from State import State
from DatabaseInterface import DatabaseInterface


class GameLogic():
    def __init__(self,
                ):
  
        self.player_iterator = 0
        self.next_player = ""
        self.database_interface = DatabaseInterface()
        
        
    def new_game(self):   
        # self.category_colors = 
        self.database_interface.get_category_colors()

        # initialize matrix of cell types
        # cell_btn_list = []
        rows = 13
        columns = 13
        self.matrix = []
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
            self.matrix.append(new_row)
        # for i in self.matrix:
        #     print(i)
        #     for j in self.matrix:
        #         print(j)

        

    def roll_die(self):
        return random.randint(1,6)

    def player_order(self, 
                    num_players):
        self.num_players = num_players
        self.order = np.array([0] * 4)
        for i in range(self.num_players):
            self.order[i] = self.roll_die()
        self.max = self.order.argmax()

        first_player = "Player" + str(self.max+1)
        print(first_player + " goes first")
        players = ["Player1", "Player2", "Player3", "Player4"]

        for i in range(num_players):
            if first_player == players[i]:
                temp = players[0]
                players[0] = players[i]
                players[i] = temp
        self.player_list = players[0:num_players]
        
        #initialize player classes for the number of players
        # for i, player in enumerate(self.player_list):
        """
        @TODO dynamically make the correct number of player class instances :(
        """
            

        
            



    def player_turn(self):    
        if (self.player_iterator + 1) >= self.num_players:
            self.player_iterator = 0
            self.next_player = self.player_list[self.player_iterator]
        else:
            self.player_iterator += 1
            self.next_player = self.player_list[self.player_iterator]

    def get_player_order(self):
        return self.player_list        
    
    def get_matrix(self):
        return self.matrix

    def get_next_player(self):
        return self.next_player



class Player():
    def __init__(self):
             self.position = [0][0]
             self.score = 0

    def set_position(self, new_position):
        self.position = new_position

    def set_score(self, new_score):
        self.score = new_score

    def get_position(self):
        return self.position
    
    def get_score(self):
        return self.score




if __name__ == "__main__":
    
    gl = GameLogic()
    gl.new_game()
    gl.player_order(4)

    
    for i in range(6):
        gl.player_turn()
        print(gl.get_next_player())
    print(gl.get_player_order())