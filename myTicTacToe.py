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

# player dictionary that will account for player1, player2, with their gamepieces
playerDict = {'Player 1': ' ', 'Player 2': ' '}

# player list to keep account of which player is going
playerList = ['Player 1', 'Player 2', 'Tie']

# print out the boardgame
def printBoard(board):
	print(board[0] + boarder + board[1] + boarder + board[2])
	print('-+-+-')
	print(board[3] + boarder + board[4] + boarder + board[5])
	print('-+-+-')
	print(board[6] + boarder + board[7] + boarder + board[8])

# changes playerTurn from round to round
def playerChange(player):
	if player == playerList[0]:
		return playerList[1]
	else:
		return playerList[0]

# checks/input the player's decisions
def inputBoard(player, playerInput):
	playerInput = int(playerInput)
	if playerInput not in range(0,9):
		print('Please enter an integer from 0 to 8.')
		return False
	elif myboard[playerInput] == 'X' or myboard[playerInput] == 'O':
		print('Please enter a tile that is empty.')
		return False
	else:
		myboard[playerInput] = playerDict[player] # should grab from inputBoard(player,playerInput)

# check if winner or tie
def winChecker(board):
	# determine who player1 is and player2 is
	if playerDict['Player 1'] == 'X':
		playerX = playerList[0]
		playerY = playerList[1]
	else:
		playerX = playerList[1]
		playerY = playerList[0]

	if ((board[0]=='X' and board[1]=='X' and board[2]=='X') or (board[0]=='X' and board[4]=='X' and board[8]=='X') or 
		(board[0]=='X' and board[3]=='X' and board[6]=='X') or (board[3]=='X' and board[4]=='X' and board[5]=='X') or
		(board[6]=='X' and board[7]=='X' and board[8]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X') or 
		(board[2]=='X' and board[4]=='X' and board[6]=='X') or (board[1]=='X' and board[4]=='X' and board[7]=='X')):
		return playerX
	elif ((board[0]=='O' and board[1]=='O' and board[2]=='O') or (board[0]=='O' and board[4]=='O' and board[8]=='O') or 
		(board[0]=='O' and board[3]=='O' and board[6]=='O') or (board[3]=='O' and board[4]=='O' and board[5]=='O') or
		(board[6]=='O' and board[7]=='O' and board[8]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or 
		(board[2]=='O' and board[4]=='O' and board[6]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O')):
		return playerY
	elif (' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2] and ' ' not in board[3] and ' ' not in board[4] and
		' ' not in board[5] and ' ' not in board[6] and ' ' not in board[7] and ' ' not in board[8]):
		return playerList[2]
	else:
		pass

# resets the board for new round
def boardReset():
	myboard = {0:' ', 1:' ', 2: ' ',
		3:' ', 4:' ', 5: ' ',
		6:' ', 7:' ', 8:' '} 
	return myboard


# main game start
print('Welcome to Tic Tac Toe!\n')
print("Which game piece would Player 1 like to be?")
player1Choice = pyip.inputChoice(['X','O'])
if player1Choice == 'X':
	playerDict['Player 1'] = 'X'
	playerDict['Player 2'] = 'O'
else:
	playerDict['Player 1'] = 'O'
	playerDict['Player 2'] = 'X'


# main game loop, if broken game will end
while True:
	playerTurn = playerList[0]
	myboard = boardReset()

	if player1Score == 1 or player2Score == 1 or tieScore == 1:
		gameStart = pyip.inputYesNo('Would you like to start a new round? ')
		if gameStart == 'no': 
			print('Thank you for playing!')
			break
		else:
			pass
	else:
		gameStart = pyip.inputYesNo('Are you ready to start a new game? ')
		if gameStart == 'no': 
			continue
		else:
			pass

	print('\n')
	if tieScore == 0:
		print(f"Player1 Score = {player1Score}\nPlayer2 Score = {player2Score}")
	else: 
		print(f"Player1 Score = {player1Score}\nPlayer2 Score = {player2Score}\nGames Tied = {tieScore}")
	printBoard(myboard)
	

	# beginning of each round
	while True:
		print(f"{playerTurn}, where would you like to place your game piece?")
		playerInput = pyip.inputChoice(['0','1','2','3','4','5','6','7','8'])

		# boardStatus = True
		boardStatus = inputBoard(playerTurn, playerInput)
		if boardStatus == False:
			continue
		else:
			pass

		winCheck = winChecker(myboard)
		if winCheck == playerList[0]:
			print(f"{playerList[0]} has won the game!")
			player1Score += 1
			printBoard(myboard)
			break
		elif winCheck == playerList[1]:
			print(f"{playerList[1]} has won the game!")
			player2Score += 1
			printBoard(myboard)
			break
		elif winCheck == 'Tie':
			print("It's a tie!")
			tieScore += 1
			printBoard(myboard)
			break
		else:
			playerTurn = playerChange(playerTurn)

		printBoard(myboard)
