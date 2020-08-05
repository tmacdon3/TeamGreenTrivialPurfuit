"""
@author: Tyler MacDonald
"""

from GameCell import GameCell
from GameLogic import GameLogic
from GameState import GameState
import os
import random
from SaveState import SaveState
from State import State
import sys
import tkinter as tk
    
x_padding = 25
y_padding = 10

FRAME_BG = "#264653"
BUTTON_BG = "#2a9d8f"
LABEL_BG = "#e9c46a"
EXTRA_BG = "#f4a261"
EXTRA2_BG = "#e76f51"

CATEGORIES = ["Category_1", "Category_2", "Category_3", "Category_4"]

class GameplayFrame(tk.Frame):

    def __init__(self, master, save_state):
        """
        """
        tk.Frame.__init__(self, bg=FRAME_BG)
        self.game_logic = save_state.game_logic
        self.state_manager = master.state_manager
        self.game_state = GameState.roll_die
        self.game_logic.player_turn()
        self.current_die_roll = 0

        self.current_category = None

        self.correct_answer = None

        self.center_row = 6
        self.center_column = 6

        rows = len(self.game_logic.matrix)
        
        # initialize matrix of GameCells from game logic
        self.game_cell_matrix = []
        row_index = 0
        for row in self.game_logic.matrix:
            column_index = 0
            row_list = []
            for value in row:
                if value != -1:
                    btn_cell = GameCell(game_frame=self, width=6, height=3, color=self.get_cell_color(value), category=self.game_logic.category_list[value], row=row_index, column=column_index)
                    btn_cell.grid(row=row_index, column=column_index)
                    row_list.append(btn_cell)
                else:
                    row_list.append(None)
                column_index += 1
            self.game_cell_matrix.append(row_list)
            row_index += 1

        # title screen button
        self.btn_title_screen = tk.Button(master=self, bg=BUTTON_BG, text="Title Screen", command=self.title_screen_btn_command)
        self.btn_title_screen.grid(row=rows, column=0, columnspan=2, sticky="W")

        # player labels
        self.lbl_player_1 = tk.Label(master=self, text="p1 Score: ", bg=LABEL_BG)
        self.lbl_player_2 = tk.Label(master=self, text="p2 Score: ", bg=LABEL_BG)
        self.lbl_player_3 = tk.Label(master=self, text="p3 Score: ", bg=LABEL_BG)
        self.lbl_player_4 = tk.Label(master=self, text="p4 Score: ", bg=LABEL_BG)
        self.lbl_player_1.grid(row=rows, column=1, columnspan=3)
        self.lbl_player_2.grid(row=rows, column=4, columnspan=3)
        self.lbl_player_3.grid(row=rows, column=7, columnspan=3)
        self.lbl_player_4.grid(row=rows, column=10, columnspan=3)

        # roll dice button
        self.btn_roll_die = tk.Button(master=self, bg=BUTTON_BG, text="Roll Die", command=self.roll_die_btn_command)
        self.btn_roll_die.grid(row=9, column=9, columnspan=2)

        # question button
        btn_question = tk.Button(master=self, bg=BUTTON_BG, text="Question", command=self.question_btn_command)
        btn_question.grid(row=10, column=9, columnspan=2)

        # status display
        self.msg_status = tk.Message(master=self, text="Status Display", bg=LABEL_BG)
        self.msg_status.grid(row=8, column=2, columnspan=3, rowspan=3)

        # update displays based on current game logic information
        self._update_status_display()
        self._display_start_positions()
        self._update_score_display()

    def _display_start_positions(self):
        """
        """
        for k in self.game_logic.player_dict.keys():
            pos = self.game_logic.get_player_position(k)
            print(pos)
            self._get_button(pos[0], pos[1]).add_player(k)
    
    def _update_score_display(self):
        """
        """
        for k,v in self.game_logic.player_dict.items():
            score = v.get_score()
            if k == "p1":
                self.lbl_player_1["text"] = "p1 Score: {}".format(score)
            elif k == "p2":
                self.lbl_player_2["text"] = "p2 Score: {}".format(score)
            elif k == "p3":
                self.lbl_player_3["text"] = "p3 Score: {}".format(score)
            elif k == "p4":
                self.lbl_player_4["text"] = "p4 Score: {}".format(score)

    def _update_status_display(self):
        """
        """

        if self.game_state == GameState.roll_die:
            status_message = "{} should roll the die".format(self.game_logic.current_player)
        elif self.game_state == GameState.answer_question:
            status_message = "{} should request a question".format(self.game_logic.current_player)
        elif self.game_state == GameState.choose_cell:
            status_message = "{} rolled a {} and should choose a cell to move to".format(self.game_logic.current_player, self.current_die_roll)
        elif self.game_state == GameState.end_game:
            status_message = "{} should choose a category".format(self.game_logic.current_player)
        else:
            status_message = "Unknown GameState. HELP!"

        self.msg_status["text"] = status_message

    def _get_button(self, row, column):
        """
        """
        return self.game_cell_matrix[row][column]

    def get_cell_color(self, cell_type):
        return self.game_logic.get_category_color(cell_type)

    def question_btn_command(self):
        """
        """
        if self.game_state == GameState.answer_question:
            print("GameplayFrame: Sending State Transition Request to StateManager")
            self.state_manager.transition_to_question(self)
        else:
            print("Not the correct state to request a question")

    def roll_die_btn_command(self):
        """
        """
        if self.game_state == GameState.roll_die:
            self.current_die_roll = self.game_logic.roll_die()
            self.game_state = GameState.choose_cell
            self._update_status_display()
        else:
            print("Not the correct state to roll the die")

    def button_was_clicked(self, row, column):
        """
        """
        if self.game_state == GameState.choose_cell:
            print("Button at [row={}, column={}] was clicked".format(row, column))

            # get where current player is
            pos = self.game_logic.get_player_position(self.game_logic.current_player)

            # remove current player from old cell
            self._get_button(pos[0], pos[1]).remove_player(self.game_logic.current_player)

            # add player to new cell
            self._get_button(row, column).add_player(self.game_logic.current_player)

            # update player position
            self.game_logic.player_dict[self.game_logic.current_player].set_position((row, column))
            
            # update current category
            self.game_logic.current_category = self._get_button(row, column).category

            # update game state and display
            self.game_state = GameState.answer_question
            self._update_status_display()
        else:
            print("Not the correct state to click a button")
        
    def title_screen_btn_command(self):
        """
        """
        print("GameplayFrame: Sending State Transition Request to StateManager")
        self.state_manager.transition_state(State.title_screen)