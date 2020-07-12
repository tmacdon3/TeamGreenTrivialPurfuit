"""
@author: Tyler MacDonald

Enum for managing the different states
"""

import enum

class State(enum.Enum):
    title_screen = 1
    database_tool = 2
    gameplay = 3
    question = 4