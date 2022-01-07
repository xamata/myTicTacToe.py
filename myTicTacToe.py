# myTicTacToe.py - create a Tic Tac Toe using Dictionaries and functions
import pyinputplus as pyip
import string

myboard = {0:' ', 1:' ', 2: ' ',
		3:' ', 4:' ', 5: ' ',
		6:' ', 7:' ', 8:' '} 
boarder = '|'

# scores for the game
player1Score = 0
player2Score = 0
tieScore = 0

# player dictionary that will account for player1, player2, and tie, with their gamepieces
playerDict = {'Player 1': '', 'Player 2': '', 'Tie': 3}

# print out the boardgame
def printBoard(board):
	print(board[0] + boarder + board[1] + boarder + board[2])
	print('-+-+-')
	print(board[3] + boarder + board[4] + boarder + board[5])
	print('-+-+-')
	print(board[6] + boarder + board[7] + boarder + board[8])

# checks/input the player's decisions
def inputBoard(player, playerInput):
	if playerInput not in range(0,9):
		print('Please enter an integer from 0 to 8.')
		return False
	elif myboard[playerInput] == 'X' or myboard[playerInput] == 'O':
		print('Please enter a tile that is empty.')
		return False
	else:
		myboard[playerInput] = playerDict[player] # should grab from inputBoard(player,playerInput)

# check if winner or tie
def winCheck(board):
	if ((board[0]=='X' and board[1]=='X' and board[2]=='X') or (board[0]=='X' and board[4]=='X' and board[8]=='X') or 
		(board[0]=='X' and board[3]=='X' and board[6]=='X') or (board[3]=='X' and board[4]=='X' and board[5]=='X') or
		(board[6]=='X' and board[7]=='X' and board[8]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X') or 
		(board[2]=='X' and board[4]=='X' and board[6]=='X') or (board[1]=='X' and board[4]=='X' and board[7]=='X')):
		return playerDict['Player 1']
	elif ((board[0]=='O' and board[1]=='O' and board[2]=='O') or (board[0]=='O' and board[4]=='O' and board[8]=='O') or 
		(board[0]=='O' and board[3]=='O' and board[6]=='O') or (board[3]=='O' and board[4]=='O' and board[5]=='O') or
		(board[6]=='O' and board[7]=='O' and board[8]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or 
		(board[2]=='O' and board[4]=='O' and board[6]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O')):
		return playerDict['Player 1']
	elif (' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2] and ' ' not in board[3] and ' ' not in board[4] and
		' ' not in board[5] and ' ' not in board[6] and ' ' not in board[7] and ' ' not in board[8]):
		return playerDict['Tie']
	else: 
		return False

# resets the board for new round
def boardReset():
	myboard = {0:' ', 1:' ', 2: ' ',
		3:' ', 4:' ', 5: ' ',
		6:' ', 7:' ', 8:' '} 

# main game start
print("Which game piece would Player 1 like to be?")
player1Choice = pyip.inputChoice(['X','O'])

# main game loop, if broken game will end
while True:
	gameStart = pyip.inputYesNo('Are you read to start the game?')
	if gameStart == 'no': 
		continue
	else:
		pass
	print('Game Starts')

