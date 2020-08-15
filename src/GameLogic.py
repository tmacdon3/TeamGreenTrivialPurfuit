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
        self.current_player = ""
        self.database_interface = database_interface
        self.matrix = []
        # value when it's not a cell
        self.default_matrix_value = -1
        
        self.roll_again_index = 4
        self.roll_again_identifier = "roll_again"

        # store this so we don't have to keep reaching out to db
        self.category_color_dict = self.database_interface.get_category_colors()
        
        # maintain a list so we can use matrix numbers as indices
        self.category_list = []
        for k in self.category_color_dict.keys():
            self.category_list.append(k)

        # also add roll again to the category list
        self.category_color_dict[self.roll_again_identifier] = "#fffd80"
        self.category_list.append(self.roll_again_identifier)

        self.player_dict = {}

        self.current_category = None
        self.answered_correctly = None

        self.win_game = False
        
    # This method generates the matrix for the gameboard 
    def new_game(self):   
        rows = 13
        columns = 13

        # maintain index lists just for ease of adding roll-again squares later on
        valid_indices = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                if row == 0 or column == 0 or row == rows-1 or column == columns-1 or row == int(rows / 2) or column == int(columns / 2):
                    # minus 2 to make sure we don't get roll agains
                    cell_type = random.randint(0, len(self.category_list)-2)
                    new_row.append(cell_type)
                    valid_indices.append([row, column])
                else:
                    # just append default if it's not a cell with a button
                    new_row.append(self.default_matrix_value)

            self.matrix.append(new_row)

        # now loop through and add 4 random roll-again squares
        num_roll_again_squares = 4
        for i in range(num_roll_again_squares):
            index = random.choice(valid_indices)
            self.matrix[index[0]][index[1]] = self.roll_again_index

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

        first_player = "p" + str(self.max+1)
        players = ["p1", "p2", "p3", "p4"]

        for i in range(num_players):
            if first_player == players[i]:
                temp = players[0]
                players[0] = players[i]
                players[i] = temp
        self.player_list = players[0:num_players]
        
        #initialize player classes for the number of players
        # for i, player in enumerate(self.player_list):

        self.player_dict = {}
        for i in range(num_players):
            j = i + 1
            self.player_dict["p{}".format(j)] = Player()


    # Update player position
    def update_position(self, player, new_position):
        self.player_dict[player].set_position(new_position)

    """
    Score is updated as follows:
    a = "holiday"
    b = "people"
    c = "events"
    d = "places"

    for instance if a player had correctly answered people and places,
    their score would be "bd"
    """
    def update_score(self):
        player = self.current_player
        if len(self.player_dict[player].get_score()) == 4 and self.player_dict[player].get_position() == (6,6):
            self.win_game = True
        else:
            category = self.current_category
            if category == "people":
                self.player_dict[player].add_score("b")
            elif category == "holiday":
                self.player_dict[player].add_score("a")
            elif category == "events":
                self.player_dict[player].add_score("c")
            elif category == "places":
                self.player_dict[player].add_score("d")

    # Determines which player shall go next.
    def player_turn(self):
        # it's the same player if it was answered correctly
        if self.answered_correctly == False or self.answered_correctly == None:
            if (self.player_iterator + 1) >= self.num_players:
                self.player_iterator = 0
                self.current_player = self.player_list[self.player_iterator]
            else:
                self.player_iterator += 1
                self.current_player = self.player_list[self.player_iterator]

    def update_player_data(self):
        self.player_dict[self.current_player].update_score_matrix(self.current_category, self.answered_correctly)

    # Returns the list of player order
    def get_player_order(self):
        return self.player_list        
    
    # Returns the gameplay matrix
    def get_matrix(self):
        return self.matrix

    # Returns the play whose turn is next
    def get_current_player(self):
        return self.current_player

    def get_category_color(self, index):
        """Use the number index in the matrix to get a color
        """
        return self.category_color_dict[self.category_list[index]]

    def get_player_position(self, player):
        """
        """
        return self.player_dict[player].get_position()

    def get_player_score(self, player):
        """
        """
        return self.player_dict[player].get_score()


# This class shall be instantiated x number of times, where x is the number of players

class Player(GameLogic):
    def __init__(self):
        # TODO don't make this hardcoded
        self.position = (6,6)
        self.score = ""
        self.score_matrix = np.array([["category", "correct", "incorrect"], ["people", 0, 0], ["holiday", 0, 0], ["events", 0, 0], ["places", 0, 0]])

    def set_position(self, new_position):
        self.position = new_position

    def add_score(self, score):
        if score not in self.score:
            self.score += score
        # sort it so they all look in order
        self.score = sorted(self.score)

    def update_score_matrix(self, category, correct_answer):
        if category == "people":
            if correct_answer == True:
                self.score_matrix[1][1] = int(self.score_matrix[1][1]) + 1
            else:
                self.score_matrix[1][2] = int(self.score_matrix[1][2]) + 1
        elif category == "holiday":
            if correct_answer == True:
                self.score_matrix[2][1] = int(self.score_matrix[2][1]) + 1
            else:
                self.score_matrix[2][2] = int(self.score_matrix[2][2]) + 1
        elif category == "events":
            if correct_answer == True:
                self.score_matrix[3][1] = int(self.score_matrix[3][1]) + 1
            else:
                self.score_matrix[3][2] = int(self.score_matrix[3][2]) + 1
        elif category == "places":
            if correct_answer == True:
                self.score_matrix[4][1] = int(self.score_matrix[4][1]) + 1
            else:
                self.score_matrix[4][2] = int(self.score_matrix[4][2]) + 1
        print(self.score_matrix)

    def get_position(self):
        return self.position
    
    def get_score(self):
        return self.score
    
    def get_score_matrix(self):
        return self.score_matrix




if __name__ == "__main__":
    
    db = DatabaseInterface(input("pw:"))
    gl = GameLogic(db)
    gl.new_game()
    gl.player_order(4)

    
    for i in range(6):
        gl.player_turn()
        print(gl.get_current_player())
    print(gl.get_player_order())

    score = "bcda"
    if "a" in score and "b" in score and "c" in score and "d" in score:
        print("FOUND string!!")
    else:
        print("Didn't find string... :(")