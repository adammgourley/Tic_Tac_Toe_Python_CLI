import os, time
import pyinputplus as pyip

class Board:
	def __init__(self):
		self.board = self.build()

	def build(self):
		return [['-','-','-'],['-','-','-'],['-','-','-']]

	def pretty_print(self):
		for i in self.board:
			for item in i:
				print(item, end=" ")
			print()

	def reset(self):
		self.board = self.build()

def make_move(object, player, row, col):
	if object.board[row - 1][col - 1] == '-':
		object.board[row - 1][col - 1] = player
		return True
	else:
		return False

def check_win(object):
	if object.board[0][0] != '-' and object.board[0][0] == object.board[0][1] and object.board[0][1] == object.board[0][2]:
		print(f"Player {object.board[0][0]} won!")
		return True
	elif object.board[1][0] != '-' and object.board[1][0] == object.board[1][1] and object.board[1][1] == object.board[1][2]:
		print(f"Player {object.board[1][0]} won!")
		return True
	elif object.board[2][0] != '-' and object.board[2][0] == object.board[2][1] and object.board[2][1] == object.board[2][2]:
		print(f"Player {object.board[2][0]} won!")
		return True
	elif object.board[0][0] != '-' and object.board[0][0] == object.board[1][0] and object.board[1][0] == object.board[2][0]:
		print(f"Player {object.board[0][0]} won!")
		return True
	elif object.board[0][1] != '-' and object.board[0][1] == object.board[1][1] and object.board[1][1] == object.board[2][1]:
		print(f"Player {object.board[0][1]} won!")
		return True
	elif object.board[0][2] != '-' and object.board[0][2] == object.board[1][2] and object.board[1][2] == object.board[2][2]:
		print(f"Player {object.board[0][2]} won!")
		return True
	elif object.board[0][0] != '-' and object.board[0][0] == object.board[1][1] and object.board[1][1] == object.board[2][2]:
		print(f"Player {object.board[0][0]} won!")
		return True
	elif object.board[0][2] != '-' and object.board[0][2] == object.board[1][1] and object.board[1][1] == object.board[2][0]:
		print(f"Player {object.board[0][2]} won!")
		return True


# Finding position to play in to make sure user cannot win. Works by finding position where player has
# opportunity to get three in a row.
# 
# If it finds a spot it wants, it implements 'make_move(object, player, row, col)'
#
def computer_turn(object):
	# Horizontal
	if object.board[0][0] == 'X' and object.board[0][1] == 'X' and object.board[0][2] == '-':
		make_move(object, 'O', 1, 3)
		return
	elif object.board[0][0] == '-' and object.board[0][1] == 'X' and object.board[0][2] == 'X':
		make_move(object, 'O', 1, 1)
		return
	elif object.board[0][0] == 'X' and object.board[0][1] == '-' and object.board[0][2] == 'X':
		make_move(object, 'O', 1, 2)
		return
	elif object.board[1][0] == 'X' and object.board[1][1] == 'X' and object.board[1][2] == '-':
		make_move(object, 'O', 2, 3)
		return
	elif object.board[1][0] == '-' and object.board[1][1] == 'X' and object.board[1][2] == 'X':
		make_move(object, 'O', 2, 1)
		return
	elif object.board[1][0] == 'X' and object.board[1][1] == '-' and object.board[1][2] == 'X':
		make_move(object, 'O', 2, 2)
		return
	elif object.board[2][0] == 'X' and object.board[2][1] == 'X' and object.board[2][2] == '-':
		make_move(object, 'O', 3, 3)
		return
	elif object.board[2][0] == '-' and object.board[2][1] == 'X' and object.board[2][2] == 'X':
		make_move(object, 'O', 3, 1)
		return
	elif object.board[2][0] == 'X' and object.board[2][1] == '-' and object.board[2][2] == 'X':
		make_move(object, 'O', 3, 2)
		return

	# Vertical
	elif object.board[0][0] == 'X' and object.board[1][0] == 'X' and object.board[2][0] == '-':
		make_move(object, 'O', 3, 1)
		return
	elif object.board[0][0] == '-' and object.board[1][0] == 'X' and object.board[2][0] == 'X':
		make_move(object, 'O', 1, 1)
		return
	elif object.board[0][0] == 'X' and object.board[1][0] == '-' and object.board[2][0] == 'X':
		make_move(object, 'O', 2, 1)
		return
	elif object.board[0][1] == 'X' and object.board[1][1] == 'X' and object.board[2][1] == '-':
		make_move(object, 'O', 3, 2)
		return
	elif object.board[0][1] == '-' and object.board[1][1] == 'X' and object.board[2][1] == 'X':
		make_move(object, 'O', 1, 2)
		return
	elif object.board[0][1] == 'X' and object.board[1][1] == '-' and object.board[2][1] == 'X':
		make_move(object, 'O', 2, 2)
		return
	elif object.board[0][2] == 'X' and object.board[1][2] == 'X' and object.board[2][2] == '-':
		make_move(object, 'O', 3, 3)
		return
	elif object.board[0][2] == '-' and object.board[1][2] == 'X' and object.board[2][2] == 'X':
		make_move(object, 'O', 1, 3)
		return
	elif object.board[0][2] == 'X' and object.board[1][2] == '-' and object.board[2][2] == 'X':
		make_move(object, 'O', 2, 3)
		return

	# Diagonal
	elif object.board[0][0] == 'X' and object.board[1][1] == 'X' and object.board[2][2] == '-':
		make_move(object, 'O', 3, 3)
		return
	elif object.board[0][0] == '-' and object.board[1][1] == 'X' and object.board[2][2] == 'X':
		make_move(object, 'O', 1, 1)
		return
	elif object.board[0][0] == 'X' and object.board[1][1] == '-' and object.board[2][2] == 'X':
		make_move(object, 'O', 2, 2)
		return
	elif object.board[0][2] == 'X' and object.board[1][1] == 'X' and object.board[2][0] == '-':
		make_move(object, 'O', 3, 1)
		return
	elif object.board[0][2] == '-' and object.board[1][1] == 'X' and object.board[2][0] == 'X':
		make_move(object, 'O', 1, 3)
		return
	elif object.board[0][2] == 'X' and object.board[1][1] == '-' and object.board[2][0] == 'X':
		make_move(object, 'O', 2, 2)
		return

	else:
		# This is where a function should come in to determine the best position for the computer to play,
		# but I just chose to have the next open spot taken; the computer just wants to make sure you lose lol..
		if object.board[1][1] == '-':
			make_move(object, 'O', 2, 2)
			return
		elif object.board[0][0] == '-':
			make_move(object, 'O', 1, 1)
			return
		elif object.board[0][1] == '-':
			make_move(object, 'O', 1, 2)
			return
		elif object.board[0][2] == '-':
			make_move(object, 'O', 1, 3)
			return
		elif object.board[1][0] == '-':
			make_move(object, 'O', 2, 1)
			return
		elif object.board[1][2] == '-':
			make_move(object, 'O', 2, 3)
			return
		elif object.board[2][0] == '-':
			make_move(object, 'O', 3, 1)
			return
		elif object.board[2][1] == '-':
			make_move(object, 'O', 3, 2)
			return
		elif object.board[2][2] == '-':
			make_move(object, 'O', 3, 3)
			return

def main():
	board = Board()
	count = 0

	while True:
		os.system('clear')
		board.pretty_print()

		if check_win(board):
			break

		print(f"Your turn (player X)")
		row = pyip.inputNum(prompt="Row #: ", min=1, max=3)
		col = pyip.inputNum(prompt="Column #: ", min=1, max=3)
		if make_move(board, 'X', int(row), int(col)):
			pass
		else:
			print("\nThat spot has already been taken.\nChoose another.\n")
			continue

		if check_win(board):
			break

		computer_turn(board)

main()