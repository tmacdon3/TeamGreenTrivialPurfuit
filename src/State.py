"""
@author: Tyler MacDonald

Enum for managing the different states
"""

import enum

class State(enum.Enum):
    title_screen = 1
    database_tool = 2
    new_game = 3
    gameplay = 4
    question = 5
    quit = 6
