class GameBoard():

		def __init__(self, boardsize, initial_board = ""):
				self.initial_board = initial_board
				self.boardsize = int(boardsize)
				self.initial_board_list = []

		def draw_a_board(self):
				dashes = " --- " * self.boardsize
				pipes =  "|    " * (self.boardsize + 1)
				for i in range(0, self.boardsize):
					print(dashes)
					print(pipes)

				print(dashes)
				return ""


		def draw_a_board_with_numbers(self):
				dashes = " --- "  * self.boardsize
				pipe = "|"
				for i in range(0, self.boardsize):
						print(dashes)
						board_format = ""
						for j in range(0, self.boardsize):
								board_format += pipe + " " +  str(self.initial_board[i][j]) + "  "
						print(board_format + "|")

				print(dashes)
				return ""
		
		def draw_initial_board(self):
				dashes = " --- "  * self.boardsize
				pipe = "|"
				for i in range(0, self.boardsize):
						print(dashes)
						board_format = ""
						add_list = []
						for j in range(0, self.boardsize):
								board_format += pipe + " 0  "
								add_list.append(0)
						print(board_format + "|")
						self.initial_board_list.append(add_list)
				print(dashes)

				return ""

		def get_initial_board_numbers(self):
				return self.initial_board_list
