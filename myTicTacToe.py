# myTicTacToe.py - create a Tic Tac Toe using what i learned about dictionaries
myboard = {0:' ', 1:' ', 2: ' ',
		3:' ', 4:' ', 5: ' ',
		6:' ', 7:' ', 8:' '}
boarder = '|'
player1Score= 0
player2Score= 0

def printBoard(board):
	print(board[0] + boarder + board[1] + boarder + board[2])
	print('-+-+-')
	print(board[3] + boarder + board[4] + boarder + board[5])
	print('-+-+-')
	print(board[6] + boarder + board[7] + boarder + board[8])
# printBoard(myboard)

def inputBoard():
	pass

def scoreCounter():
	pass

def boardReset():
	pass

# main while loop