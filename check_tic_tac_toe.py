import numpy as np


class CheckTicTacToe():

    def __init__(self, final_board="", board_size=""):
        self.final_board = final_board
        self.found_winner = False
        if board_size:
            self.board_size = board_size
        else:
            self.board_size = len(self.final_board)

    def check_board_size(self):
        while int(self.board_size) % 2 == 0:
            self.board_size = input(
                "Please enter an odd number for a board size: ")
        return self.board_size

    def check_row(self):
        for i in range(self.board_size):
            row = self.final_board[i]
            first_number_in_row = row[0]
            if len(set(row)) == 1 and first_number_in_row != 0:
                self.found_winner = True
                return first_number_in_row

        return 0

    def check_column(self):
        trans_board = np.transpose(self.final_board)
        self.final_board = trans_board
        self.check_row()

    def check_diagonal(self):
        mid = int(self.board_size / 2)
        middle_number = self.final_board[mid][mid]
        change_row_up = mid
        change_column_up = mid
        change_row_down = mid
        change_column_down = mid
        diagonal_elements_first = []
        diagonal_elements_second = []
        if middle_number != 0:
            for i in range(self.board_size):
                diagonal_elements_first.append(self.final_board[i][i])

            if len(set(diagonal_elements_first)) == 1:
                self.found_winner = True
                return middle_number

            diagonal_elements_second.append(middle_number)
            while change_column_up != self.board_size - \
                    1 and change_row_down != self.board_size - 1:
                change_row_up = change_row_up - 1
                change_column_up = change_column_up + 1
                change_row_down = change_row_down + 1
                change_column_down = change_column_down - 1

                if self.final_board[change_row_up][change_column_up] == middle_number:
                    diagonal_elements_second.append(
                        self.final_board[change_row_up][change_column_up])
                if self.final_board[change_row_down][change_column_down] == middle_number:
                    diagonal_elements_second.append(
                        self.final_board[change_row_down][change_column_down])
                if len(diagonal_elements_second) == self.board_size:
                    self.found_winner = True
                    return middle_number

            return 0

    def check_all(self):
        self.check_row()
        self.check_column()
        self.check_diagonal()
