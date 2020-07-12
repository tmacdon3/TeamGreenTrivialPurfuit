"""
@author: Joseph Aulds
"""
import random
from State import State
from StateManager import StateManager

class Game_Logic():
    def __init__(self,
                num_players):
        sm = StateManager()
        sm.transition_state(State.new_game)
        self.num_players = num_players
        for i in range(num_players):
            print self.roll_die()

    def roll_die(self):
        return random.randint(1,6)


class Player():
    def __init__(self,
             position,
             score,
             ):
             self.position = position




if __name__ == "__main__":
    sm = StateManager()
    gl = Game_Logic(2)

    print gl.roll_die()



    print("Current state is: {}".format(sm.get_current_state()))

    sm.transition_state(State.gameplay)

    print("Current state is: {}".format(sm.get_current_state()))
