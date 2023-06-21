from random import randint
import os

greeting_message = """
***********************************************************************
*     *****  *****  *****   ***** ***** *****   ***** ***** *****     * 
*       *      *    *         *   *   * *         *   *   * *         *
*       *      *    *         *   ***** *         *   *   * ***       *
*       *      *    *         *   *   * *         *   *   * *         *
*       *    *****  *****     *   *   * *****     *   ***** *****     *
***********************************************************************
                       Welcome to the game!  
"""


class Player:
    def __init__(self, name, tile):
        self.name = name
        self.tile = tile
        self.points = 0
        self.is_active_player = False
    
    def __repr__(self):
        return f"{self.name} is playing '{self.tile}' and has {self.points} points. Active player: {self.is_active_player}"
    
    def add_point(self):
        self.points += 1
    
    def switch_active(self):
        if self.is_active_player == False:
            self.is_active_player = True
        else:
            self.is_active_player = False
    
    def reset_points(self):
        self.points = 0


############## Game
## Attributes:
    # board
    # player_1
    # player_2
## Methods:
    # print_board
    # check_if_winner
    # check_if_tie
    # reset_board
    # clear_screen



# Def Board

# Print Greeting

# Define player 1 and tile
# Define player 2 and tile

# Randomly Choose First Player

# Clear Screen
# Show Score
# Print Board
# Show available positions
# Select position

# Check if winner 

# If winner:
    # Add point to active player
    # Ask if continue playing
    # if yes
        # Reset Board
        # clear screen
        # random player
        # print score
        # print board
    # if no:
        # Exit game
        # print exit message and score
# If no winner:
    # clear screen
    # reverse players
    # print score
    # print board

# If Tie:
    # Ask if continue playing
    # If yes:
        # Reset Board
        # clear screen
        # random player
        # print score
        # print board
    # If no:
        # exit game
        # print exit message and score
# If no Tie:
    # clear screen
    # reverse players
    # print score
    # print board


