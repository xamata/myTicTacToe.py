# myTicTacToePsuedocode.py - create a Tic Tac Toe using what i learned about dictionaries in PsuedoCode
myboard = # a dictionary with keys:0-8 and  ' ' as values

# scores should be universal while the program is running to keep count, starting from 0
player1Score= 0
player2Score= 0
tieScore = 0

 # player is a dictionary that will output 'X' or 'O'
 create player dictionary that will hold whether player1 is a 'O' or an 'X' and same for player 2 and for ties

# prints the board for the users to see progression of the game
def printBoard(board):
	print the board using the myboard dictionary and characters like '|', '-', and '+'

# put the players input into the board, changes the look of the board
def inputBoard(player, playerInput): # dictionary for player, integer for playerInput
	check if playeyInput is a valid integer
	check if game tile has a game piece already
		if game tile has a piece already inside, return false
		else Put desired players integer into the myboard dictionary using indexing

# check if there is a winner or tie to end that round
def winCheck(board):
	check if the board has a cats game, 3 'O's in a row, or '3' X's in a row # cats game is full board with no 3 in a row
		if tie, return player dictionary with a 3
		elif player1 wins returns player dictionary with 0
		elif player2 wins returns player dictionary with 1

# keeps score of the game 
def scoreCounter(winner):
	check who is the winner with an if statement:
		if player1 wins:
			add 1 to player 1 score
		if else player 2 wins:
			add 1 to player 2 score
		else: 
			add 1 to tiescore
			return back to main, it was a tie

# plugs in reset 
def boardReset():
	plug in the original board containing only spaces

# main game setup

print player1 if they want to be X or O
set player1Character to be the input of the question
	check if input was an X or an O using player dictionary variable
	else, go back to the input

print players who player1 will be 'x' or an 'o' and who player2 will be 
print scores

# main while loop , if broken , game will end
while True:
	print: are you ready to play?
	get input:
	if: yes, continue
	else: break

	call printBoard() method with myboard as input to display board to get the game feel

	while loop to return to until round has ended

		print: ask where player of choice wants to place their game piece, will be a integer 0-8(check)
		set a variable playerInput equal to the input of the previous question

		call inputBoard() method with whose turn it is and their playerInput
			if inputBoard() returns false, go to the beginning of while loop with an error message that the tile is already taken

		check the board to see if someone won or game board is full using winCheck
			if someone won or game board is full, break out of loop
			else: 
				if player1 turn, change to player2
				elif player2 turn change to player1
				return to top of while loop


	call the scoreCounter() method with winner inputed to add to the overall scoreCounter
	print scores 

	print: ask players if they want to play again
		if yes, return to the top of the while loop
		else break out of loop


# problems/ things i didn't account for
# 1. function for changing the player's name
# 2. lack of knowledge on dictionaries. I didn't know you can't call a key using it's value/
#		if it's possible, i don't know how. Maybe using value method, and the output saved to a
# 		variable that could be used to determine which player has which game piece
# 3. The dictionary and lists seem redundant, what's the better way?
# 		The reason for it is so that the player their game piece, usually the beginning of the game
# 
