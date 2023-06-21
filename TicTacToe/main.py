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

game_over = False
global player_1_turn
player_1_turn = False
playing_tile = "O"
player_1_score = 0
player_2_score = 0

board = [
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "]
]

available_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def mark_board(position, marker):
    if position == "7":
        board[0][0] = marker
    elif position == "8":
        board[0][2] = marker
    elif position == "9":
        board[0][4] = marker
    elif position == "4":
        board[2][0] = marker
    elif position == "5":
        board[2][2] = marker
    elif position == "6":
        board[2][4] = marker
    elif position == "1":
        board[4][0] = marker
    elif position == "2":
        board[4][2] = marker
    elif position == "3":
        board[4][4] = marker
    else:
        pass


def print_board(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print("\n")

def choose_player(value):
    return input(f"Choose a name for player {value}: ")

def set_first_player(rand_number):
    if rand_number == 0:
        return player_1
    return player_2

def check_winner(tile):
    # top row
    if board[0][0] == tile and board[0][2] == tile and board[0][4] == tile:
        return True
    # middle row
    if board[2][0] == tile and board[2][2] == tile and board[2][4] == tile:
        return True
    # bottom row
    if board[4][0] == tile and board[4][2] == tile and board[4][4] == tile:
        return True
    # left column
    if board[0][0] == tile and board[2][0] == tile and board[4][0] == tile:
        return True
    # middle column
    if board[0][2] == tile and board[2][2] == tile and board[4][2] == tile:
        return True
    # right column
    if board[0][4] == tile and board[2][4] == tile and board[4][4] == tile:
        return True
    # diagonal 1
    if board[0][0] == tile and board[2][2] == tile and board[4][4] == tile:
        return True
    # diagonal 2
    if board[0][4] == tile and board[2][2] == tile and board[4][0] == tile:
        return True
    return False

def check_tie():
    if len(available_positions) == 0:
        return True
    return False

def reverse_players():
    print(player_1_turn)
    input()
    if player_1_turn == False:
        print("over here")
        input()
        player_1_turn = True
    # player_1_turn = False

    # if playing_tile == "X":
    #     playing_tile = "O"
    # playing_tile = "X"

################## GAME INIT ############################
print(greeting_message)
player_1 = choose_player("X") #Reyner
player_2 = choose_player("O") #Juan

#Choose a random starting position"
rand_number = randint(0,1)
first_player = set_first_player(rand_number)

if first_player == player_1:
    player_1_turn = True
    playing_tile = "X"
else:
    player_1_turn = False
    playing_tile = "O"


################# GAME LOOP ##############################

while(not game_over):
    # Print new board on clear screen:
    os.system('cls')
    print_board(board)
    print(available_positions)

    if player_1_turn:
        position = input(f"Choose a position for {player_1} {playing_tile}: ")
    else:
        position = input(f"Choose a position for {player_2} {playing_tile}: ")

    while (position not in available_positions):
        print(available_positions)
        position = input("Position invalid, please choose a correct position")
    available_positions.remove(position)
    mark_board(position, playing_tile)

    print("check if win")
    winner = check_winner(playing_tile)
    print("check if tie")
    tie = check_tie()

    print("Game ended")
    print("Adding points to winner")
    
    reverse_players()


    # play_again = input("Would you like to play again? ('q' to quit) ")
    # if (play_again != 'q'):
    #     print("Cleaning screen and starting over")
    #     os.system('cls')
    # else:
    #     print("Good Bye!")
    #     print("Printing total scores")
    #     game_over = True