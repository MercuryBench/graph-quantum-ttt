from qTTT import *
from qTTT_game_util import *
import random

while(True): # loop for games
	#mode = getGameMode()
	mode = "pvp"
	if mode == "pvp":
		print("You're playing against a human opponent")
	else:
		print("You're playing against the computer")
	turn = whoGoesFirst()
	if mode == "pvp":
		print('Player ' + str(turn) + ' will go first.')	# global assumption: X always starts
		if turn == 1:
			playerLetter, player2letter = "X", "O" #inputPlayerLetter()
		else:
			playerLetter, player2letter = "O", "X" #inputPlayerLetter()
	else:
		if turn == 1:
			print('You will go first!')
			playerLetter, player2letter = "X", "O" #inputPlayerLetter()
		else:
			print('The computer will go first')
			playerLetter, player2letter = "O", "X" #inputPlayerLetter()
	
	# INITIALIZE TREE AND BOARD HERE
	#####################################################
	# define: theBoard (as the root of the tree)
	theBoard = Board()
	lastMark = None
	numMark = 0

	while (True): # loop for turns
		if turn == 1:
			print("It's player 1's turn. Place your mark (" + playerLetter + ")")
			theBoard.printBoard()

			# Check whether there is entanglement after player 2's move
			if lastMark:
				if theBoard.findCycle(lastMark.pos):
					col = getPlayerCollapse(theBoard, lastMark) # let player 1 decide where to put the last mark
					theBoard.collapse_(lastMark.letter, lastMark.num, col[0], col[1])
					theBoard.printBoard()
	  
			# look at winning conditions:
			p1won, p1lms = theBoard.hasWon(playerLetter)
			p2won, p2lms = theBoard.hasWon(player2letter)
			if p1won:
				if p2won:
					if p1lms < p2lms:
						print("\n")
						theBoard.printBoard()
						print("Player 1 (" + playerLetter + ") has won the game!")
						break
					else:
						print("\n")
						theBoard.printBoard()
						if mode == "pvp":
							print("Player 2 (" + player2letter + ") has won the game")
						else:
							print("The computer (" + player2letter + ") has won the game!")
						
						break	   			
				else:
					print("\n")
					theBoard.printBoard()
					print("Player 1 (" + playerLetter + ") has won the game!")
					break
			elif p2won:
				print("\n")
				theBoard.printBoard()
				if mode == "pvp":
					print("Player 2 (" + player2letter + ") has won the game")
				else:
					print("The computer (" + player2letter + ") has won the game!")
				break
			else:
				if theBoard.isFull():
				  print("\n")
				  theBoard.printBoard()
				  print("The game is a tie!")
				  break
		
			turn = 2
		   	# if the game hasn't ended, make a move
			pos1, pos2 = getPlayerMove(theBoard)
		   
			lastMark = theBoard.addSpookyMark_(playerLetter, numMark, pos1, pos2)
			#print("How many recursions?")
			#rec = int(raw_input())
			numMark += 1
		else:      
			if mode == "pvp":
				print("It's player 2's turn. Place your mark (" + player2letter + ")")
			else:
				print("It's the computer's turn")
			# Player 2's turn or computer.
			theBoard.printBoard()

			if mode == "pvp":
				if lastMark:
					if theBoard.findCycle(lastMark.pos):
						col = getPlayerCollapse(theBoard, lastMark) # let player 1 decide where to put the last mark
						theBoard.collapse_(lastMark.letter, lastMark.num, col[0], col[1])
						theBoard.printBoard()
		  
				# look at winning conditions:
				p1won, p1lms = theBoard.hasWon(playerLetter)
				p2won, p2lms = theBoard.hasWon(player2letter)
				if p1won:
					if p2won:
						if p1lms < p2lms:
							print("\n")
							theBoard.printBoard()
							print("Player 1 has won the game!")
							break
						else:
							print("\n")
							theBoard.printBoard()
							print("The computer has won the game!")
							break	   			
					else:
						print("\n")
						theBoard.printBoard()
						print("Player 1 has won the game!")
						break
				elif p2won:
					print("\n")
					theBoard.printBoard()
					print("The computer has won the game!")
					break
				else:
					if theBoard.isFull():
					  print("\n")
					  theBoard.printBoard()
					  print("The game is a tie!")
					  break
		
				turn = 1
			   	# if the game hasn't ended, make a move
				pos1, pos2 = getPlayerMove(theBoard)
			   
				lastMark = theBoard.addSpookyMark_(player2letter, numMark, pos1, pos2)
				numMark += 1
			else: # player vs. computer, and it's the computer's turn

	if not playAgain():
		break

