"""
@author: Tyler MacDonald

Enum for managing the different game states
"""

import enum

class GameState(enum.Enum):
    roll_die = 1,
    answer_question = 2,
    choose_cell = 3,
    end_game = 4
