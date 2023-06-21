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
    def __init__(self, name: str, tile: str):
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
## Methods:
    # mark board
    # check_if_winner
    # check_if_tie
    # reset_board
    # clear_screen

class Game:
    def __init__(self, player_1: object, player_2: object):
        self.board = [
    ["X", "|", "X", "|", "X"],
    ["-", "-", "-", "-", "-"],
    ["X", "|", "X", "|", "X"],
    ["-", "-", "-", "-", "-"],
    ["X", "|", "X", "|", "X"]
]
        self.player_1 = player_1
        self.player_2 = player_2

        self.available_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    def __repr__(self):
        return "Tic Tac Toe Game Class"
    
    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print("\n")

    def check_if_full_board(self):
        if len(self.available_positions) == 0:
            return True
        return False
    
    def check_if_winner(self, tile):
        # Top Row
        if self.board[0][0] == tile and self.board[0][2] == tile and self.board[0][4] == tile:
            return True
        # Middle Row
        if self.board[2][0] == tile and self.board[2][2] == tile and self.board[2][4] == tile:
            return True
        # Bottom Row
        if self.board[4][0] == tile and self.board[4][2] == tile and self.board[4][4] == tile:
            return True
        # Left Col
        if self.board[0][0] == tile and self.board[2][0] == tile and self.board[4][0] == tile:
            return True
        # Middle Col
        if self.board[0][2] == tile and self.board[2][2] == tile and self.board[4][2] == tile:
            return True
        # Right Col
        if self.board[0][4] == tile and self.board[2][4] == tile and self.board[4][4] == tile:
            return True
        # Diag 1
        if self.board[0][0] == tile and self.board[2][2] == tile and self.board[4][4] == tile:
            return True
        # Diag 2
        if self.board[4][0] == tile and self.board[2][2] == tile and self.board[0][4] == tile:
            return True
        return False
        
            

player_1 = Player("Reyner", "X")
player_2 = Player("Juan", "O")

ttt = Game(player_1, player_2)
print("Full Board: ", ttt.check_if_full_board())
print("Winner: ", ttt.check_if_winner("X"))

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


