"""
@author: Tyler MacDonald
"""

from State import State

class StateManager:

    def __init__(self):
        """
        """
        self.current_state = State.title_screen

    def transition_state(self, state):
        """
        """
        self.current_state = state

        # TODO: Actual logic for transitioning between states

    def get_current_state(self):
        """
        """
        return self.current_state

# Usage example
if __name__ == "__main__":
    sm = StateManager()

    print("Current state is: {}".format(sm.get_current_state()))

    sm.transition_state(State.gameplay)

    print("Current state is: {}".format(sm.get_current_state()))