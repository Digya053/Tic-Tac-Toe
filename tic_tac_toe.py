import random
import time

from check_tic_tac_toe import CheckTicTacToe
from draw_a_game_board import GameBoard


class PlayTicTacToe():

    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.board_size = len(self.initial_board)
        self.occupied_places = []
        self.remaining_places = []
        self.players = [1, 2]
        self.user = 0
        self.random = 0
        self.winner = ""
        self.switch_player = "Player 1"
        self.user_turn = False

    def update_board(self, updated_board):
        self.initial_board = updated_board

    def adjust_players(self):
        try:
            player_user = int(input(
                "\nDo you want to be 'Player 1' or 'Player 2'. Enter '1' for 'Player 1' and '2' for 'Player 2': "))
            if player_user != 1 and player_user != 2:
                player_user = int(
                    input("You can only choose '1' or '2' as a player. Please choose again:  "))
        except ValueError:
            player_user = int(
                input("You can only choose '1' or '2' as a player. Please choose again: "))

        if player_user == 1:
            self.user = 1
            self.random = 2
            self.user_turn = True
        else:
            self.user = 2
            self.random = 1
            self.user_turn = False

        return ""

    def display_remaining_places(self):
        self.remaining_places = []
        for i in range(len(self.initial_board)):
            for j in range(len(self.initial_board)):
                if self.initial_board[i][j] == 0:
                    self.remaining_places.append((i, j))
        time.sleep(1)
        print("\nThere are " +
              str(len(self.remaining_places)) +
              " remaining places to place entry.")
        print("\nThe remaining places are: " + str(self.remaining_places))

        return len(self.remaining_places)

    def update_entries(self):
        print("It's your turn to place an entry!!!")
        row = int(
            input('Enter the row number in which you want to place your entry: '))
        column = int(
            input('Enter the column number in which you want to place your entry: '))
        self.manage_lists(row, column)
        self.initial_board[row][column] = self.user
        self.display_updated_board()
        self.user_turn = False

    def random_entries(self):
        print(self.switch_player + " is placing an entry. Please wait...")
        random_choice = random.choice(self.remaining_places)
        row = random_choice[0]
        column = random_choice[1]
        self.manage_lists(row, column)
        self.initial_board[row][column] = self.random
        self.display_updated_board()
        self.user_turn = True

    def manage_lists(self, row, column):
        self.occupied_places.append((row, column))
        self.remaining_places.remove((row, column))

    def display_updated_board(self):
        print("The updated board after " + self.switch_player + "'s entry is:")
        time.sleep(2)
        dashes = " --- " * self.board_size
        pipe = "|"
        for i in range(0, self.board_size):
            print(dashes)
            board_format = ""
            for j in range(0, self.board_size):
                board_format += pipe + " " + \
                    str(self.initial_board[i][j]) + "  "
            print(board_format + "|")

        print(dashes)
        return ""

    def switch_turn(self, player):
        self.switch_player = player
        print("It's " + self.switch_player + "'s turn!")

    def adjust_turns(self):
        if self.user_turn:
            self.switch_turn("Player " + str(self.user))
            self.update_entries()
        else:
            self.switch_turn("Player " + str(self.random))
            time.sleep(2)
            self.random_entries()


if __name__ == "__main__":
    initial_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("=== Welcome To Tic Tac Toe ===")
    game_board = GameBoard(3)
    print("\t" + str(game_board.draw_a_board()))

    size = input("Enter the size of the board: ")
    check_tic_tac_toe = CheckTicTacToe(board_size=size)
    board_size = check_tic_tac_toe.check_board_size()

    print("\nYour initial board is:")
    game_board = GameBoard(board_size)

    print("\t" + str(game_board.draw_initial_board()))
    initial_board_list = game_board.get_initial_board_numbers()

    play_tic_tac_toe = PlayTicTacToe(initial_board_list)
    play_tic_tac_toe.adjust_players()

    play_tic_tac_toe.display_remaining_places()
    length = len(play_tic_tac_toe.remaining_places)

    print("\nLet's start a game!!!")

    while length != 0:
        play_tic_tac_toe.adjust_turns()

        play_tic_tac_toe.display_remaining_places()
        length = len(play_tic_tac_toe.remaining_places)

        if len(play_tic_tac_toe.occupied_places) >= int(board_size):
            check_winner = CheckTicTacToe(
                final_board=play_tic_tac_toe.initial_board)
            check_winner.check_all()
            if check_winner.found_winner:
                print(
                    "Congratulations! " +
                    play_tic_tac_toe.switch_player +
                    " is the winner")
                break
