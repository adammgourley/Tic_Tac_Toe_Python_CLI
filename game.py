# Tic Tac Toe (2 player game)

import pyinputplus as pyip 		# User input validation

class Board:
	def __init__(self):
		self.board = [['-', '-', '-'],
					  ['-', '-', '-'],
					  ['-', '-', '-']]

	def print_board(self):
		for i in self.board:
			print("| ", end="")
			for y in i:
				print(f"{y}", end=" | ")
			print()


def player_turn(board, player_sign):
	while True:
		row = pyip.inputNum(prompt="Row #: ", min=1, max=3)
		col = pyip.inputNum(prompt="Column #: ", min=1, max=3)
		
		if board[int(row) - 1][int(col) - 1] == '-':
			board[int(row) - 1][int(col) - 1] = player_sign
			break
		else:
			print("That spot is taken. Choose another.")


def game_over_check(board):
	if board[0][0] == board[0][1] and board[0][2] == board[0][0]:
		if board[0][0] == '-':
			return False
		return True
	if board[1][0] == board[1][1] and board[1][2] == board[1][0]:
		if board[1][0] == '-':
			return False
		return True
	if board[2][0] == board[2][1] and board[2][2] == board[2][0]:
		if board[2][0] == '-':
			return False
		return True
	if board[0][0] == board[1][0] and board[2][0] == board[1][0]:
		if board[0][0] == '-':
			return False
		return True
	if board[0][1] == board[1][1] and board[2][1] == board[1][1]:
		if board[0][1] == '-':
			return False
		return True
	if board[0][2] == board[1][2] and board[2][2] == board[1][2]:
		if board[0][2] == '-':
			return False
		return True
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		if board[0][0] == '-':
			return False
		return True
	return False


def main():
	board = Board()
	turn = 0
	board.print_board()
	while game_over_check(board.board) is False:
		if turn == 0:
			player = 'O'
			turn = 1
		else:
			player = 'X'
			turn = 0

		print(f"Player {player}'s turn...")
		player_turn(board.board, player)
		board.print_board()

	if turn == 0:
		print("Player X won!")
	else:
		print("Player O won!")


if __name__ == '__main__':
	main()