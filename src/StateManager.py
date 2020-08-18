"""
@author: Tyler MacDonald
"""

from CategorySelectionDisplayFrame import CategorySelectionDisplayFrame
from DatabaseToolFrame import DatabaseToolFrame
from GameplayFrame import GameplayFrame
from NewGameFrame import NewGameFrame
from QuestionDisplayFrame import QuestionDisplayFrame
from SaveState import SaveState
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
        self.save_state = None

    def transition_state(self, state):
        """
        """
        print("StateManager: Transitioning from {} to {}".format(self.current_state, state))
        self.current_state = state

        # TODO: Actual logic for transitioning between states
        if self.current_state == State.title_screen:
            frame = TitleScreenFrame(self.app)
        elif self.current_state == State.database_tool:
            frame = DatabaseToolFrame(self.app)
        elif self.current_state == State.new_game:
            frame = NewGameFrame(self.app)
        elif self.current_state == State.quit:
            sys.exit(1)

        self.app.switch_frame(frame)

    def transition_to_gameplay(self, save_state):
        """
        """
        self.current_state = State.gameplay
        gameplay_frame = GameplayFrame(self.app, save_state)
        self.app.switch_frame(gameplay_frame)

    def transition_to_gameplay_from_question(self):
        """
        """
        gameplay_frame = GameplayFrame(self.app, self.save_state)

        self.app.switch_frame(gameplay_frame)


    def transition_to_question(self, gameplay_frame, end_game):
        """
        """
        self.current_state = State.question

        if end_game:
            self.app.switch_frame(CategorySelectionDisplayFrame(self.app, gameplay_frame))
        else:
            # save the current state of the game
            self.save_state = SaveState(gameplay_frame.game_logic)

            frame = QuestionDisplayFrame(self.app, self.save_state)
            self.app.switch_frame(frame)

    def get_current_state(self):
        """
        """
        return self.current_state
