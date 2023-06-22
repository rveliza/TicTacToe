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
    
    def reset_points(self):
        self.points = 0

class Game:
    def __init__(self, player_1: object, player_2: object):
        self.board = [
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "]
]
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1, player_2]
        self.available_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.game_over = False
    
    def __repr__(self):
        return "Tic Tac Toe Game Class"
    
    def print_board(self):
        print("\n")
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print("\n")

    def add_tile(self, player: object, position: str):
        if position in self.available_positions:
            position = int(position)
            if position == 7:
                self.board[0][0] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 8:
                self.board[0][2] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 9:
                self.board[0][4] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 4:
                self.board[2][0] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 5:
                self.board[2][2] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 6:
                self.board[2][4] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 1:
                self.board[4][0] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 2:
                self.board[4][2] = player.tile
                self.available_positions.remove(str(position))
                return True
            if position == 3:
                self.board[4][4] = player.tile
                self.available_positions.remove(str(position))
                return True
        else:
            return False
        
    def check_if_full_board(self):
        if len(self.available_positions) == 0:
            return True
        return False
    
    def check_if_winner(self, player: object):
        # Top Row
        if self.board[0][0] == player.tile and self.board[0][2] == player.tile and self.board[0][4] == player.tile:
            return True
        # Middle Row
        if self.board[2][0] == player.tile and self.board[2][2] == player.tile and self.board[2][4] == player.tile:
            return True
        # Bottom Row
        if self.board[4][0] == player.tile and self.board[4][2] == player.tile and self.board[4][4] == player.tile:
            return True
        # Left Col
        if self.board[0][0] == player.tile and self.board[2][0] == player.tile and self.board[4][0] == player.tile:
            return True
        # Middle Col
        if self.board[0][2] == player.tile and self.board[2][2] == player.tile and self.board[4][2] == player.tile:
            return True
        # Right Col
        if self.board[0][4] == player.tile and self.board[2][4] == player.tile and self.board[4][4] == player.tile:
            return True
        # Diag 1
        if self.board[0][0] == player.tile and self.board[2][2] == player.tile and self.board[4][4] == player.tile:
            return True
        # Diag 2
        if self.board[4][0] == player.tile and self.board[2][2] == player.tile and self.board[0][4] == player.tile:
            return True
        return False
    
    def reset_board(self):
        self.board = [
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "]
]
    
    def clear_screen(self):
        os.system('clear')

    def random_player(self):
        random_number = randint(0, 1)
        if random_number == 0:
            self.player_1.is_active_player = True
        else:
            self.player_2.is_active_player = True

    def show_score(self):
        st_desc = f"{self.player_1.name}: {self.player_1.points} vs {self.player_2.name}: {self.player_2.points}"
        print(st_desc)

    def select_active_player(self):
        for player in self.players:
            if player.is_active_player:
                return player

    def show_active_player(self, player):
        print(f"{player.name}'s turn, using '{player.tile}'")

    def show_available_moves(self):
        return input(f"Choose an available space: {self.available_positions} ")

    def switch_active_players(self):
        for player in self.players:
            if player.is_active_player == True:
                player.is_active_player = False
            else:
                player.is_active_player = True  
            
    def prompt_continue_play(self):
        continue_play = input("Would you like to continue? -press any key for 'Yes', 'n' for no.")
        if continue_play != 'n':
            self.available_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            self.reset_board()
            return True
        else:
            return False

    def small_reset(self):
        self.clear_screen()
        self.show_score()
        self.print_board()

    def exit_game(self):
        self.game_over = True
        self.small_reset()
        print("Good Bye!")

    def is_winner_procedure(self, active_player):
        print(f"\n{active_player.name} won! with {active_player.points} points!")
        active_player.add_point()
        continue_play = ttt.prompt_continue_play()
        self.small_reset()
        if not continue_play:
            self.exit_game()

    def board_full_procedure(self):
        print("It is a tie!")
        continue_play = ttt.prompt_continue_play()
        self.small_reset()
        if not continue_play:
            self.exit_game()

######### INITIAL SETUP ################
os.system('clear')
print(greeting_message)

# Create Players
x_player_name = input("Name for player playing 'X': ")
player_1 = Player(x_player_name, "X")

y_player_name = input("Name for player playing 'O': ")
player_2 = Player(y_player_name, "O")

# Create Game
ttt = Game(player_1, player_2)

# Randomly Choose First Player
ttt.random_player()

############### GAME LOOP #################
while(not ttt.game_over):
    ttt.small_reset()
    active_player = ttt.select_active_player()
    ttt.show_active_player(active_player)

    selected_position = ttt.show_available_moves()
    tile_added = ttt.add_tile(active_player, selected_position)
    if tile_added:
        ttt.switch_active_players()
        is_winner = ttt.check_if_winner(active_player)
        board_full = ttt.check_if_full_board()
        if is_winner:
            ttt.is_winner_procedure(active_player)
        elif board_full:
            ttt.board_full_procedure()