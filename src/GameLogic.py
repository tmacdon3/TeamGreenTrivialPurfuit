"""
@author: Joseph Aulds
"""
import random
from State import State
from StateManager import StateManager

class GameLogic():
    def __init__(self,
                state_manager):
        self.state_manager = state_manager
        
        


    def new_game(self,
                num_players,
                category_colors): 
        self.num_players = num_players
        for i in range(num_players):
            print("Player " + str(i+1) + " rolled " + str(self.roll_die()))

    def roll_die(self):
        return random.randint(1,6)


class Player():
    def __init__(self,
             position,
             score,
             ):
             self.position = position




