"""
@author: Tyler MacDonald
"""

from DatabaseToolFrame import DatabaseToolFrame
from GameplayFrame import GameplayFrame
from NewGameFrame import NewGameFrame
from QuestionDisplayFrame import QuestionDisplayFrame
from State import State
import sys
from TitleScreenFrame import TitleScreenFrame
import tkinter as tk

# TODO Make this a singleton design

class StateManager:

    def __init__(self, app):
        """
        """
        self.current_state = State.title_screen
        self.app = app

    def transition_state(self, state):
        """
        """
        print("StateManager: Transitioning from {} to {}".format(self.current_state, state))
        self.current_state = state

        # TODO: Actual logic for transitioning between states
        if self.current_state == State.title_screen:
            frame = TitleScreenFrame(self.app, self.app.state_manager)
        elif self.current_state == State.database_tool:
            frame = DatabaseToolFrame(self.app, self.app.state_manager, self.app.database_interface)
        elif self.current_state == State.new_game:
            frame = NewGameFrame(self.app, self.app.state_manager)
        elif self.current_state == State.gameplay:
            frame = GameplayFrame(self.app, self.app.state_manager)
        elif self.current_state == State.question:
            frame = QuestionDisplayFrame(self.app, self.app.state_manager, self.app.database_interface)
        elif self.current_state == State.quit:
            sys.exit(1)

        self.app.switch_frame(frame)

    def get_current_state(self):
        """
        """
        return self.current_state
