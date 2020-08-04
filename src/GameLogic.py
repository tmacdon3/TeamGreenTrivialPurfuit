"""
@author: Joseph Aulds
"""
import random
import numpy as np
from State import State
from DatabaseInterface import DatabaseInterface


class GameLogic():
    def __init__(self, database_interface):
  
        self.player_iterator = 0
        self.next_player = ""
        self.database_interface = database_interface
        self.matrix = []
        # value when it's not a cell
        self.default_matrix_value = -1

        # store this so we don't have to keep reaching out to db
        self.category_color_dict = self.database_interface.get_category_colors()
        
        # maintain a list so we can use matrix numbers as indices
        self.category_list = []
        for k in self.category_color_dict.keys():
            self.category_list.append(k)
        
    # This method generates the matrix for the gameboard 
    def new_game(self):   
        rows = 13
        columns = 13
        for row in range(rows):
            new_row = []
            for column in range(columns):
                if row == 0 or column == 0 or row == rows-1 or column == columns-1 or row == int(rows / 2) or column == int(columns / 2):
                    cell_type = random.randint(0, len(self.category_list)-1)
                    new_row.append(cell_type)
                else:
                    # just append default if it's not a cell with a button
                    new_row.append(self.default_matrix_value)

            self.matrix.append(new_row)

    # This method rolls the die for choosing who goes first and for gameplay
    def roll_die(self):
        return random.randint(1,6)

    # This method determines who shall go first, and then update the player list for next player
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

        self.p1 = Player()
        self.p2 = Player()
        self.p3 = Player()
        self.p4 = Player()

        self.update_position("p2", (9,19))
        self.update_position("p1", (5, 15))
        self.update_score("p1", "ac")
        self.update_score("p2", "acbd")
        print(self.get_all_players_positions())
        print(self.get_all_players_scores())


    # Update player position
    def update_position(self, player, new_position):
        if player == "p1":
            self.p1.set_position(new_position)
        elif player == "p2":
            self.p2.set_position(new_position)
        elif player == "p3":
            self.p3.set_position(new_position)
        elif player == "p4":
            self.p4.set_position(new_position)

    """
    Score is updated as follows:
    a = "Declaration of Independence and Continental Congress"
    b = "people"
    c = "events"
    d = "places"

    for instance if a player had correctly answered people and places,
    their score would be "bd"
    """
    def update_score(self, player, new_score):
        if player == "p1":
            self.p1.set_score(new_score)
        elif player == "p2":
            self.p2.set_score(new_score)
        elif player == "p3":
            self.p3.set_score(new_score)
        elif player == "p4":
            self.p4.set_score(new_score)     

            
    # Determines which player shall go next.
    def player_turn(self):    
        if (self.player_iterator + 1) >= self.num_players:
            self.player_iterator = 0
            self.next_player = self.player_list[self.player_iterator]
        else:
            self.player_iterator += 1
            self.next_player = self.player_list[self.player_iterator]

    # Returns the list of player order
    def get_player_order(self):
        return self.player_list        
    
    # Returns the gameplay matrix
    def get_matrix(self):
        return self.matrix

    # Returns the play whose turn is next
    def get_next_player(self):
        return self.next_player

    def get_category_color(self, index):
        """Use the number index in the matrix to get a color
        """
        print("looking for {}".format(index))
        return self.category_color_dict[self.category_list[index]]
    
    def get_all_players_scores(self):
        return self.p1.get_score(), self.p2.get_score(), self.p3.get_score(), self.p4.get_score()

    def get_all_players_positions(self):
        return self.p1.get_position(), self.p2.get_position(), self.p3.get_position(), self.p4.get_position()


# This class shall be instantiated x number of times, where x is the number of players

class Player(GameLogic):
    def __init__(self):
             self.position = (0,0)
             self.score = ""

    def set_position(self, new_position):
        self.position = new_position

    def set_score(self, new_score):
        self.score = new_score

    def get_position(self):
        return self.position
    
    def get_score(self):
        return self.score




if __name__ == "__main__":
    
    db = DatabaseInterface(input("pw:"))
    gl = GameLogic(db)
    gl.new_game()
    gl.player_order(4)

    
    for i in range(6):
        gl.player_turn()
        print(gl.get_next_player())
    print(gl.get_player_order())

    score = "bcda"
    if "a" in score and "b" in score and "c" in score and "d" in score:
        print("FOUND string!!")
    else:
        print("Didn't find string... :(")